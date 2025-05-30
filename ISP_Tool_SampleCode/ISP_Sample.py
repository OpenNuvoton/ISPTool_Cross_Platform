# This program is licensed under the LGPL (Lesser General Public License).
# It uses PySide6, which is distributed under the LGPL.
#
# You are free to use, modify, and distribute this program under the
# terms of the LGPL, as long as you comply with the requirements of
# the license, including making modifications publicly available if
# required by the LGPL.
#
# PySide6 is licensed under the LGPL, and this program adheres to
# the conditions and obligations of that license.

import ctypes
import os
import sys
import struct
import time
import traceback

from ctypes import c_ubyte, c_void_p, c_uint, c_ushort, CFUNCTYPE, POINTER, Structure, memmove, byref, pointer

import hid
import serial

from PySide6 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from configwindow import ConfigDialog

from config_selection import config_setting_str
from FlashInfo import GetStaticInfo
from serial_port import serial_ports
from PartNumID import PROJ_M460HD, PROJ_M460LD, PROJ_M2L31, PROJ_M55M1

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
        ("m_usCheckSum",c_ushort),
        ("m_uCmdIndex",c_uint),
        ("m_intf",c_uint),
        ("ac_buffer",c_ubyte * 65),
        # ("dev_io",POINTER(c_void_p)),
        ("m_dev_io",DEV_IO),
    ]

class USB_dev_io:

    dev = None

    def _init_(self):
        self.dev = None

    def USB_init(self):
        self.dev = hid.device()

    def USB_open(self):
        test = False
        if self.dev is None:
            self.dev = hid.device()

        try:
            self.dev.open(0x0416, 0x3F00)
            test = True
        except Exception:
            pass

        if not test:
            try:
                self.dev.open(0x0416, 0xA316)
                test = True
            except Exception:
                pass

        if not test:
            try:
                for device_info in hid.enumerate(0x0416, 0x5201):
                    if device_info['interface_number'] == 5:
                        self.dev.open_path(device_info['path'])
                        test = True
            except Exception:
                pass

        if not test:
            try:
                for device_info in hid.enumerate(0x0416, 0x5203):
                    if device_info['interface_number'] == 5:
                        self.dev.open_path(device_info['path'])
                        test = True
            except Exception:
                pass

        if not test:
            try:
                for device_info in hid.enumerate(0x0416, 0x2006):
                    if device_info['interface_number'] == 4:
                        self.dev.open_path(device_info['path'])
                        test = True
            except Exception:
                pass

        if not test:
            try:
                #self.dev.open(0x0416, 0x2006)
                for device_info in hid.enumerate(0x0416, 0x2009):
                    if device_info['interface_number'] == 4:
                        self.dev.open_path(device_info['path'])
                        test = True
            except Exception:
                pass

        if not test:
            try:
                self.dev.open(0x0416, 0x3F10)
                test = True
            except Exception:
                pass

        if not test:
            print('USB no get')
        else:
            print ('USB get')
        return test

    def USB_close(self):
        try:
            if self.dev is not None:
                self.dev.close()
            self.dev = None
            print('USB Close')

        except Exception as e:
            print(f"Exception occurred: {e}")
            traceback.print_exc()

    def USB_write(self, Ctime, buffer):
        try:
            data = (c_ubyte * 65).from_address(ctypes.addressof(buffer.contents))
            bytes_data = bytearray(data)
            print(bytes_data)
            bytes_written = self.dev.write(bytes_data)
            if bytes_written >= len(bytes_data):
                return 1
            return 0

        except Exception as e:
            print(f"Exception occurred: {e}")
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
            traceback.print_exc()
            return 0

