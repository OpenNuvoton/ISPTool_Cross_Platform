#include "stdio.h"
#include "string.h"
#include "NuMicro.h"
#include "ISP_CMD.h"
#include "ISPLib.h"

#define PACKET_SIZE 64
uint8_t rcvbuf[PACKET_SIZE];
uint8_t sendbuf[PACKET_SIZE];
uint8_t file_buffer[512];

unsigned short gcksum;
extern  unsigned int AP_file_totallen;

struct sISP_COMMAND ISP_COMMAND;
#define BOOL  uint8_t
#define PAGE_SIZE                      0x00000200     /* Page size */
#define dbg_printf printf
//#define dbg_printf(...)
extern io_handle_t handle_io;

void WordsCpy(void *dest, void *src, int32_t size)
{
    uint8_t *pu8Src, *pu8Dest;
    int32_t i;

    pu8Dest = (uint8_t *)dest;
    pu8Src = (uint8_t *)src;

    for (i = 0; i < size; i++)
        pu8Dest[i] = pu8Src[i];
}

#define BUSY PB9
#define PASS PB8

ErrNo CmdSyncPackno(void)
{
    ISP_SyncPackNo(&handle_io);
    return ENOERR;
}

void CmdRunLDROM(void)
{
    ISP_RunLDROM(&handle_io);
    //delay for reset
    for (int i = 0; i < 200; i++)
        CLK_SysTickDelay(1000);
}

void CmdRunAPROM(void)
{
    ISP_RunAPROM(&handle_io);

    //delay for reset
    for (int i = 0; i < 200; i++)
        CLK_SysTickDelay(1000);
}

ErrNo CmdFWVersion(unsigned int *fwver)
{
    *fwver = (unsigned int)ISP_GetVersion(&handle_io);
    return 0;
}

ErrNo CmdGetDeviceID(unsigned int *devid)
{
    *devid = ISP_GetDeviceID(&handle_io);
    return 0;
}

ErrNo CmdGetConfig(unsigned int *config)
{
		ISP_ReadConfig(&handle_io, config);
    return 0;
}

volatile unsigned int AUTO_DETECT_VALUE;

void CmdISPOpen(void){
    ISP_Open(&handle_io);
}

void auto_detect_command(void)
{
    int var = 0;

    while(var == 0){
        handle_io.m_uCmdIndex = 1;
        var = ISP_Connect(&handle_io, 50000);
    }
    AUTO_DETECT_VALUE = 0;
}

void fill_file_buffer(int addr, int len){
    uint32_t u32data;
    int i = 0;
    while(i <= len){
        u32data = FMC_Read(addr + i);
        file_buffer[3 + i] = (u32data >> 24) & 0xFF;  
        file_buffer[2 + i] = (u32data >> 16) & 0xFF;  
        file_buffer[1 + i] = (u32data >> 8) & 0xFF;   
        file_buffer[0 + i] = 	u32data & 0xFF; 
        i += 4;
    }
}

ErrNo UpdatedTargetFalsh(uint32_t data_addr, uint32_t in_startaddr, uint32_t in_file_totallen)
{             
    unsigned long AP_file_totallen = in_file_totallen;

    ISP_SyncPackNo(&handle_io);

    for (unsigned long i = 0; i < AP_file_totallen;) {
        unsigned long uLen;
        unsigned int uRetry = 10;
        fill_file_buffer(data_addr + i, 56);
        while (uRetry) {
            ISP_UpdateAPROM(&handle_io, in_startaddr, AP_file_totallen, in_startaddr + i, (unsigned char*)file_buffer, (unsigned int*)&uLen);

            if (handle_io.bResendFlag) {
                uRetry--;
                if (uRetry == 0 || i == 0 || !ISP_Resend(&handle_io)) {
                    BUSY = 0;
                    PASS = 1;
                    return 1;
                }
            } else {
                break;
            }
        }
        i += uLen;
        printf("Programm: %.0f %%\r", (float)((float)((float)i /(float) AP_file_totallen) * (float)100.0));
    }

    BUSY = 0;
    PASS = 0;
    return ENOERR;
}

void init_ISP_command(void)
{
    ISP_COMMAND.ISPSyncPackno = CmdSyncPackno;
    ISP_COMMAND.ISPFWVersion = CmdFWVersion;
    ISP_COMMAND.ISPGetDeviceID = CmdGetDeviceID;
    ISP_COMMAND.ISPGetConfig = CmdGetConfig;
    ISP_COMMAND.ISPCmdRunLDROM = CmdRunLDROM;
    ISP_COMMAND.ISPCmdRunAPROM = CmdRunAPROM;
    ISP_COMMAND.ISPauto_detect_command = auto_detect_command;
    ISP_COMMAND.ISPUpdateFlash = UpdatedTargetFalsh;
    ISP_COMMAND.ISPOpen = CmdISPOpen;
}

void ISPOpen(struct sISP_COMMAND *gISP_COMMAND)
{
    gISP_COMMAND->ISPOpen();
}

int SyncPackno(struct sISP_COMMAND *gISP_COMMAND)
{
    return gISP_COMMAND->ISPSyncPackno();
}

void Auto_Detect_Connect(struct sISP_COMMAND *gISP_COMMAND)
{
    gISP_COMMAND->ISPauto_detect_command();
}


int FWVersion(struct sISP_COMMAND *gISP_COMMAND, uint32_t *buff)
{
    return gISP_COMMAND->ISPFWVersion(buff);
}


int GetDeviceID(struct sISP_COMMAND *gISP_COMMAND, uint32_t *buff)
{
    return gISP_COMMAND->ISPGetDeviceID(buff);
}

int GetConfig(struct sISP_COMMAND *gISP_COMMAND, uint32_t *buff)
{
    return gISP_COMMAND->ISPGetConfig(buff);
}

void RunLDROM(struct sISP_COMMAND *gISP_COMMAND)
{
    gISP_COMMAND->ISPCmdRunLDROM();
}

void RunAPROM(struct sISP_COMMAND *gISP_COMMAND)
{
    gISP_COMMAND->ISPCmdRunAPROM();
}

int Updated_Target_Flash(struct sISP_COMMAND *gISP_COMMAND, uint32_t data_addr, uint32_t in_startaddr, uint32_t in_file_totallen)
{
    return gISP_COMMAND->ISPUpdateFlash(data_addr, in_startaddr, in_file_totallen);
}


