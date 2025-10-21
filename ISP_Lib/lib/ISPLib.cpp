#include <stdio.h>
#include <string.h>
#include "ISPLib.h"

unsigned short Checksum(unsigned char* buf, unsigned int len)
{
    unsigned int i;
    unsigned short c;
    for (c = 0, i = 0; i < len; i++) {
        c += buf[i];
    }
    return (c);
}

unsigned int ISP_Open(io_handle_t* handle)
{
    if (handle->dev_open) {
        return TRUE;
    }
    // do third party open()
    if (handle->m_dev_io.open()) {
        handle->dev_open = TRUE;
    }
    return handle->dev_open;
}

void ISP_Close(io_handle_t* handle)
{
    if (handle->dev_open == FALSE) {
        return;
    }
    handle->m_dev_io.close();
    handle->dev_open = FALSE;
}

void ISP_ReOpen(io_handle_t* handle)
{
    ISP_Close(handle);
    ISP_Open(handle);
}

unsigned int ISP_Read(io_handle_t* handle, unsigned char* pcBuffer,
                      unsigned int szMaxLen, unsigned int dwMilliseconds, unsigned int bCheckIndex)
{
    unsigned short usCheckSum = 0;
    unsigned int uCmdIndex = 0;
    unsigned int dwLength = 0;
    handle->bResendFlag = FALSE;
    while (1) {
        if (handle->dev_open == FALSE) {
            return FALSE;
        }
        memset(handle->ac_buffer, 0, sizeof(handle->ac_buffer));
        dwLength = handle->m_dev_io.read(dwMilliseconds, handle->ac_buffer);
        if (!dwLength) {
            return FALSE;
        }
        usCheckSum = *((unsigned short*) & (handle->ac_buffer[1]));
        uCmdIndex = *((unsigned long*) & (handle->ac_buffer[5]));
        if (dwLength >= 8 && (!bCheckIndex || uCmdIndex == handle->m_uCmdIndex - 1) &&
        usCheckSum == handle->m_usCheckSum) {
            if (szMaxLen > dwLength - 8) {
                szMaxLen = dwLength - 8;
            }
            if (pcBuffer != NULL && szMaxLen > 0) {
                memcpy(pcBuffer, (unsigned char*) & (handle->ac_buffer[9]), szMaxLen);
            }
            return TRUE;
        } else {
            handle->bResendFlag = TRUE;
            break;
        }
    }
    return FALSE;
}

unsigned int ISP_Write(io_handle_t* handle, unsigned int uCmd,
                       unsigned char *pcBuffer, unsigned int dwLen, unsigned int dwMilliseconds)
{
    unsigned int dwLength = 0;
    unsigned int dwCmdLength = dwLen;
    unsigned int bRet = FALSE;
    if (handle->dev_open == FALSE) {
        return FALSE;
    }
    if (dwCmdLength > sizeof(handle->ac_buffer) - 9) {
        dwCmdLength = sizeof(handle->ac_buffer) - 9;
    }
    memset(handle->ac_buffer, 0, sizeof(handle->ac_buffer));
    memcpy(&handle->ac_buffer[1], &uCmd, sizeof(uCmd));
    memcpy(&handle->ac_buffer[5], &handle->m_uCmdIndex, sizeof(handle->m_uCmdIndex));
    if (pcBuffer != NULL && dwCmdLength > 0) {
        memcpy((unsigned char*)(&(handle->ac_buffer[9])), pcBuffer, dwCmdLength);
    }
    handle->m_usCheckSum = Checksum(&(handle->ac_buffer[1]),
                                    sizeof(handle->ac_buffer) - 1);
    if (handle->m_intf > 2) {
        *(&(handle->ac_buffer[2])) = static_cast<char>(handle->m_intf);
    }
    bRet = handle->m_dev_io.write(dwMilliseconds, handle->ac_buffer);
    if (bRet != FALSE) {
        handle->m_uCmdIndex += 2;
    } else {
        handle->m_dev_io.close();
    }
    return bRet;
}


