import os
import sys
import argparse
import serial
import struct
import hid
import ctypes

from ctypes import *
from FlashInfo import *

VOIDFUNCTYPE = CFUNCTYPE(c_void_p)
UINTFUNCTYPE = CFUNCTYPE(c_uint)
RWFUNCTYPE = CFUNCTYPE(c_uint, c_uint, POINTER(c_ubyte))

class DEV_IO(Structure):
    _fields_ = [
        ("init",CFUNCTYPE(c_void_p)),                           # be called at init state
        ("open",CFUNCTYPE(c_uint)),                             # return True or False
        ("close",CFUNCTYPE(c_void_p)),                          # no return 
        ("write",CFUNCTYPE(c_uint, c_uint, POINTER(c_ubyte))),  # return 1 when success, 0 when fail
        ("read",CFUNCTYPE(c_uint, c_uint, POINTER(c_ubyte))),   # return read value length
    ]
                
class io_handle_t(Structure):
    _fields_ = [
        ("dev_open", c_uint),
        ("bResendFlag", c_uint),
        ("m_usCheckSum",c_ubyte),
        ("m_uCmdIndex",c_uint),
        ("ac_buffer",c_ubyte * 65),
        ("dev_io",POINTER(c_void_p)),
        ("m_dev_io",DEV_IO),
    ]

class USB_dev_io:

    dev = None
    interface_num = 0
    
    def _init_(self):
        self.dev = None
        self.interface_num = 0
    
    def USB_init(self):
        self.dev = hid.device()
    
    def USB_open(self):
        test = 0;
        if self.dev == None:
            self.dev = hid.device()
            
        try:
            self.dev.open(0x0416, 0x3F00)
        except Exception as e:
            test = 1
            
        if (test > 0):
            try:
                self.dev.open(0x0416, 0xA316)
            except Exception as e:
                test = 2
        
        if (test > 1):
            try:
                self.dev.open(0x0416, 0x5201)
            except Exception as e:
                test = 3
                
        if (test > 2):
            try:
                self.dev.open(0x0416, 0x5203)
            except Exception as e:
                test = 4
                
        if (test > 3):
            try:
                self.dev.open(0x0416, 0x2006)
            except Exception as e:
                test = 5
                
        if (test > 4):
            try:
                self.dev.open(0x0416, 0x3F10)
            except Exception as e:
                test = 6
            
        if (test > 5):
            print('USB no get')
            return False
        else: 
            print ('USB get')
            return True
    
    def USB_close(self):
        try:
            if self.dev != None:
                self.dev.close()
            self.dev = None
            print('USB Close')
            
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
            
    def USB_write(self, Ctime, buffer):
        try:
            data = (c_ubyte * 65).from_address(ctypes.addressof(buffer.contents))
            bytes_data = bytearray(data)
            
            if (self.interface_num != 0):
                bytes_data[2] = (self.interface_num + 1)
            
            #self.dev.set_nonblocking(1)
            bytes_written = self.dev.write(bytes_data)
            if bytes_written >= len(bytes_data):
                return 1
            else:
                return 0
                
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
            return 0
        
    def USB_read(self, Ctime, buffer):
        
        try:
            return_str = self.dev.read(65, 2000) #return by string
            
            buffer_as_bytes = (c_ubyte * (len(return_str)+1))()
            buffer_as_bytes[1:] = return_str
            memmove(buffer, buffer_as_bytes, len(buffer_as_bytes))
            
            return len(buffer_as_bytes) - 1
            
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
            return 0

class UART_dev_io:

    dev = None
    interface_num = 1
    COM_PORT = "COM1"
    
    def _init_(self):
        self.dev = None
        self.interface_num = 1
        
    def UART_init(self):
        self.dev = None
    
    def UART_open(self):
        try: 
            if self.dev != None:
                self.dev.close()
                
            self.dev = serial.Serial(self.COM_PORT, 115200, timeout = 3) 
            
            if(self.dev.isOpen() == False):
                self.dev.open()
                
            return self.dev.isOpen()
            
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def UART_close(self):
        try:
            if self.dev != None:
                self.dev.close()
                
            self.dev = None
            print('UART Close')
            
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
    
    def UART_write(self, Ctime, buffer):
        try:
            data = (c_ubyte * 65).from_address(ctypes.addressof(buffer.contents))
            bytes_data = bytearray(data[1:])
            test = self.dev.write(bytes_data)
            if test == len(bytes_data):
                return 1
            else:
                return 0
                
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
            return 0

    def UART_read(self, Ctime, buffer):
        try:
            return_str = self.dev.read(64)
            buffer_as_bytes = (c_ubyte * (len(return_str)+1))()
            
            if (len(return_str) != 0):
                buffer_as_bytes[1:] = return_str
            
            memmove(buffer, buffer_as_bytes, len(buffer_as_bytes))  
            
            if len(return_str) >= 4:
                return len(return_str)
            else:
                return 0
        
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
            return 0