class UART_dev_io:

    dev = None
    COM_PORT = "COM1"

    def _init_(self):
        self.dev = None

    def UART_init(self):
        self.dev = None

    def UART_open(self):
        try:
            if self.dev is not None:
                self.dev.close()

            self.dev = serial.Serial(self.COM_PORT, 115200, timeout = 2)

            if self.dev.isOpen() is False:
                self.dev.open()

            return self.dev.isOpen()

        except Exception as e:
            print(f"Exception occurred: {e}")
            traceback.print_exc()
            return False

    def UART_close(self):
        try:
            if self.dev is not None:
                self.dev.close()

            self.dev = None
            print('UART Close')

        except Exception as e:
            print(f"Exception occurred: {e}")
            traceback.print_exc()

    def UART_write(self, Ctime, buffer):
        try:
            data = (c_ubyte * 65).from_address(ctypes.addressof(buffer.contents))
            bytes_data = bytearray(data[1:])
            test = self.dev.write(bytes_data)
            #print(test, bytes_data)
            if test == len(bytes_data):
                return 1
            return 0

        except Exception as e:
            print(f"Exception occurred: {e}")
            traceback.print_exc()
            return 0

    def UART_read(self, Ctime, buffer):
        try:
            return_str = self.dev.read(64)
            buffer_as_bytes = (c_ubyte * (len(return_str)+1))()

            if len(return_str) != 0:
                buffer_as_bytes[1:] = return_str

            memmove(buffer, buffer_as_bytes, len(buffer_as_bytes))
            if len(return_str) >= 4:
                return len(return_str)
            return 0

        except Exception as e:
            print(f"Exception occurred: {e}")
            traceback.print_exc()
            return 0