void ISP_UpdateConfig(io_handle_t* handle, unsigned int config[],
                      unsigned int response[])
{
    ISP_Write(handle, CMD_UPDATE_CONFIG, (unsigned char*)config, 56,
              USBCMD_TIMEOUT_LONG);
    ISP_Read(handle, (unsigned char*)response, 56, USBCMD_TIMEOUT_LONG, TRUE);
}

void ISP_UpdateConfig_Ext(io_handle_t* handle, unsigned int config[],
                      unsigned int response[], unsigned int i)
{
    unsigned char ext_buffer[8];
    unsigned int index = i;
    if (i >= 16 && i <= 18) {
        index += 16;  // CONFIG_16 at 0x0F300080 not 0x0F300040
    }
    unsigned int j = i - i % 2;
    unsigned int index_j = index - index % 2;
    memcpy(&ext_buffer[0], &index_j, 4);
    memcpy(&ext_buffer[4], &config[j], 4);
    if (j + 1 <= 18) {
        memcpy(&ext_buffer[8], &config[j + 1], 4);
    }
    else {
        unsigned int empty = 0xFFFFFFFF;
        memcpy(&ext_buffer[8], &empty, 4);
    }
    ISP_Write(handle, CMD_UPDATE_CONFIG_EXT, ext_buffer, 12, USBCMD_TIMEOUT_LONG);
    ISP_Read(handle, (unsigned char*)&response[j], 8, USBCMD_TIMEOUT_LONG, TRUE);
}

void ISP_ReadConfig(io_handle_t* handle, unsigned int config[])
{
    ISP_Write(handle, CMD_READ_CONFIG, NULL, 0, USBCMD_TIMEOUT);
    ISP_Read(handle, (unsigned char*)config, 56, USBCMD_TIMEOUT, TRUE);
}

void ISP_ReadConfig_Ext(io_handle_t* handle, unsigned int config[], unsigned int i)
{
    unsigned int index = i;
    if (i >= 16 && i <= 18) {
        index += 16;  // CONFIG_16 at 0x0F300080 not 0x0F300040
    }
    ISP_Write(handle, CMD_READ_CONFIG_EXT, (unsigned char*)&index, 0, USBCMD_TIMEOUT);
    ISP_Read(handle, (unsigned char*)&config[i], 4, USBCMD_TIMEOUT, TRUE);
}

void ISP_SyncPackNo(io_handle_t* handle)
{
    handle->m_uCmdIndex = 1;
    ISP_Write(handle, CMD_SYNC_PACKNO, (unsigned char*) & (handle->m_uCmdIndex), 4,
              USBCMD_TIMEOUT);
    ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT, FALSE);
}

void ISP_UpdateAPROM(io_handle_t* handle, unsigned int start_addr,
                     unsigned int total_len, unsigned int cur_addr, unsigned char *buffer,
                     unsigned int *update_len)
{
    unsigned int write_len = total_len - (cur_addr - start_addr);
    unsigned char acBuffer[56];
    if (start_addr == cur_addr) {
        if (write_len > sizeof(acBuffer) - 8) {
            write_len = sizeof(acBuffer) - 8;
        }
        memcpy(&acBuffer[0], &start_addr, 4);
        memcpy(&acBuffer[4], &total_len, 4);
        memcpy(&acBuffer[8], buffer, write_len);
        ISP_Write(handle, CMD_UPDATE_APROM, acBuffer, write_len + 8,
                  USBCMD_TIMEOUT_LONG);
        ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, TRUE);
    } else {
        if (write_len > sizeof(acBuffer)) {
            write_len = sizeof(acBuffer);
        }
        ISP_Write(handle, 0, buffer, write_len, USBCMD_TIMEOUT_LONG);
        ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, TRUE);
    }
    if (update_len != NULL) {
        *update_len = write_len;
    }
}

