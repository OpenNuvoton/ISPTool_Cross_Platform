#include "isplib.h"
#include "stdio.h"
#include "NuMicro.h"
#include "stdint.h"

#ifdef ISP_RS485

#include "isplib_func.h"
io_handle_t handle_io;

#define MAX_PKT_SIZE            (64)

#define BUSY PB9
#define PASS PB8

#define nRTSPin						(PE12)
#define REVEIVE_MODE			(0)
#define TRANSMIT_MODE			(1)

uint8_t  uart_rcvbuf[64] = {0};

uint8_t volatile bUartDataReady = 0;
uint8_t volatile bufhead = 0;

extern volatile unsigned int AUTO_DETECT_VALUE;

void UART1_IRQHandler(void)
{
    /*----- Determine interrupt source -----*/
    uint32_t u32IntSrc = UART1->INTSTS;

    if (u32IntSrc & 0x11) { //RDA FIFO interrupt & RDA timeout interrupt
        while (((UART1->FIFOSTS & UART_FIFOSTS_RXEMPTY_Msk) == 0) && (bufhead < MAX_PKT_SIZE)) {	//RX fifo not empty
            uart_rcvbuf[bufhead++] = UART1->DAT;
        }
    }

    if (bufhead == MAX_PKT_SIZE) {
        bUartDataReady = TRUE;
        bufhead = 0;
       // _EP_HID_IN_Handler(EP_HID_IN, uart_rcvbuf, 64);
    } else if (u32IntSrc & 0x10) {
        bufhead = 0;
    }
}

void m_dev_io_init()
{
    /* Enable UART module clock */
    CLK->APBCLK0 |= CLK_APBCLK0_UART1CKEN_Msk;
    /* Select UART module clock source */
    CLK->CLKSEL1 &= ~CLK_CLKSEL1_UART1SEL_Msk;
    CLK->CLKSEL1 |= CLK_CLKSEL1_UART1SEL_HIRC;
    PE->MODE = (PE->MODE & ~(0x3ul << (12 << 1))) | (GPIO_MODE_OUTPUT << (12 << 1));
    nRTSPin = REVEIVE_MODE;
    SYS->GPC_MFPH = (SYS->GPC_MFPH & ~(SYS_GPC_MFPH_PC8MFP_Msk)) | SYS_GPC_MFPH_PC8MFP_UART1_RXD;
    SYS->GPE_MFPH = (SYS->GPE_MFPH & ~(SYS_GPE_MFPH_PE13MFP_Msk)) | SYS_GPE_MFPH_PE13MFP_UART1_TXD;
    /*---------------------------------------------------------------------------------------------------------*/
    /* Init UART                                                                                               */
    /*---------------------------------------------------------------------------------------------------------*/
    /* Select UART function */
    UART1->FUNCSEL = UART_FUNCSEL_UART;
    /* Set UART line configuration */
    UART1->LINE = UART_WORD_LEN_8 | UART_PARITY_NONE | UART_STOP_BIT_1;
    /* Set UART Rx and RTS trigger level */
    UART1->FIFO = UART_FIFO_RFITL_14BYTES | UART_FIFO_RTSTRGLV_14BYTES;
    /* Set UART baud rate */
    UART1->BAUD = (UART_BAUD_MODE2 | UART_BAUD_MODE2_DIVIDER(__HIRC, 115200));
    /* Set time-out interrupt comparator */
    UART1->TOUT = (UART1->TOUT & ~UART_TOUT_TOIC_Msk) | (0x40);
    NVIC_SetPriority(UART1_IRQn, 2);
    NVIC_EnableIRQ(UART1_IRQn);
    /* 0x0811 */
    UART1->INTEN = (UART_INTEN_TOCNTEN_Msk | UART_INTEN_RXTOIEN_Msk | UART_INTEN_RDAIEN_Msk);
}

void RS485_WriteMultiBytes(uint8_t *data)
{
    uint32_t i;
    NVIC_DisableIRQ(UART1_IRQn);
    bUartDataReady = 0;
    nRTSPin = TRANSMIT_MODE;

    for (i = 0; i < MAX_PKT_SIZE; i++) {
        while ((UART1->FIFOSTS & UART_FIFOSTS_TXFULL_Msk));

        UART1->DAT = data[i];
    }

    while ((UART1->FIFOSTS & UART_FIFOSTS_TXEMPTYF_Msk) == 0);

    nRTSPin = REVEIVE_MODE;
    NVIC_EnableIRQ(UART1_IRQn);
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
		unsigned int readlen = 0;
	
    if (AUTO_DETECT_VALUE == 0)
    {
        while (bUartDataReady == 0);
    }
    else
    {
        SysTick->LOAD = 20000 * CyclesPerUs;
        SysTick->VAL  = 0x0UL;
        SysTick->CTRL = SysTick_CTRL_CLKSOURCE_Msk | SysTick_CTRL_ENABLE_Msk;

        while (bUartDataReady == 0)
        {
            /* Waiting for down-count to zero */
            if ((SysTick->CTRL & SysTick_CTRL_COUNTFLAG_Msk) != 0UL)
            {
                break;
            }
        }
        /* Disable SysTick counter */
        SysTick->CTRL = 0UL;
    }

    for (i = 0; i < rxlen; i++)
    {
        pcBuffer[i] = uart_rcvbuf[i];
				readlen ++;
    }

    return (unsigned int) readlen;
}

unsigned int m_dev_io_write(unsigned int dwMilliseconds, unsigned char* pcBuffer) 
{
		BUSY = 1;
    RS485_WriteMultiBytes((uint8_t *)pcBuffer + 1);
    return 1;
}

#endif