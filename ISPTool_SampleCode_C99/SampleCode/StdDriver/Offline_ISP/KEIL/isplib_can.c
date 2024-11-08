#include "isplib.h"
#include "stdio.h"
#include "NuMicro.h"
#include "stdint.h"

#ifdef ISP_CAN
#define GPIO_SETMODE(port, pin, u32Mode) port->MODE = (port->MODE & ~(0x3ul << (pin << 1))) | (u32Mode << (pin << 1));

#include "isplib_func.h"
#include "string.h"

io_handle_t handle_io;

#define MAX_PKT_SIZE            (64)

#define BUSY PB9
#define PASS PB8

#define CAN_BAUD_RATE                     500000
#define Master_ISP_ID                     0x487
#define Device0_ISP_ID                    0x784
#define CAN_ISP_DtatLength                0x08

unsigned char loca_buffer[64];
unsigned char response_buff[64];
volatile uint32_t StartAddress, TotalLen;
volatile uint32_t glcmd;
volatile uint8_t u8CAN_PackageFlag = 0;
STR_CANMSG_T rrMsg;

int32_t CAN_Package_Tx(CAN_T *tCAN, uint8_t *data)
{
    STR_CANMSG_T tMsg;
    /* Send a 11-bit Standard Identifier message */
    tMsg.FrameType = CAN_DATA_FRAME;
    tMsg.IdType    = CAN_STD_ID;
    tMsg.Id        = Master_ISP_ID;
    tMsg.DLC       = CAN_ISP_DtatLength;
    memcpy(&tMsg.Data, data, 8);
    u8CAN_PackageFlag = 0;
    return CAN_Transmit(tCAN, MSG(5), &tMsg);
}

void CAN_Transmit_ISP(uint32_t cmd, uint32_t data)
{
    uint32_t buf[2];
    buf[0] = cmd;
    buf[1] = data;
    CAN_Package_Tx(CAN1, (uint8_t *)buf);
}

void CAN_MsgInterrupt(CAN_T *tCAN, uint32_t u32IIDR)
{
    if (u32IIDR == 1) {
        CAN_Receive(tCAN, 0, &rrMsg);
        u8CAN_PackageFlag = 1;
        //_EP_HID_IN_Handler(EP_HID_IN, &rrMsg.Data[0], 64);
    }
}

void CAN1_IRQHandler(void)
{
    uint32_t u8IIDRstatus;
    u8IIDRstatus = CAN1->IIDR;

    if (u8IIDRstatus == 0x00008000) {     /* Check Status Interrupt Flag (Error status Int and Status change Int) */
        /**************************/
        /* Status Change interrupt*/
        /**************************/
        if (CAN1->STATUS & CAN_STATUS_RXOK_Msk) {
            CAN1->STATUS &= ~CAN_STATUS_RXOK_Msk;   /* Clear RxOK status*/
        }

        if (CAN1->STATUS & CAN_STATUS_TXOK_Msk) {
            CAN1->STATUS &= ~CAN_STATUS_TXOK_Msk;    /* Clear TxOK status*/
        }
    } else if (u8IIDRstatus != 0) {
        CAN_MsgInterrupt(CAN1, u8IIDRstatus);
        CAN_CLR_INT_PENDING_BIT(CAN1, (u8IIDRstatus - 1)); /* Clear Interrupt Pending */
    }
}

void m_dev_io_init()
{
    /* Enable CAN1 module clock */
    CLK->APBCLK0 |= CLK_APBCLK0_CAN1CKEN_Msk;
    /* Set PC multi-function pins for CAN1 RXD(PC.9) and TXD(PC.10) */
    SYS->GPC_MFPH = (SYS->GPC_MFPH & ~(SYS_GPC_MFPH_PC9MFP_Msk | SYS_GPC_MFPH_PC10MFP_Msk)) |
                    (SYS_GPC_MFPH_PC9MFP_CAN1_RXD | SYS_GPC_MFPH_PC10MFP_CAN1_TXD);
    /* Set CAN transceiver to high speed mode */
    GPIO_SETMODE(PC, 11, GPIO_MODE_OUTPUT);
    PC11 = 0;
    CAN_SetBaudRate(CAN1, CAN_BAUD_RATE);
    CAN_EnableInt(CAN1, (CAN_CON_IE_Msk | CAN_CON_SIE_Msk | CAN_CON_EIE_Msk));
    NVIC_SetPriority(CAN1_IRQn, (1 << __NVIC_PRIO_BITS) - 2);
    NVIC_EnableIRQ(CAN1_IRQn);
    /* Set CAN reveive message */
    //can_setRxMsg(CAN1);
    CAN_SetRxMsg(CAN1, MSG(0), CAN_STD_ID, Device0_ISP_ID);
}