void ISP_UpdateDataFlash(io_handle_t* handle, unsigned int start_addr,
                         unsigned int total_len, unsigned int cur_addr, unsigned char *buffer,
                         unsigned int *update_len)
{
    unsigned int write_len = total_len - (cur_addr - start_addr);
    unsigned char acBuffer[56];
    if (start_addr == cur_addr) {
        if (write_len > sizeof(acBuffer) - 8) {
            write_len = sizeof(acBuffer) - 8;
        }
        memcpy(&acBuffer[0], &start_addr, 4);
        memcpy(&acBuffer[4], &total_len, 4);
        memcpy(&acBuffer[8], buffer, write_len);
        ISP_Write(handle, CMD_UPDATE_DATAFLASH, acBuffer, write_len + 8,
                  USBCMD_TIMEOUT_LONG);
        ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, TRUE);
    } else {
        if (write_len > sizeof(acBuffer)) {
            write_len = sizeof(acBuffer);
        }
        ISP_Write(handle, 0, buffer, write_len, USBCMD_TIMEOUT_LONG);
        ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, TRUE);
    }
    if (update_len != NULL) {
        *update_len = write_len;
    }
}

unsigned int ISP_EraseAll(io_handle_t* handle)
{
    unsigned int ret = FALSE;
    if (ISP_Write(handle, CMD_ERASE_ALL, NULL, 0, USBCMD_TIMEOUT_LONG)) {
        ret = ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, TRUE);
    }
    return ret;
}

unsigned int ISP_RunAPROM(io_handle_t* handle)
{
    return ISP_Write(handle, CMD_RUN_APROM, NULL, 0, USBCMD_TIMEOUT_LONG);
}

unsigned int ISP_RunLDROM(io_handle_t* handle)
{
    return ISP_Write(handle, CMD_RUN_LDROM, NULL, 0, USBCMD_TIMEOUT_LONG);
}

unsigned int ISP_Connect(io_handle_t* handle, unsigned int dwMilliseconds)
{
    unsigned int ret = FALSE;
    unsigned int uID;
    if (ISP_Write(handle, CMD_CONNECT, NULL, 0, USBCMD_TIMEOUT_LONG)) {
        ret = ISP_Read(handle, (unsigned char*)&uID, 4, dwMilliseconds, FALSE);
    }
    if (ret) {
        handle->m_uCmdIndex = 3;
    }
    return ret;
}

unsigned char ISP_GetVersion(io_handle_t* handle)
{
    unsigned char ucVersion = 0;
    ISP_Write(handle, CMD_GET_VERSION, NULL, 0, USBCMD_TIMEOUT);
    ISP_Read(handle, (unsigned char*)&ucVersion, 1, USBCMD_TIMEOUT, TRUE);
    return ucVersion;
}

unsigned int ISP_GetDeviceID(io_handle_t* handle)
{
    unsigned int uID = 0;
    ISP_Write(handle, CMD_GET_DEVICEID, NULL, 0, USBCMD_TIMEOUT);
    ISP_Read(handle, (unsigned char*)&uID, 4, USBCMD_TIMEOUT, TRUE);
    return uID;
}

unsigned int ISP_Resend(io_handle_t* handle)
{
    unsigned int ret = FALSE;
    if (ISP_Write(handle, CMD_RESEND_PACKET, NULL, 0, USBCMD_TIMEOUT_LONG)) {
        ret = ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, FALSE);
    }
    return ret;
}

unsigned int ISP_EraseSPI(io_handle_t* handle, unsigned int offset,
                          unsigned int total_len)
{
    unsigned int os = offset;
    while (os < total_len) {
        ISP_Write(handle, CMD_ERASE_SPIFLASH, (unsigned char*)&os, 4,
                  USBCMD_TIMEOUT_LONG);
        if (ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, TRUE)) {
            os += 64 * 1024;
        } else {
            return FALSE;
        }
    }
    return TRUE;
}

unsigned int ISP_UpdateSPI(io_handle_t* handle, unsigned int start_addr,
                           unsigned int total_len, const char *buffer)
{
    unsigned long write_len = 0;
    unsigned char acBuffer[56];
    while (write_len < total_len) {
        unsigned int addr = start_addr + write_len;
        unsigned int len = (total_len - write_len);
        if (len > (sizeof(acBuffer) - 8)) {
            len = (sizeof(acBuffer) - 8);
        }
        memcpy(&acBuffer[0], &addr, 4);
        memcpy(&acBuffer[4], &len, 4);
        memcpy(&acBuffer[8], buffer + write_len, len);
        ISP_Write(handle, CMD_UPDATE_SPIFLASH, acBuffer, len + 8, USBCMD_TIMEOUT_LONG);
        if (ISP_Read(handle, NULL, 0, USBCMD_TIMEOUT_LONG, TRUE)) {
            write_len += len;
        } else {
            return FALSE;
        }
    }
    return TRUE;
}