def get_option(option) -> int:
    option = str.upper(option)
    return {
        'USB': 0,
        'UART': 1,
        'SPI': 2,
        'I2C': 3,
        'RS485': 4,
        'CAN': 5,
    }.get(option, 0)

def main():

    m_io_handle_t = io_handle_t()
    m_io_handle_t.dev_open = False;
    m_io_handle_t.bResendFlag = False;
    m_io_handle_t.m_uCmdIndex = 1;
    m_io_handle_t.m_usCheckSum = 0;
    m_io_handle_t.ac_buffer = (c_ubyte*65)()

    m_DEV_IO = DEV_IO()
    
    #USB Version
    m_USB_dev_io = USB_dev_io()
    m_UART_dev_io = UART_dev_io()
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--option", nargs='+', help="Option flag")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--aprom", nargs='+', help="Update APROM")
    group.add_argument("-d", "--dataflash", nargs='+', help="Update Data Flash")
    group.add_argument("-c", "--config", nargs='+', help="Update Config Value")
    group.add_argument("-e", "--erase", action='store_true', help="Erase All")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
        
    args = parser.parse_args()
    
    if args.option:
        option = get_option(args.option[0])
        #print(option)
    else:
        option = 0
        
    # do open & connect
    if (option != 1):
        m_DEV_IO.init = VOIDFUNCTYPE(m_USB_dev_io.USB_init)
        m_DEV_IO.open = UINTFUNCTYPE(m_USB_dev_io.USB_open)
        m_DEV_IO.close = VOIDFUNCTYPE(m_USB_dev_io.USB_close)
        m_DEV_IO.read = RWFUNCTYPE(m_USB_dev_io.USB_read)
        m_DEV_IO.write = RWFUNCTYPE(m_USB_dev_io.USB_write)
        if (option != 0):
            m_USB_dev_io.interface_num = option
    else:
        m_DEV_IO.init = VOIDFUNCTYPE(m_UART_dev_io.UART_init)
        m_DEV_IO.open = UINTFUNCTYPE(m_UART_dev_io.UART_open)
        m_DEV_IO.close = VOIDFUNCTYPE(m_UART_dev_io.UART_close)
        m_DEV_IO.read = RWFUNCTYPE(m_UART_dev_io.UART_read)
        m_DEV_IO.write = RWFUNCTYPE(m_UART_dev_io.UART_write)
        m_UART_dev_io.COM_PORT = args.option[1]
        
    if os.name == 'nt':  # Windows
        m_lib = ctypes.cdll.LoadLibrary('./ISPLib.dll')
    elif os.name == 'posix':  # Linux/Unix/MacOS
        m_lib = ctypes.cdll.LoadLibrary('./ISPLib.so')  
        
    m_io_handle_t.m_dev_io = m_DEV_IO
        
    m_lib.ISP_Open.argtypes = [POINTER(io_handle_t)]
    m_lib.ISP_Open.restype = c_uint
    m_lib.ISP_Close.argtypes = [POINTER(io_handle_t)]
    m_lib.ISP_Close.restype = None

    ct = m_lib.ISP_Open(byref(m_io_handle_t))
    if (ct != 0):
        t = 0
        r = 0
        while (t < 50):
            t = t + 1
            m_lib.ISP_SyncPackNo(byref(m_io_handle_t))
            r = m_lib.ISP_Connect(byref(m_io_handle_t), 50000)
            if (r > 0):
                break
            print("ISP Connect Retry!")
         
        if (r):
            m_lib.ISP_SyncPackNo(byref(m_io_handle_t))
            print("ISP Connect Success!")
        else:
            print("ISP Connect Fail!")
            return
    else:
        print("ISP Open Fail!")
        return

    m_ucFW_VER = 0x0
    m_ucFW_VER = m_lib.ISP_GetVersion(byref(m_io_handle_t))
    
    m_ulDeviceID = 0xFFFFFFFF
    m_ulDeviceID = m_lib.ISP_GetDeviceID(byref(m_io_handle_t))
    m_config = (c_uint * 12)(0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                             0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF)
    m_lib.ISP_ReadConfig(byref(m_io_handle_t), byref(m_config))
    chip_name, chip_type, aprom_size, nvm_size, nvm_addr, page_size = GetStaticInfo(m_ulDeviceID, m_config)
    
    print("Target ISP Firmware Version: " + hex(m_ucFW_VER) + "\n")
    print("Target Device ID: " + hex(m_ulDeviceID) + "\n")
    print("Target Device: " + chip_name + "\n")
    print("Target APROM size: " + str(int(aprom_size/1024)) + "KB\n")
    print("Target Data Flash Size: " + str(int(nvm_size/1024)) + "KB\n")
    print("Target Config[0]: " + hex(m_config[0]) + "\n")
    print("Target Config[1]: " + hex(m_config[1]) + "\n")
    print("Target Config[2]: " + hex(m_config[2]) + "\n")
    print("Target Config[3]: " + hex(m_config[3]) + "\n")
    
    if args.aprom:
        arg_count = len(args.aprom)
        if arg_count != 1:
            print("No Writing File!")
            return
        APROM_file = []
        filename = args.aprom[0]
        f = open(filename, 'rb')            
        m_APROM_Checksum = 0
        while True:
            x=f.read(1)
            if not x:
                break
            temp=struct.unpack('B',x) 
            APROM_file.append(temp[0])
            m_APROM_Checksum = m_APROM_Checksum + temp[0]
        f.close()
        lenAPROM =len(APROM_file)
        if (lenAPROM > aprom_size):
            print("APROM size over!")
            return
        m_lib.ISP_SyncPackNo(byref(m_io_handle_t))
        i = 0
        start_addr = 0
        update_len = c_uint()
        retry_coda = 10
        APROM_file_ctypes = (ctypes.c_ubyte * lenAPROM)(*APROM_file)
        array_pointer = ctypes.pointer(APROM_file_ctypes)
        
        while (i < lenAPROM):
            update_len = c_uint(0)
            buffer = ctypes.cast(ctypes.addressof(array_pointer.contents) + i, POINTER(c_ubyte))
            m_lib.ISP_UpdateAPROM(byref(m_io_handle_t), start_addr, lenAPROM, start_addr + i, buffer, byref(update_len))
            if (m_io_handle_t.bResendFlag == True):
                retry_coda =  retry_coda - 1
                if (retry_coda == 0): 
                    print("Resend Limit Over! \n")
                    return
            i = i + update_len.value
        print("Update APROM finish \n")
       
    elif args.dataflash:
        arg_count = len(args.dataflash)
        if arg_count != 1:
            print("No Writing File!")
            return
        DataFlash_file = []
        filename = args.dataflash[0]
        f = open(filename, 'rb')            
        m_DataFlash_Checksum = 0
        while True:
            x=f.read(1)
            if not x:
                break
            temp=struct.unpack('B',x) 
            DataFlash_file.append(temp[0])
            m_DataFlash_Checksum = m_DataFlash_Checksum + temp[0]
        f.close()
        lenDataFlash =len(DataFlash_file)
        if (lenDataFlash > nvm_size):
            print("Data Flash size over!")
            return
        m_lib.ISP_SyncPackNo(byref(m_io_handle_t))
        i = 0
        start_addr = 0
        update_len = c_uint()
        retry_coda = 10
        DataFlash_file_ctypes = (ctypes.c_ubyte * lenDataFlash)(*DataFlash_file)
        array_pointer = ctypes.pointer(DataFlash_file_ctypes)
        
        while (i < lenDataFlash):
            update_len = c_uint(0)
            buffer = ctypes.cast(ctypes.addressof(array_pointer.contents) + i, POINTER(c_ubyte))
            m_lib.ISP_UpdateDataFlash(byref(m_io_handle_t), start_addr, lenDataFlash, start_addr + i, buffer, byref(update_len))
            if (m_io_handle_t.bResendFlag == True):
                retry_coda =  retry_coda - 1
                if (retry_coda == 0): 
                    print("Resend Limit Over! \n")
                    return
            i = i + update_len.value
        print("Update Data Flash finish \n")
    
    elif args.config:
        arg_count = len(args.config)
        m_wconfig = (c_uint * 12)(0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                  0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF)
        if arg_count < 1:
            print("No Writing Config!")
            return
        elif arg_count < 13:
            for i in range(arg_count):
                m_wconfig[i] = int(args.config[i], 0)
                
        m_lib.ISP_UpdateConfig(pointer(m_io_handle_t), m_wconfig, m_config)
        m_lib.ISP_ReadConfig(pointer(m_io_handle_t), m_config)
        print("Update Config finish \n")
    
    elif args.erase:
        m_lib.ISP_EraseAll(pointer(m_io_handle_t))
        print("Erase Flash finish \n")
            
    m_lib.ISP_Close(byref(m_io_handle_t))

if __name__ == "__main__":
    main()