class Main_Ui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self) # Call the inherited classes __init__ method

        self.setupUi(self)
        self.setWindowTitle("Nuvoton ISP Tool")

        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.connect_flag = False

        self.btn_APROM.clicked.connect(self.iniBrowseAPROM)
        self.btn_DataFlash.clicked.connect(self.iniBrowseDataFlash)

        self.io_handle_t = io_handle_t()
        self.io_handle_t.dev_open = False
        self.io_handle_t.bResendFlag = False
        self.io_handle_t.m_uCmdIndex = 1
        self.io_handle_t.m_intf = 1
        self.io_handle_t.m_usCheckSum = 0
        self.io_handle_t.ac_buffer = (c_ubyte*65)()

        self.DEV_IO = DEV_IO()

        #USB Version
        self.USB_dev_io = USB_dev_io()
        self.UART_dev_io = UART_dev_io()

        if os.name == 'nt':  # Windows
            self.lib = ctypes.cdll.LoadLibrary('./ISPLib.dll')
            #self.lib = ctypes.cdll.LoadLibrary('./ISPLib_debug.dll')
        elif os.name == 'posix':  # Linux/Unix/MacOS
            self.lib = ctypes.cdll.LoadLibrary('./ISPLib.so')

        self.config = (c_uint * 14)(0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                    0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                    0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF)
        self.wconfig = (c_uint * 14)(0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                     0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                     0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF)

        self.m_ulDeviceID = 0x0
        self.chip_type = 0x0
        self.memory_size = 0
        self.aprom_size = 0
        self.nvm_size = 0
        self.page_size = 0

        self.configwindow = None

        self.label_DeviceID.setText("Device ID:" + "0xFFFFFFFF")
        self.label_Size.setText("")
        self.label_DeviceID_2.setText("")
        self.label_Size_2.setText("")

        self.btn_Connect.clicked.connect(self.Ui_open)
        self.btn_Write.clicked.connect(self.Ui_write)
        self.btn_Erase.clicked.connect(self.Ui_erase)
        self.btn_Config.clicked.connect(self.configshow)

        self.comboBox_port.setEnabled(False)
        self.comboBox_interface.currentTextChanged.connect(self.comboBox_changed)

    def comboBox_changed(self):
        self.comboBox_port.clear()
        if self.comboBox_interface.currentIndex()== 1:
            self.comboBox_port.setEnabled(True)
            port_list = serial_ports()
            self.comboBox_port.addItems(port_list)
        else:
            self.comboBox_port.setEnabled(False)

    def DEV_IO_setting(self):
        if self.io_handle_t.m_intf != 2:
            self.DEV_IO.init = VOIDFUNCTYPE(self.USB_dev_io.USB_init)
            self.DEV_IO.open = UINTFUNCTYPE(self.USB_dev_io.USB_open)
            self.DEV_IO.close = VOIDFUNCTYPE(self.USB_dev_io.USB_close)
            self.DEV_IO.read = RWFUNCTYPE(self.USB_dev_io.USB_read)
            self.DEV_IO.write = RWFUNCTYPE(self.USB_dev_io.USB_write)
        else:
            self.DEV_IO.init = VOIDFUNCTYPE(self.UART_dev_io.UART_init)
            self.DEV_IO.open = UINTFUNCTYPE(self.UART_dev_io.UART_open)
            self.DEV_IO.close = VOIDFUNCTYPE(self.UART_dev_io.UART_close)
            self.DEV_IO.read = RWFUNCTYPE(self.UART_dev_io.UART_read)
            self.DEV_IO.write = RWFUNCTYPE(self.UART_dev_io.UART_write)

        self.io_handle_t.m_dev_io = self.DEV_IO

    def Ui_open(self):
        prev = self.connect_flag
        self.io_handle_t.m_intf = self.comboBox_interface.currentIndex() + 1
        if self.io_handle_t.m_intf == 2:
            self.UART_dev_io.COM_PORT = str(self.comboBox_port.currentText())

        self.DEV_IO_setting()

        self.lib.ISP_Open.argtypes = [POINTER(io_handle_t)]
        self.lib.ISP_Open.restype = c_uint

        ct = False
        reply = None

        if not self.connect_flag:
            ct = self.lib.ISP_Open(byref(self.io_handle_t))
            self.connect_flag = ct != 0
            if self.connect_flag is False:
                reply = QtWidgets.QMessageBox.warning(None, 'message box', 'Connect Fail')
        else:
            self.connect_flag = False
            self.label_DeviceID.setText("Device ID:" + "0xFFFFFFFF")
            self.label_Size.setText("")
            self.label_DeviceID_2.setText("")
            self.label_Size_2.setText("")

        if self.connect_flag is False:
            self.lib.ISP_Close(byref(self.io_handle_t))
            self.label_Connection.setText("Status: Disconnected")
            self.comboBox_interface.setEnabled(True)
            self.btn_Connect.setText("Connect")
        else:
            ct = self.attempt_connection()

        if (not ct and not prev):
            self.update_disconnected_status()

    def attempt_connection(self):
        if self.io_handle_t.m_intf == 6:
            attempt = 0
            for attempt in range(0, 50):
                if self.lib.ISP_CAN_Connect(byref(self.io_handle_t), 4000):
                    self.m_ulDeviceID = self.lib.ISP_CAN_GetDeviceID(byref(self.io_handle_t))
                    self.update_flash()  # to get chip_type only
                    config_offset = {PROJ_M460HD, PROJ_M460LD, PROJ_M2L31, PROJ_M55M1}
                    offset = self.chip_type in config_offset
                    self.lib.ISP_CAN_ReadConfig(byref(self.io_handle_t), byref(self.config), offset)
                    self.update_flash()  # regular update flash
                    self.label_Connection.setText("Status: Connected")
                    self.btn_Connect.setText("Disconnect")
                    self.comboBox_interface.setEnabled(False)
                    return True
        else:
            if self.io_handle_t.m_intf == 2:
                self.UART_dev_io.dev.timeout = 0.04
            for attempt in range(0, 250):
                self.io_handle_t.m_uCmdIndex = 1
                if self.lib.ISP_Connect(byref(self.io_handle_t), 40):
                    if self.io_handle_t.m_intf == 2:
                        self.UART_dev_io.dev.timeout = 2
                    self.lib.ISP_SyncPackNo(byref(self.io_handle_t))
                    self.m_ucFW_VER = self.lib.ISP_GetVersion(byref(self.io_handle_t))
                    self.m_ulDeviceID = self.lib.ISP_GetDeviceID(byref(self.io_handle_t))
                    self.lib.ISP_ReadConfig(byref(self.io_handle_t), byref(self.config))
                    self.update_flash()
                    self.label_Connection.setText("Status: Connected")
                    self.btn_Connect.setText("Disconnect")
                    self.comboBox_interface.setEnabled(False)
                    return True
        return False

    def update_disconnected_status(self):
        self.lib.ISP_Close.argtypes = [POINTER(io_handle_t)]
        self.lib.ISP_Close.restype = None

        self.lib.ISP_Close(byref(self.io_handle_t))
        reply = QtWidgets.QMessageBox.warning(None, 'message box', 'Connect Fail')
        self.connect_flag = False

    def update_flash(self):
        c_name, c_type, apr_sz, nvm_sz, nvm_addr, p_size = GetStaticInfo(self.m_ulDeviceID, self.config)
        self.label_DeviceID.setText("Device ID: " + hex(self.m_ulDeviceID))
        self.label_DeviceID_2.setText("Device Name: " + c_name)
        self.chip_type = c_type
        self.memory_size = apr_sz + nvm_sz
        self.page_size = p_size
        self.label_Size.setText("APROM Size: "+ str(int(apr_sz/1024)) + "KB")
        self.label_Size_2.setText("Data Flash Size: "+ str(int(nvm_sz/1024)) + "KB")
        self.aprom_size = apr_sz
        self.nvm_size = nvm_sz

    def Ui_write(self):
        if self.connect_flag is True:
            self.update_flash()
            reply = None
            if self.radioButton_APROM.isChecked():
                b_second = time.time()
                self.APROM_file = []
                self.read_APROM()
                lenAPROM =len(self.APROM_file)
                print(lenAPROM, self.aprom_size)
                if lenAPROM > self.aprom_size:
                    reply = QtWidgets.QMessageBox.warning(None, 'message box', 'APROM size over')
                    return
                self.lib.ISP_SyncPackNo(byref(self.io_handle_t))
                i = 0
                staddr = 0
                update_len = c_uint()
                retry_coda = 10
                self.APROM_file_ctypes = (ctypes.c_ubyte * lenAPROM)(*self.APROM_file)
                array_pointer = ctypes.pointer(self.APROM_file_ctypes)

                while i < self.APROM_size:
                    update_len = c_uint(0)
                    buf = ctypes.cast(ctypes.addressof(array_pointer.contents) + i, POINTER(c_ubyte))
                    if self.io_handle_t.m_intf != 6:
                        self.lib.ISP_UpdateAPROM(byref(self.io_handle_t), staddr, self.APROM_size, staddr + i, buf, byref(update_len))
                    else:
                        self.lib.ISP_CAN_UpdateAPROM(byref(self.io_handle_t), staddr, self.APROM_size, staddr + i, buf, byref(update_len))

                    if self.io_handle_t.bResendFlag is True:
                        retry_coda =  retry_coda - 1
                        if retry_coda == 0:
                            print("\n over \n")
                            return
                        print("\n over \n")
                        break
                    i = i + update_len.value
                    print(i, lenAPROM)
                    # percent = i / len(self.APROM_file)
                    self.progressBar.setValue( int(i * 100 / lenAPROM) )

                f_second = time.time()
                print("Update APROM finish: " + str(f_second - b_second) + " second cost.")
                reply = QtWidgets.QMessageBox.warning(None, 'message box', 'Update APROM finish')

            elif self.radioButton_DataFlash.isChecked():
                self.lib.ISP_ReadConfig(byref(self.io_handle_t), byref(self.config))
                self.DataFlash_file = []
                self.read_DataFlash()
                lenDataFlash =len(self.DataFlash_file)
                if lenDataFlash > self.nvm_size:
                    reply = QtWidgets.QMessageBox.warning(None, 'message box', 'Data flash size over')
                    return
                self.lib.ISP_SyncPackNo(byref(self.io_handle_t))
                i = 0
                staddr = self.config[1] & 0x00FFFFFF
                update_len = c_uint()
                retry_coda = 10
                self.DataFlash_file_ctypes = (ctypes.c_ubyte * lenDataFlash)(*self.DataFlash_file)
                array_pointer = ctypes.pointer(self.DataFlash_file_ctypes)
                while i < self.DataFlash_size:
                    update_len = c_uint(0)
                    buf = ctypes.cast(ctypes.addressof(array_pointer.contents) + i, POINTER(c_ubyte))
                    if self.io_handle_t.m_intf != 6:
                        self.lib.ISP_UpdateDataFlash(byref(self.io_handle_t), staddr, self.DataFlash_size, staddr + i, buf, byref(update_len))
                    else:
                        self.lib.ISP_CAN_UpdateDataFlash(byref(self.io_handle_t), staddr, self.DataFlash_size, staddr + i, buf, byref(update_len))
                    if self.io_handle_t.bResendFlag is True:
                        retry_coda =  retry_coda - 1
                        if retry_coda == 0:
                            return
                        break
                    i = i + update_len.value
                    # percent = i / lenDataFlash
                    self.progressBar.setValue( int(i * 100 / lenDataFlash) )
                reply = QtWidgets.QMessageBox.warning(None, 'message box', 'Update Data Flash finish')

            elif self.radioButton_Config.isChecked():
                if self.io_handle_t.m_intf != 6:
                    self.lib.ISP_UpdateConfig(pointer(self.io_handle_t), self.wconfig, self.config)
                    self.lib.ISP_ReadConfig(pointer(self.io_handle_t), self.config)
                else:
                    config_offset = {PROJ_M460HD, PROJ_M460LD, PROJ_M2L31, PROJ_M55M1}
                    offset = self.chip_type in config_offset
                    self.lib.ISP_CAN_UpdateConfig(pointer(self.io_handle_t), self.wconfig, self.config, offset)
                    self.lib.ISP_CAN_ReadConfig(pointer(self.io_handle_t), self.config, offset)

            if self.checkBox_jump.isChecked():
                self.lib.ISP_RunAPROM(pointer(self.io_handle_t))

        self.update_flash()

    def Ui_erase(self):
        reply = None
        if self.connect_flag is True:
            self.lib.ISP_EraseAll(pointer(self.io_handle_t))
            self.lib.ISP_ReadConfig(pointer(self.io_handle_t), self.config)

        self.update_flash()
        reply = QtWidgets.QMessageBox.warning(None, 'message box', 'Erase All finish')

    def iniBrowseAPROM(self):
        filename = ""
        # Fix for crash in X on Ubuntu 14.04
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter = "bin(*.bin)")
        if filename != "":
            self.lineEdit_APROM.setText(filename)

    def iniBrowseDataFlash(self):
        filename = ""
        # Fix for crash in X on Ubuntu 14.04
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(filter = "bin(*.bin)")
        if filename != "":
            self.lineEdit_DataFlash.setText(filename)

    def configshow(self):
        ctp = self.chip_type

        if config_setting_str(ctp) == "":
            import ui.config_type_0 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
        elif config_setting_str(ctp) == "M051D":
            import ui.config_type_M051D as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M051D_setup()
        elif config_setting_str(ctp) == "M058":
            import ui.config_type_M051D as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M058_setup()
        elif config_setting_str(ctp) == "M051A":
            import ui.config_type_M051 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M051A_setup()
        elif config_setting_str(ctp) == "M051B":
            import ui.config_type_M051 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M051B_setup()
        elif config_setting_str(ctp) == "M251":
            import ui.config_type_M251 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M251_setup()
        elif config_setting_str(ctp) == "M258":
            import ui.config_type_M251 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M258_setup()
        elif config_setting_str(ctp) == "NUC100":
            import ui.config_type_NUC100 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NUC100_setup()
        elif config_setting_str(ctp) == "NUC122":
            import ui.config_type_NUC100 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NUC122_setup()
        elif config_setting_str(ctp) == "NUC123AN":
            import ui.config_type_NUC200 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NUC123AN_setup()
        elif config_setting_str(ctp) == "NUC123AE":
            import ui.config_type_NUC200 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NUC123AE_setup()
        elif config_setting_str(ctp) == "NUC200":
            import ui.config_type_NUC200 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NUC200_setup()
        elif config_setting_str(ctp) == "M0564":
            import ui.config_type_NUC200 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M0564_setup()
        elif config_setting_str(ctp) == "NUC1262":
            import ui.config_type_NUC200 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NUC1262_setup()
        elif config_setting_str(ctp) == "MINI51":
            import ui.config_type_MINI51 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_MINI51_setup()
        elif config_setting_str(ctp) == "MINI51CN":
            import ui.config_type_MINI51CN as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_MINI51CN_setup()
        elif config_setting_str(ctp) == "NANO100":
            import ui.config_type_NANO100 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NANO100_setup()
        elif config_setting_str(ctp) == "NANO112":
            import ui.config_type_NANO100 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NANO112_setup()
        elif config_setting_str(ctp) == "NANO103":
            import ui.config_type_NANO103 as UI
            self.configwindow.config_type_NANO103_setup()
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
        elif config_setting_str(ctp) == "MINI55":
            import ui.config_type_MINI55 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_MINI55_setup()
        elif config_setting_str(ctp) == "NM1120":
            import ui.config_type_NM1120 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NM1120_setup()
        elif config_setting_str(ctp) == "NM1500":
            import ui.config_type_NM1500 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NM1500_setup()
        elif config_setting_str(ctp) == "NUC400":
            import ui.config_type_NUC400 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_NUC400_setup()
        elif config_setting_str(ctp) == "M451":
            import ui.config_type_M451 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M451_setup()
        elif config_setting_str(ctp) == "M031":
            import ui.config_type_M031 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M031_setup()
        elif config_setting_str(ctp) == "M030G":
            import ui.config_type_M031 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M030G_setup()
        elif config_setting_str(ctp) == "M0A21":
            import ui.config_type_M0A21 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M0A21_setup()
        elif config_setting_str(ctp) == "M480":
            import ui.config_type_M480 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M480_setup()
        elif config_setting_str(ctp) == "M480LD":
            import ui.config_type_M480LD as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M480LD_setup()
        elif config_setting_str(ctp) == "M460":
            import ui.config_type_M460 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M460_setup()
        elif config_setting_str(ctp) == "M2351":
            import ui.config_type_M2351 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M2351_setup()
        elif config_setting_str(ctp) == "M2354":
            import ui.config_type_M2351 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M2354_setup()
        elif config_setting_str(ctp) == "M471":
            import ui.config_type_M471 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M471_setup()
        elif config_setting_str(ctp) == "M2L31":
            import ui.config_type_M2L31 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M2L31_setup()
        elif config_setting_str(ctp) == "M2003":
            import ui.config_type_M2003 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M2003_setup()
        elif config_setting_str(ctp) == "M55M1":
            import ui.config_type_M55M1 as UI
            self.configwindow = ConfigDialog(parent = self, ui = UI.Ui_Dialog())
            self.configwindow.config_type_M55M1_setup()

        self.configwindow.show()

    def read_APROM(self):
        filename = self.lineEdit_APROM.text()
        with open(filename, 'rb') as f:
            self.APROM_Checksum = 0
            while True:
                x=f.read(1)
                if not x:
                    break
                temp=struct.unpack('B',x)
                self.APROM_file.append(temp[0])
                self.APROM_Checksum=self.APROM_Checksum + temp[0]
        self.APROM_size = len(self.APROM_file)

    def read_DataFlash(self):
        filename = self.lineEdit_DataFlash.text()
        with open(filename, 'rb') as f:
            self.DataFlash_Checksum = 0
            while True:
                x=f.read(1)
                if not x:
                    break
                temp=struct.unpack('B',x)
                self.DataFlash_file.append(temp[0])
                self.DataFlash_Checksum=self.DataFlash_Checksum + temp[0]
        self.DataFlash_size = len(self.DataFlash_file)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # tool icon
    app.setWindowIcon(QtGui.QIcon('./image/NuTool.ico'))
    myapp = Main_Ui()
    myapp.show()
    sys.exit(app.exec_())