unsigned int ISP_CAN_Write(io_handle_t* handle, unsigned int uCmd,
                           unsigned int uData, unsigned int dwMilliseconds = 20)
{
    unsigned int dwLength = 0;
    unsigned int bRet = FALSE;
    if (handle->dev_open == FALSE) {
        return FALSE;
    }
    memset(handle->ac_buffer, 0, sizeof(handle->ac_buffer));
    *((unsigned long*) & (handle->ac_buffer[3])) = uCmd;
    *((unsigned long*) & (handle->ac_buffer[7])) = uData;
    handle->m_uCmdIndex = uCmd;
    bRet = handle->m_dev_io.write(dwMilliseconds, handle->ac_buffer);
    if (bRet == FALSE) {
        handle->m_dev_io.close();
    }
    return bRet;
}

unsigned int ISP_CAN_Read(io_handle_t* handle,
                          unsigned int dwMilliseconds = 5000)
{
    unsigned long uCmd = 0;
    unsigned long uData = 0;
    unsigned int dwLength = 0;
    handle->bResendFlag = FALSE;
    if (handle->dev_open == FALSE) {
        return FALSE;
    }
    dwLength = handle->m_dev_io.read(dwMilliseconds, handle->ac_buffer);
    if (!dwLength) {
        return FALSE;
    }
    uCmd = *((unsigned long*) & (handle->ac_buffer[1]));
    uData = *((unsigned long*) & (handle->ac_buffer[5]));
    if (uCmd != handle->m_uCmdIndex) {
        return FALSE;
    } else {
        return TRUE;
    }
}

unsigned int ISP_CAN_GetDeviceID(io_handle_t* handle)
{
    unsigned int UID = 0;
    ISP_CAN_Write(handle, CAN_CMD_GET_DEVICEID, 0);
    int ret = ISP_CAN_Read(handle);
    if (ret) {
        UID = *((unsigned long*) & (handle->ac_buffer[5]));
    }
    return UID;
}

void ISP_CAN_ReadConfig(io_handle_t* handle, unsigned int config[],
                        bool offset)
{
    int offset_v = (offset) ? 0x0 : 0x0F000000;
    for (int i = 0; i < 14; i++) {
        if (ISP_CAN_Write(handle, CAN_CMD_READ_CONFIG, offset_v + 0x00300000 + 4 * i)) {
            if (ISP_CAN_Read(handle)) {
                config[i] = *((unsigned long*) & (handle->ac_buffer[5]));
            }
        }
    }
}

void ISP_CAN_UpdateConfig(io_handle_t* handle, unsigned int config[],
                          unsigned int response[], bool offset)
{
    int offset_v = (offset) ? 0x0 : 0x0F000000;
    for (int i = 0; i < 14; i++) {
        if (ISP_CAN_Write(handle, offset_v + 0x00300000 + 4 * i, config[i])) {
            if (ISP_CAN_Read(handle)) {
                response[i] = *((unsigned long*) & (handle->ac_buffer[5]));
            }
        }
    }
}

void ISP_CAN_ReadConfig_Ext(io_handle_t* handle, unsigned int config[],
                        bool offset, unsigned int i)
{
    int offset_v = (offset) ? 0x0 : 0x0F000000;
    unsigned int index = i;
    if (i >= 16 && i <= 18) {
        index += 16;  // CONFIG_16 at 0x0F300080 not 0x0F300040
    }
    if (ISP_CAN_Write(handle, CAN_CMD_READ_CONFIG, offset_v + 0x00300000 + 4 * index)) {
        if (ISP_CAN_Read(handle)) {
            config[i] = *((unsigned long*) & (handle->ac_buffer[5]));
        }
    }
}

