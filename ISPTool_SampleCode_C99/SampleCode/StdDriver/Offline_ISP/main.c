/**************************************************************************//**
 * @file     main.c
 * @version  V1.00
 * @brief    Implement a mass storage class sample to demonstrate how to
 *           receive an USB short packet.
 *
 * @copyright (C) 2016 Nuvoton Technology Corp. All rights reserved.
 ******************************************************************************/
#include <stdio.h>
#include <string.h>
#include "NuMicro.h"
#include "ISP_CMD.h"
#include "Voltage.h"

//timer 0 FOR USB HOST
//timer 1 for usb host

extern void DO_ISP(int data_address, int start_address, int program_size);

#define ISP_LED_ON PC6=0
#define ISP_LED_OFF PC6=1
#define BUSY PB9
#define PASS PB8

unsigned char button_start = 0;

/*--------------------------------------------------------------------------*/
void SYS_Init(void)
{
    uint32_t volatile i;

    /* Unlock protected registers */
    SYS_UnlockReg();

    /* Set XT1_OUT(PF.2) and XT1_IN(PF.3) to input mode */
    PF->MODE &= ~(GPIO_MODE_MODE2_Msk | GPIO_MODE_MODE3_Msk);

    /* Enable External XTAL (4~24 MHz) */
    CLK_EnableXtalRC(CLK_PWRCTL_HXTEN_Msk);

    /* Waiting for 12MHz clock ready */
    CLK_WaitClockReady(CLK_STATUS_HXTSTB_Msk);

    /* Switch HCLK clock source to HXT */
    CLK_SetHCLK(CLK_CLKSEL0_HCLKSEL_HXT, CLK_CLKDIV0_HCLK(1));

    /* Set core clock as PLL_CLOCK from PLL */
    CLK_SetCoreClock(FREQ_192MHZ);

    /* Set both PCLK0 and PCLK1 as HCLK/2 */
    CLK->PCLKDIV = CLK_PCLKDIV_PCLK0DIV2 | CLK_PCLKDIV_PCLK1DIV2;

    SYS->USBPHY &= ~SYS_USBPHY_HSUSBROLE_Msk;    /* select HSUSBD */
    /* Enable USB HIGH HOST PHY */
    SYS->USBPHY = (SYS->USBPHY & ~(SYS_USBPHY_HSUSBROLE_Msk | SYS_USBPHY_HSUSBACT_Msk)) | SYS_USBPHY_HSUSBEN_Msk;

    for (i = 0; i < 0x1000; i++);  // delay > 10 us

    SYS->USBPHY |= SYS_USBPHY_HSUSBACT_Msk;

    /* Enable IP clock */
    CLK_EnableModuleClock(HSUSBD_MODULE);

    /* Select IP clock source */
    CLK_SetModuleClock(UART0_MODULE, CLK_CLKSEL1_UART0SEL_HXT, CLK_CLKDIV0_UART0(1));

    /* Enable IP clock */
    CLK_EnableModuleClock(UART0_MODULE);

    /* Set GPB multi-function pins for UART0 RXD and TXD */
    SYS->GPA_MFPL &= ~(SYS_GPA_MFPL_PA0MFP_Msk | SYS_GPA_MFPL_PA1MFP_Msk);
    SYS->GPA_MFPL |= (SYS_GPA_MFPL_PA0MFP_UART0_RXD | SYS_GPA_MFPL_PA1MFP_UART0_TXD);


    /* select multi-function pin */
    SYS->GPG_MFPH &= ~(SYS_GPG_MFPH_PG13MFP_Msk     | SYS_GPG_MFPH_PG14MFP_Msk     | SYS_GPG_MFPH_PG11MFP_Msk      | SYS_GPG_MFPH_PG12MFP_Msk);
    SYS->GPG_MFPH |= (SYS_GPG_MFPH_PG13MFP_SD1_CMD | SYS_GPG_MFPH_PG14MFP_SD1_CLK | SYS_GPG_MFPH_PG11MFP_SD1_DAT1 | SYS_GPG_MFPH_PG12MFP_SD1_DAT0);

    SYS->GPG_MFPH &= ~(SYS_GPG_MFPH_PG9MFP_Msk      | SYS_GPG_MFPH_PG10MFP_Msk);
    SYS->GPG_MFPH |= (SYS_GPG_MFPH_PG9MFP_SD1_DAT3 | SYS_GPG_MFPH_PG10MFP_SD1_DAT2);

    SYS->GPD_MFPH &= ~(SYS_GPG_MFPH_PG15MFP_Msk);
    SYS->GPD_MFPH |= (SYS_GPG_MFPH_PG15MFP_SD1_nCD);
    CLK_SetModuleClock(SDH1_MODULE, CLK_CLKSEL0_SDH1SEL_PLL, CLK_CLKDIV0_SDH0(10));

    CLK_EnableModuleClock(SDH1_MODULE);
    CLK_EnableModuleClock(UART0_MODULE);
    CLK_EnableModuleClock(TMR0_MODULE);

    CLK_SetModuleClock(TMR0_MODULE, CLK_CLKSEL1_TMR0SEL_HXT, 0);
    /* User can use SystemCoreClockUpdate() to calculate PllClock, SystemCoreClock and CycylesPerUs automatically. */

    CLK_EnableModuleClock(USBH_MODULE);

    /* USB Host desired input clock is 48 MHz. Set as PLL divided by 4 (192/4 = 48) */
    CLK->CLKDIV0 = (CLK->CLKDIV0 & ~CLK_CLKDIV0_USBDIV_Msk) | CLK_CLKDIV0_USB(4);

    /* Enable USBD and OTG clock */
    CLK->APBCLK0 |= CLK_APBCLK0_USBDCKEN_Msk | CLK_APBCLK0_OTGCKEN_Msk;
    /* Set OTG as USB Host role */
    SYS->USBPHY = (SYS->USBPHY & ~(SYS_USBPHY_USBROLE_Msk)) | SYS_USBPHY_USBEN_Msk | SYS_USBPHY_SBO_Msk | (0x1 << SYS_USBPHY_USBROLE_Pos);
    SYS->GPB_MFPL = (SYS->GPB_MFPL & ~SYS_GPB_MFPL_PB6MFP_Msk) | SYS_GPB_MFPL_PB6MFP_USB_VBUS_EN;

    /* USB_VBUS_ST (USB 1.1 over-current detect pin) multi-function pin - PC.14   */
    SYS->GPB_MFPL = (SYS->GPB_MFPL & ~SYS_GPB_MFPL_PB7MFP_Msk) | SYS_GPB_MFPL_PB7MFP_USB_VBUS_ST;
    SYS->GPA_MFPH &= ~(SYS_GPA_MFPH_PA12MFP_Msk | SYS_GPA_MFPH_PA13MFP_Msk |
                       SYS_GPA_MFPH_PA14MFP_Msk | SYS_GPA_MFPH_PA15MFP_Msk);
    SYS->GPA_MFPH |= SYS_GPA_MFPH_PA12MFP_USB_VBUS | SYS_GPA_MFPH_PA13MFP_USB_D_N |
                     SYS_GPA_MFPH_PA14MFP_USB_D_P | SYS_GPA_MFPH_PA15MFP_USB_OTG_ID;

    SystemCoreClockUpdate();
}

