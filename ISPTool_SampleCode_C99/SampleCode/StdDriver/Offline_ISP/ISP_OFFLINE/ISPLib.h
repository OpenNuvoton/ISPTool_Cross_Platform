//select the interface 

#define ISP_UART
//#define ISP_I2C
//#define ISP_SPI
//#define ISP_RS485
//#define ISP_CAN

#define CMD_GET_VERSION     	0x000000A6
#define CMD_UPDATE_APROM		0x000000A0
#define CMD_SYNC_PACKNO			0x000000A4
#define CMD_UPDATE_CONFIG   	0x000000A1
#define CMD_ERASE_ALL 	    	0x000000A3
#define CMD_READ_CONFIG     	0x000000A2
#define CMD_GET_DEVICEID    	0x000000B1
#define CMD_RUN_APROM			0x000000AB
#define CMD_RUN_LDROM			0x000000AC
#define CMD_CONNECT				0x000000AE
#define CMD_UPDATE_DATAFLASH 	0x000000C3
#define CMD_RESEND_PACKET   	0x000000FF
#define CMD_ERASE_SPIFLASH      0x000000D0
#define CMD_UPDATE_SPIFLASH     0x000000D1

#define USBCMD_TIMEOUT				50000
#define USBCMD_TIMEOUT_LONG			250000

#ifndef FALSE
#define FALSE           (0UL) 
#endif
#ifndef TRUE
#define TRUE           (1UL) 
#endif

typedef struct
{
	void (*init)(void);
	unsigned int (*open)(void);
	void (*close)(void);
	unsigned int (*write)(unsigned int dwMilliseconds, unsigned char* pcBuffer);
	unsigned int (*read)(unsigned int dwMilliseconds, unsigned char* pcBuffer);
} DEV_IO;

typedef struct
{
	unsigned int dev_open;
	unsigned int bResendFlag;
	unsigned char m_usCheckSum;
	unsigned int m_uCmdIndex;
	unsigned char ac_buffer[65];
	void* dev_io;
	DEV_IO m_dev_io;
} io_handle_t;

#ifdef __cplusplus
extern "C" {
#endif

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

// use the open/close/read/write third party provided
DLL_EXPORT  unsigned short Checksum(unsigned char* buf, unsigned int len);

DLL_EXPORT  unsigned int ISP_Open(io_handle_t* handle);
DLL_EXPORT  void ISP_Close(io_handle_t* handle);
DLL_EXPORT  void ISP_ReOpen(io_handle_t* handle);

DLL_EXPORT  unsigned int ISP_Read(io_handle_t* handle, unsigned char* pcBuffer, unsigned int szMaxLen, unsigned int dwMilliseconds, unsigned int bCheckIndex);
DLL_EXPORT  unsigned int ISP_Write(io_handle_t* handle, unsigned int uCmd, unsigned char* pcBuffer, unsigned int dwLen, unsigned int dwMilliseconds);

DLL_EXPORT  void ISP_UpdateConfig(io_handle_t* handle, unsigned int config[], unsigned int response[]);
DLL_EXPORT  void ISP_ReadConfig(io_handle_t* handle, unsigned int config[]);
DLL_EXPORT  void ISP_SyncPackNo(io_handle_t* handle);
DLL_EXPORT  void ISP_UpdateAPROM(io_handle_t* handle, unsigned int start_addr, unsigned int total_len, unsigned int cur_addr, unsigned char* buffer, unsigned int* update_len);
DLL_EXPORT  void ISP_UpdateDataFlash(io_handle_t* handle, unsigned int start_addr, unsigned int total_len, unsigned int cur_addr, unsigned char* buffer, unsigned int* update_len);

DLL_EXPORT  unsigned int ISP_EraseAll(io_handle_t* handle);
DLL_EXPORT  unsigned int ISP_RunAPROM(io_handle_t* handle);
DLL_EXPORT  unsigned int ISP_RunLDROM(io_handle_t* handle);

DLL_EXPORT  unsigned int ISP_Connect(io_handle_t* handle, unsigned int dwMilliseconds);
DLL_EXPORT  unsigned int ISP_Resend(io_handle_t* handle);

DLL_EXPORT  unsigned char ISP_GetVersion(io_handle_t* handle);
DLL_EXPORT  unsigned int ISP_GetDeviceID(io_handle_t* handle);

DLL_EXPORT  unsigned int ISP_EraseSPI(io_handle_t* handle, unsigned int offset, unsigned int total_len);
DLL_EXPORT  unsigned int ISP_UpdateSPI(io_handle_t* handle, unsigned int start_addr, unsigned int total_len, const char* buffer);

DLL_EXPORT  unsigned int ISP_CAN_Write(io_handle_t* handle, unsigned int uCmd, unsigned int uData, unsigned int dwMilliseconds);
DLL_EXPORT  unsigned int ISP_CAN_Read(io_handle_t* handle, unsigned int dwMilliseconds);
DLL_EXPORT  void ISP_CAN_UpdateConfig(io_handle_t* handle, unsigned int config[], unsigned int response[], unsigned char offset);
DLL_EXPORT  void ISP_CAN_ReadConfig(io_handle_t* handle, unsigned int config[], unsigned char offset);

#ifdef __cplusplus
}
#endif
