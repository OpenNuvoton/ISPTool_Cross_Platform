#include "isplib.h"
#include "stdio.h"
#include "NuMicro.h"
#include "stdint.h"

#ifdef ISP_I2C

#include "isplib_func.h"
io_handle_t handle_io;

#define MAX_PKT_SIZE            (64)

#define BUSY PB9
#define PASS PB8

void m_dev_io_init() 
{
    uint32_t u32ClkDiv;
    uint32_t u32Pclk = FREQ_192MHZ / 2;
		uint32_t u32BusClock = 100000;
    /* Enable IP clock */
    CLK->APBCLK1 |= CLK_APBCLK1_USCI0CKEN_Msk;
    /* Set UI2C0 multi-function pins */
    SYS->GPE_MFPL = (SYS->GPE_MFPL & ~(SYS_GPE_MFPL_PE2MFP_Msk | SYS_GPE_MFPL_PE3MFP_Msk)) |
                    (SYS_GPE_MFPL_PE2MFP_USCI0_CLK | SYS_GPE_MFPL_PE3MFP_USCI0_DAT0);
    /* USCI_I2C clock pin enable schmitt trigger */
    PE->SMTEN |= GPIO_SMTEN_SMTEN2_Msk;
    /* Open USCI_I2C0 and set clock to 100k */
    // UI2C_Open(UI2C0, u32ClkSpeed);
    u32ClkDiv = (uint32_t)((((((u32Pclk / 2U) * 10U) / (u32BusClock)) + 5U) / 10U) - 1U); /* Compute proper divider for USCI_I2C clock */
    /* Enable USCI_I2C protocol */
    UI2C0->CTL &= ~UI2C_CTL_FUNMODE_Msk;
    UI2C0->CTL = 4U << UI2C_CTL_FUNMODE_Pos;
    /* Data format configuration */
    /* 8 bit data length */
    UI2C0->LINECTL &= ~UI2C_LINECTL_DWIDTH_Msk;
    UI2C0->LINECTL |= 8U << UI2C_LINECTL_DWIDTH_Pos;
    /* MSB data format */
    UI2C0->LINECTL &= ~UI2C_LINECTL_LSB_Msk;
    /* Set USCI_I2C bus clock */
    UI2C0->BRGEN &= ~UI2C_BRGEN_CLKDIV_Msk;
    UI2C0->BRGEN |= (u32ClkDiv << UI2C_BRGEN_CLKDIV_Pos);
    UI2C0->PROTCTL |=  UI2C_PROTCTL_PROTEN_Msk;
    /* Get USCI_I2C0 Bus Clock */
    // printf("UI2C0 clock %d Hz\n", UI2C_GetBusClockFreq(UI2C0));
    /* Set USCI_I2C0 Slave Addresses */
    // UI2C0->DEVADDR0  = 0x60;
    UI2C0->PROTCTL  = (UI2C0->PROTCTL & ~UI2C_PROTCTL_GCFUNC_Msk) | UI2C_GCMODE_DISABLE;
    /* Enable UI2C0 protocol interrupt */
    UI2C_ENABLE_PROT_INT(UI2C0, (UI2C_PROTIEN_ACKIEN_Msk | UI2C_PROTIEN_NACKIEN_Msk | UI2C_PROTIEN_STORIEN_Msk | UI2C_PROTIEN_STARIEN_Msk));
    // NVIC_EnableIRQ(USCI0_IRQn);
}
unsigned int m_dev_io_open() {
    return TRUE;
}

void m_dev_io_close() {

}

unsigned int m_dev_io_read(unsigned int dwMilliseconds, unsigned char* pcBuffer) {
    BUSY = 0;
		int ret = UI2C_ReadMultiBytes(UI2C0, 0x60, (uint8_t *)pcBuffer + 1, 64);
		return ret;
}

unsigned int m_dev_io_write(unsigned int dwMilliseconds, unsigned char* pcBuffer) {
    BUSY = 1;
		UI2C_WriteMultiBytes(UI2C0, 0x60, (uint8_t *)pcBuffer + 1, 64);   
    return 1;
}
#endif