void ISP_CAN_UpdateConfig_Ext(io_handle_t* handle, unsigned int config[],
                          unsigned int response[], bool offset, unsigned int i)
{
    int offset_v = (offset) ? 0x0 : 0x0F000000;
    unsigned int index = i;
    if (i >= 16 && i <= 18) {
        index += 16;  // CONFIG_16 at 0x0F300080 not 0x0F300040
    }
    
    if (ISP_CAN_Write(handle, offset_v + 0x00300000 + 4 * index, config[i])) {
        if (ISP_CAN_Read(handle)) {
            response[i] = *((unsigned long*) & (handle->ac_buffer[5]));
        }
    }

}

void ISP_CAN_UpdateAPROM(io_handle_t* handle, unsigned int start_addr,
                         unsigned int total_len, unsigned int cur_addr, unsigned char *buffer,
                         unsigned int *update_len)
{
    handle->bResendFlag = TRUE;
    unsigned int write_len = total_len - (cur_addr - start_addr);
    unsigned char acBuffer[56];
    if (write_len > 4) {
        write_len = 4;
    }
    if (write_len) {
        unsigned long data = 0;
        memcpy(&data, buffer, write_len);
        if (ISP_CAN_Write(handle, cur_addr, data)) {
            if (ISP_CAN_Read(handle)) {
                handle->bResendFlag = FALSE;
            }
        }
    }
    if (update_len != NULL) {
        *update_len = write_len;
    }
}

void ISP_CAN_UpdateDataFlash(io_handle_t* handle, unsigned int start_addr,
                             unsigned int total_len, unsigned int cur_addr, unsigned char *buffer,
                             unsigned int *update_len)
{
    ISP_CAN_UpdateAPROM(handle, start_addr, total_len, cur_addr, buffer,
                        update_len);
}

void ISP_CAN_UpdateAPROM_64(io_handle_t* handle, unsigned int start_addr,
                         unsigned int total_len, unsigned int cur_addr, unsigned char *buffer,
                         unsigned int *update_len)
{
    handle->bResendFlag = TRUE;
    unsigned int write_len = total_len - (cur_addr - start_addr);
    unsigned char acBuffer[56];
    if (write_len > 8) {
        write_len = 8;
    }
    if (write_len) {
        char ret_1 = 1, ret_2 = 1, ret_3 = 1;
        unsigned long data_1 = 0;
        unsigned long data_2 = 0;
        memcpy(&data_1, buffer, 4);
        memcpy(&data_2, buffer + 4, 4);
        if (ISP_CAN_Write(handle, cur_addr, data_1)) {
            if (ISP_CAN_Read(handle)) {
                ret_1 = 0;
            }
        }
        if (ISP_CAN_Write(handle, cur_addr + 4, data_2)) {
            if (ISP_CAN_Read(handle)) {
                ret_2 = 0;
            }
        }
        if (ISP_CAN_Write(handle, CAN_CMD_SECOND_READ, cur_addr + 4)) {
            if (ISP_CAN_Read(handle)) {
                ret_3 = 0;
            }
        }
        handle->bResendFlag = ret_1 | ret_2 | ret_3;
    }
    if (update_len != NULL) {
        *update_len = write_len;
    }
}

void ISP_CAN_UpdateDataFlash_64(io_handle_t* handle, unsigned int start_addr,
                             unsigned int total_len, unsigned int cur_addr, unsigned char *buffer,
                             unsigned int *update_len)
{
    ISP_CAN_UpdateAPROM_64(handle, start_addr, total_len, cur_addr, buffer,
                        update_len);
}

unsigned int ISP_CAN_Connect(io_handle_t* handle, unsigned int dwMilliseconds)
{
    unsigned int ret = FALSE;
    if (ISP_CAN_Write(handle, CAN_CMD_GET_DEVICEID, 0)) {
        ret = ISP_CAN_Read(handle);
    }
    return ret;
}

unsigned int ISP_CAN_RunAPROM(io_handle_t* handle)
{
    return ISP_CAN_Write(handle, CAN_CMD_RUN_APROM, 0);
}

unsigned int ISP_SendSingleCommand(io_handle_t* handle, unsigned int cmd)
{
    return ISP_Write(handle, cmd, NULL, 0, USBCMD_TIMEOUT_LONG);
}