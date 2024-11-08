#include <stdio.h>
#include "NuMicro.h"
#include "ISP_CMD.h"
#include "Voltage.h"
#include <string.h>
#include "isplib.h"
#include "isplib_func.h"

extern void CmdRunAPROM(void);
extern void CmdRunLDROM(void);

extern volatile unsigned int AUTO_DETECT_VALUE;

extern struct sISP_COMMAND ISP_COMMAND;
extern volatile unsigned int AP_file_totallen;

uint32_t config[2];

extern io_handle_t handle_io;

int ISP_PROGRAM(int data_address, int start_address, int program_size)
{
    ErrNo ret;
    ret = Updated_Target_Flash(&ISP_COMMAND, data_address, start_address, program_size);

    return ret;
}

int ISP_INTERFACE_INIT(void)
{
    handle_io.m_dev_io.init = m_dev_io_init;
    handle_io.m_dev_io.open = m_dev_io_open;
    handle_io.m_dev_io.close = m_dev_io_close;
    handle_io.m_dev_io.write = m_dev_io_write;
    handle_io.m_dev_io.read = m_dev_io_read;
    handle_io.m_dev_io.init();

    init_ISP_command();

    ISPOpen(&ISP_COMMAND);

    return 1;
}

//only rs485, uart support auto detect command
int ISP_AUTO_DETECT(void)
{
    AUTO_DETECT_VALUE = 1;

    if (AUTO_DETECT_VALUE == 1)
    {
        Auto_Detect_Connect(&ISP_COMMAND);
    }

    AUTO_DETECT_VALUE = 1;

    SyncPackno(&ISP_COMMAND); //return 0 =>pass

    AUTO_DETECT_VALUE = 0;

    return 1;
}


int ISP_CmdSyncPackno(void)
{
    AUTO_DETECT_VALUE = 0;
    SyncPackno(&ISP_COMMAND);
    return 1;
}

int ISP_CmdFWVersion(void)
{
    uint32_t fwversion;
    FWVersion(&ISP_COMMAND, &fwversion);
    return 1;
}

int ISP_CmdGetDeviceID(void)
{
    uint32_t devid;
    GetDeviceID(&ISP_COMMAND, &devid);
    return 1;
}

int ISP_CmdGetConfig(void)
{
    unsigned int config[2];
    GetConfig(&ISP_COMMAND, config);
    return 1;
}


int ISP_CmdJumpAPROM(void)
{
    CmdRunAPROM();
    return 1;
}

int ISP_CmdJumpLDROM()
{
    CmdRunLDROM();
    return 1;
}

void DO_ISP(int data_address, int start_address, int program_size){
    ISP_INTERFACE_INIT();
	
//#if defined(ISP_UART) || defined(ISP_RS485)
    ISP_AUTO_DETECT();
#if defined(ISP_SPI)
		CLK_SysTickDelay(10000);
#endif
//#endif
	
    ISP_PROGRAM(data_address, start_address, program_size);
}