void GPC_IRQHandler(void)
{
    /* To check if PC.5 interrupt occurred */
    if (GPIO_GET_INT_FLAG(PC, BIT7))
    {
        GPIO_CLR_INT_FLAG(PC, BIT7);
        button_start = 1;
    }
}


int32_t main(void)
{
    SYS_Init();

    Voltage_Init();
    Voltage_SupplyTargetPower(1, 3300);

    /* Init UART to 115200-8n1 for print message */
    UART_Open(UART0, 115200);

    /* Endpoint configuration */

    GPIO_SET_DEBOUNCE_TIME(GPIO_DBCTL_DBCLKSRC_LIRC, GPIO_DBCTL_DBCLKSEL_1024);
    GPIO_ENABLE_DEBOUNCE(PC, BIT7);

    GPIO_SetMode(PC, BIT7, GPIO_MODE_INPUT);
    GPIO_EnableInt(PC, 7, GPIO_INT_FALLING);
    NVIC_EnableIRQ(GPC_IRQn);
    /* Start transaction */

    GPIO_SetMode(PC, BIT6, GPIO_MODE_OUTPUT);
    GPIO_SetMode(PB, BIT9, GPIO_MODE_OUTPUT);
    GPIO_SetMode(PB, BIT8, GPIO_MODE_OUTPUT);
    ISP_LED_ON;

    FMC_Open(); 
    /* Enable USBD interrupt */
    NVIC_EnableIRQ(USBD20_IRQn);

    while (1)
    {
        //  SYS_UnlockReg();
        CLK_Idle();

        if (button_start == 1)
        {
            while (PC7 == 0); //wait for button release

            button_start = 0; //clear button
            NVIC_DisableIRQ(USBD20_IRQn);
            NVIC_DisableIRQ(GPC_IRQn);
					
						// store write data into Nu-Link2-Pro data flash
						// change DATA_FLASH_TEST_BASE base on dataflash address.
            int DATA_FLASH_TEST_BASE  = 0x30000;
						// change WRITE_DATA_SIZE base on write data byte size.
						int WRITE_DATA_SIZE = 1024;

						PASS = 1;
					
            DO_ISP(DATA_FLASH_TEST_BASE, 0, WRITE_DATA_SIZE);
						
						PASS = 0;
					
            NVIC_EnableIRQ(USBD20_IRQn);
            NVIC_EnableIRQ(GPC_IRQn);
        }
    }
}



/*** (C) COPYRIGHT 2016 Nuvoton Technology Corp. ***/