unsigned int m_dev_io_open() {
    return TRUE;
}

void m_dev_io_close() {

}

unsigned int m_dev_io_read(unsigned int dwMilliseconds, unsigned char* pcBuffer) {
    BUSY = 0;
    uint8_t i;
    uint32_t rxlen = 64;

    for (i = 0; i < rxlen; i++)
    {
        pcBuffer[i] = response_buff[i];
    }

    return rxlen;
}

unsigned int m_dev_io_write(unsigned int dwMilliseconds, unsigned char* pcBuffer) {
    BUSY = 1;
	
    int i;
    uint32_t txlen = 64;
    uint32_t g_packno;
    uint8_t *response;
    uint32_t lcmd, outdata;
    uint16_t lcksum;
    response = response_buff;

    for (i = 0; i < txlen; i++)
    {
        loca_buffer[i] = pcBuffer[i];
    }

    lcmd = inpw(pcBuffer + 3);
    g_packno = inpw(pcBuffer + 7);


    lcksum = Checksum(pcBuffer, txlen);
    outps(response, lcksum);
    outpw(response + 4, ++g_packno);

    if (glcmd == CMD_UPDATE_APROM)
    {
        txlen = 64 - 8;

        if (TotalLen < txlen)
        {
            txlen = TotalLen;//prevent last package from over writing
            TotalLen = 0;
            glcmd = 0;
        }
        else
        {
            TotalLen = TotalLen - txlen;
        }

        for (i = 0; i < txlen; i = i + 4)
        {
            outdata = inpw(pcBuffer + i + 8);
            //printf("0x%x\n\r",outdata);
            CAN_Transmit_ISP(StartAddress, outdata);

            while (u8CAN_PackageFlag == 0);

            if (outdata != *(unsigned int *)&rrMsg.Data[4])
            {
                outps(response, 0);
                outpw(response + 4, 0);

                return 1;
            }

            StartAddress = StartAddress + 4;
        }

    }

    if (lcmd == CMD_UPDATE_APROM)
    {
        StartAddress = inpw(pcBuffer + 8);
        TotalLen = inpw(pcBuffer + 12);
        txlen = 64 - 16;

        if (TotalLen < txlen)
        {
            txlen = TotalLen;//prevent last package from over writing
        }
        else
        {
            glcmd = CMD_UPDATE_APROM;
            TotalLen = TotalLen - txlen;
        }

        for (i = 0; i < txlen; i = i + 4)
        {
            //printf("0x%x\n\r",StartAddress);
            outdata = inpw(pcBuffer + i + 16);
            // printf("0x%x\n\r",outdata);
            CAN_Transmit_ISP(StartAddress, outdata);

            while (u8CAN_PackageFlag == 0);

            if (outdata != *(unsigned int *)&rrMsg.Data[4])
            {
                outps(response, 0);
                outpw(response + 4, 0);

                return 1;
            }

            StartAddress = StartAddress + 4;
        }

    }

    if (lcmd == CMD_GET_DEVICEID)
    {
        CAN_Transmit_ISP(0xB1000000, 0);

        while (u8CAN_PackageFlag == 0);

        //printf("0x%x",*(unsigned int*)&rrMsg.Data[4]); //conver data to uint32
        outpw(response + 8, *(unsigned int *)&rrMsg.Data[4]);
    }


    if (lcmd == CMD_RUN_APROM)
    {
        CAN_Transmit_ISP(0xAB000000, 0);
    }

    if (lcmd == CMD_GET_VERSION)
    {
        outpw(response + 8, 0xffffff5a);
    }
/*
    if (lcmd == CMD_GET_FLASHMODE)
    {
        outpw(response + 8, 0X02);
    }
*/
    if (lcmd == CMD_READ_CONFIG)
    {
        CAN_Transmit_ISP(0xA2000000, 0x00300000);//CONFIG0

        while (u8CAN_PackageFlag == 0);

        outpw(response + 8, *(unsigned int *)&rrMsg.Data[4]);

        CAN_Transmit_ISP(0xA2000000, 0x00300004);//CONFIG1

        while (u8CAN_PackageFlag == 0);

        outpw(response + 12, *(unsigned int *)&rrMsg.Data[4]);

        CAN_Transmit_ISP(0xA2000000, 0x00300008);//CONFIG2

        while (u8CAN_PackageFlag == 0);

        outpw(response + 16, *(unsigned int *)&rrMsg.Data[4]);

        CAN_Transmit_ISP(0xA2000000, 0x0030000C);//CONFIG2

        while (u8CAN_PackageFlag == 0);

        outpw(response + 20, *(unsigned int *)&rrMsg.Data[4]);
    }

    return 1;
}
#endif