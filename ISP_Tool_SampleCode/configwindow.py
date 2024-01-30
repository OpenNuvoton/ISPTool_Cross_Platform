
#!/usr/bin/env python
from ctypes import *
import json
import os

from PyQt5.QtCore import QDateTime, QPointF, QRegExp, Qt, QTimer
from PyQt5.QtGui import QColor, QIntValidator, QRegExpValidator, QValidator
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QFileDialog, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, 
        QLineEdit, QMessageBox, QPlainTextEdit, QProgressBar, QPushButton, QRadioButton, QScrollBar, 
        QSizePolicy, QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from PartNumID import *
from config_selection import *

class ConfigDialog(QDialog):
    def __init__(self, parent=None, ui = None):
        super(ConfigDialog, self).__init__(parent)
        
        self.parent = parent
        self.ui = ui
        self.ui.setupUi(self)
        self.setWindowTitle("Config Setting")
        self.wconfig = (c_uint * 14)(0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                     0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                     0xFFFFFFFF,0xFFFFFFFF)
        for i in range(0, 14):
            self.wconfig[i] = self.parent.wconfig[i]
        
        self.size = float(self.parent.memory_size / 1024)
        self.page_size = float(self.parent.page_size / 1024)
        print(self.size, self.page_size)
        
        self.ui.pushButton_OK.clicked.connect(self.exportFile)
        self.ui.pushButton_Cancel.clicked.connect(self.close)
        self.valid_setting()
        self.get_config()
    
    # use to import exist json to window
    def get_config(self):
        for i in range(0, 14):
            self.wconfig[i] = self.parent.config[i] if (self.parent.connect_flag == True) else self.parent.wconfig[i]
            
        for i in range(0, 14):
            line_edit_name = f'lineEdit_config{i}'
            print(line_edit_name)
            if hasattr(self.ui, line_edit_name):
                line_edit = getattr(self.ui, line_edit_name)
                line_edit.setText(f'{self.wconfig[i]:08X}')
                print(line_edit.text())

        if hasattr(self.ui, 'gridGroupBox_boot'):
            self.ui.gridGroupBox_boot.setEnabled(False)
            
    def updateValue(self, value, cfg_num):
        self.wconfig[cfg_num] = value
        cfg_text = self.wconfig[cfg_num]
        line_edit_name = f'lineEdit_config{cfg_num}'
        if hasattr(self.ui, line_edit_name):
            line_edit = getattr(self.ui, line_edit_name)
            line_edit.setText(f'{cfg_text:08X}')
    
    def updateBits(self, lsb, val, bits = 1, cfg_num = 0):
        _mask = (1 << bits) - 1 
        self.wconfig[cfg_num] &= ~(_mask << lsb)
        self.wconfig[cfg_num] |= ((val &_mask) << lsb)
        cfg_text = self.wconfig[cfg_num]
        line_edit_name = f'lineEdit_config{cfg_num}'
        if hasattr(self.ui, line_edit_name):
            line_edit = getattr(self.ui, line_edit_name)
            line_edit.setText(f'{cfg_text:08X}')
            
    def checkBit(self, state, lsb, cfg_num):
        val = 1 if state else 0
        self.updateBits(lsb, val, bits = 1, cfg_num = cfg_num)
        
    def checkBitTwo(self, state, lsb, cfg_num):
        val = 3 if state else 0
        self.updateBits(lsb, val, bits = 2, cfg_num = cfg_num)
        
    def getBits(self, lsb, val, bits = 1, cfg_num = 0):
        _mask = (1 << bits) - 1
        value = self.wconfig[cfg_num] & (_mask << lsb)
        return value >> lsb == val
        
    def radioButton_bw_template_4(self, place):
        self.ui.radioButton_bw_v_0.clicked.connect(lambda: self.updateBits(place, 3, 2, 0))
        self.ui.radioButton_bw_v_1.clicked.connect(lambda: self.updateBits(place, 2, 2, 0))
        self.ui.radioButton_bw_v_2.clicked.connect(lambda: self.updateBits(place, 1, 2, 0))
        self.ui.radioButton_bw_v_3.clicked.connect(lambda: self.updateBits(place, 0, 2, 0))
        self.ui.radioButton_bw_v_0.setChecked(self.getBits(place, 3, 2, 0))
        self.ui.radioButton_bw_v_1.setChecked(self.getBits(place, 2, 2, 0)) 
        self.ui.radioButton_bw_v_2.setChecked(self.getBits(place, 1, 2, 0))
        self.ui.radioButton_bw_v_3.setChecked(self.getBits(place, 0, 2, 0))
        
    def radioButton_bw_template_8(self, place):
        self.ui.radioButton_bw_v_0.clicked.connect(lambda: self.updateBits(place, 7, 3, 0))
        self.ui.radioButton_bw_v_1.clicked.connect(lambda: self.updateBits(place, 6, 3, 0))
        self.ui.radioButton_bw_v_2.clicked.connect(lambda: self.updateBits(place, 5, 3, 0))
        self.ui.radioButton_bw_v_3.clicked.connect(lambda: self.updateBits(place, 4, 3, 0))
        self.ui.radioButton_bw_v_4.clicked.connect(lambda: self.updateBits(place, 3, 3, 0))
        self.ui.radioButton_bw_v_5.clicked.connect(lambda: self.updateBits(place, 2, 3, 0))
        self.ui.radioButton_bw_v_6.clicked.connect(lambda: self.updateBits(place, 1, 3, 0))
        self.ui.radioButton_bw_v_7.clicked.connect(lambda: self.updateBits(place, 0, 3, 0))
        self.ui.radioButton_bw_v_0.setChecked(self.getBits(place, 7, 3, 0))
        self.ui.radioButton_bw_v_1.setChecked(self.getBits(place, 6, 3, 0))
        self.ui.radioButton_bw_v_2.setChecked(self.getBits(place, 5, 3, 0))
        self.ui.radioButton_bw_v_3.setChecked(self.getBits(place, 4, 3, 0))
        self.ui.radioButton_bw_v_4.setChecked(self.getBits(place, 3, 3, 0))
        self.ui.radioButton_bw_v_5.setChecked(self.getBits(place, 2, 3, 0))
        self.ui.radioButton_bw_v_6.setChecked(self.getBits(place, 1, 3, 0))
        self.ui.radioButton_bw_v_7.setChecked(self.getBits(place, 0, 3, 0))
        
    def checkBox_bw_0_template(self, place):
        self.ui.checkBox_bw_0.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_bw_0.isChecked(), place, 0))
        self.ui.checkBox_bw_0.setChecked(self.getBits(place, 0, 1, 0))
        
    def checkBox_bw_1_template(self, place):
        self.ui.checkBox_bw_1.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_bw_1.isChecked(), place, 0))
        self.ui.checkBox_bw_1.setChecked(self.getBits(place, 0, 1, 0))
        
    def doubleSpinBox_pagesize_template(self):
        self.ui.checkBox_dataflash.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_dataflash.isChecked(), 0, 0),
                                                                 self.ui.doubleSpinBox_pagesize.setEnabled(self.ui.checkBox_dataflash.isChecked()),
                                                                 self.updateValue((0xFFFFFFFF if not self.ui.checkBox_dataflash.isChecked() else int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value())) ), 1),
                                                                 self.ui.lineEdit_data_address.setText(f'{(0xFFFFFFFF if not self.ui.checkBox_dataflash.isChecked() else (int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value())))):08X}')))
        self.ui.doubleSpinBox_pagesize.setEnabled(self.ui.checkBox_dataflash.isChecked())
        self.ui.doubleSpinBox_pagesize.setSingleStep(self.page_size)
        self.ui.doubleSpinBox_pagesize.setRange(self.page_size, self.size - self.page_size)
        self.ui.doubleSpinBox_pagesize.valueChanged.connect(lambda: (self.updateValue(int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value())), 1),
                                                                     self.ui.lineEdit_data_address.setText(f'{(int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value()))):08X}')))
        self.ui.doubleSpinBox_pagesize.lineEdit().setReadOnly(True)
        self.ui.lineEdit_data_address.setReadOnly(True)
        self.ui.checkBox_dataflash.setChecked(self.getBits(0, 0, 1, 0))
        
    def secure_conceal_pagesize_template(self):
        self.ui.checkBox_dataflash.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_dataflash.isChecked(), 0, 0),
                                                                 self.ui.doubleSpinBox_pagesize.setEnabled(self.ui.checkBox_dataflash.isChecked()),
                                                                 self.updateValue((0xFFFFFFFF if not self.ui.checkBox_dataflash.isChecked() else int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value())) ), 1),
                                                                 self.ui.lineEdit_data_address.setText(f'{(0xFFFFFFFF if not self.ui.checkBox_dataflash.isChecked() else (int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value())))):08X}')))
        self.ui.doubleSpinBox_pagesize.setEnabled(self.ui.checkBox_dataflash.isChecked())
        self.ui.doubleSpinBox_pagesize.setSingleStep(self.page_size)
        self.ui.doubleSpinBox_pagesize.setRange(self.page_size, self.size - self.page_size)
        self.ui.doubleSpinBox_pagesize.valueChanged.connect(lambda: (self.updateValue(int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value())), 1),
                                                                     self.ui.lineEdit_data_address.setText(f'{(int(1024 * (self.size - self.ui.doubleSpinBox_pagesize.value()))):08X}')))
        self.ui.doubleSpinBox_pagesize.lineEdit().setReadOnly(True)
        self.ui.lineEdit_data_address.setReadOnly(True)
        self.ui.checkBox_dataflash.setChecked(self.getBits(0, 0, 1, 0))
        self.ui.checkBox_secure_conceal.stateChanged.connect(lambda: (self.ui.checkBox_dataflash.setEnabled(not self.ui.checkBox_secure_conceal.isChecked()),
                                                                 self.ui.checkBox_dataflash.setChecked(False if self.ui.checkBox_secure_conceal.isChecked() else self.ui.checkBox_dataflash.isChecked()),
                                                                 self.checkBit(1, 0, 0),
                                                                 self.ui.doubleSpinBox_pagesize.setEnabled(False),
                                                                 self.updateValue(0xFFFFFFFF, 1),
                                                                 self.ui.lineEdit_data_address.setText('0xFFFFFFFF'),
                                                                 self.updateValue((0x55AA5AA5 if self.ui.checkBox_secure_conceal.isChecked() else 0xFFFFFFFF), 6),
                                                                 self.ui.lineEdit_baddress.setText(f'{(int((self.size - self.page_size) * 1024) if self.ui.checkBox_secure_conceal.isChecked() else 0xFFFFFFFF):08X}'),
                                                                 self.ui.lineEdit_pcount.setText(f'{(1 if self.ui.checkBox_secure_conceal.isChecked() else 0)}'),
                                                                 self.ui.lineEdit_baddress.setEnabled(self.ui.checkBox_secure_conceal.isChecked()),
                                                                 self.ui.lineEdit_pcount.setEnabled(self.ui.checkBox_secure_conceal.isChecked()))),
                                                                 
        self.ui.lineEdit_baddress.setEnabled(self.ui.checkBox_secure_conceal.isChecked())
        self.ui.lineEdit_pcount.setEnabled(self.ui.checkBox_secure_conceal.isChecked())
        self.ui.lineEdit_baddress.editingFinished.connect(lambda: ( self.ui.lineEdit_baddress.setText(f'{(int(self.ui.lineEdit_baddress.text(), 16) & 0xFFFFF000):08X}'),
                                                                 self.updateValue((int(self.ui.lineEdit_baddress.text(),16) & 0xFFFFF000), 4),
                                                                 self.ui.lineEdit_pcount.setText(f'{int(self.ui.lineEdit_pcount.text()) if int(self.ui.lineEdit_pcount.text())<= ((self.size - int(self.ui.lineEdit_baddress.text(), 16)/1024))/self.page_size else int((self.size - int(self.ui.lineEdit_baddress.text(), 16)/1024)/self.page_size)}'),
                                                                 self.updateValue(int(self.ui.lineEdit_pcount.text()), 5)))
        self.ui.lineEdit_pcount.editingFinished.connect(lambda: ( self.ui.lineEdit_pcount.setText(f'{int(self.ui.lineEdit_pcount.text())if int(self.ui.lineEdit_pcount.text())<= (self.size - int(self.ui.lineEdit_baddress.text(), 16)/1024)/self.page_size else int((self.size - int(self.ui.lineEdit_baddress.text(), 16)/1024)/self.page_size)}'),
                                                               self.updateValue(int(self.ui.lineEdit_pcount.text()), 5))) 

    def check_secure_region(self):
        for i in range (0, 32):
            getattr(self.ui, (f'checkBox_{i}')).stateChanged.connect(lambda _, i=i: self.checkBit(not getattr(self.ui, (f'checkBox_{i}')).isChecked(), i, 8))
        for i in range (0, 32):
            getattr(self.ui, (f'checkBox_{i + 32}')).stateChanged.connect(lambda _, i=i: self.checkBit(not getattr(self.ui, (f'checkBox_{i+32}')).isChecked(), i, 9))

    def radioButton_bt_template_2(self):
        self.ui.radioButton_bt_0_0.setChecked(self.getBits(7, 0, 1, 0))
        self.ui.radioButton_bt_0_1.setChecked(self.getBits(7, 1, 1, 0))
     
    def radioButton_bt_template_4(self):
        self.ui.radioButton_bt_0_0.setChecked(self.getBits(6, 1, 2, 0))
        self.ui.radioButton_bt_0_1.setChecked(self.getBits(6, 3, 2, 0))
        self.ui.radioButton_bt_1_0.setChecked(self.getBits(6, 0, 2, 0))
        self.ui.radioButton_bt_1_1.setChecked(self.getBits(6, 2, 2, 0))
        
    def radioButton_hxt_template(self):
        self.ui.radioButton_hxt_0.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
        self.ui.radioButton_hxt_1.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
        self.ui.radioButton_hxt_0.setChecked(self.getBits(27, 1, 1, 0))
        self.ui.radioButton_hxt_1.setChecked(self.getBits(27, 0, 1, 0))
        
    def checkBox_security_lock_template(self):
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0))
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))
        
    def checkBox_ice_lock_template(self, place):    
        self.ui.checkBox_ice_lock.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_ice_lock.isChecked(), place, 0))
        self.ui.checkBox_ice_lock.setChecked(self.getBits(place, 0, 1, 0))
        
    def checkBox_watchdog_pwdwn_template(self):
        self.ui.checkBox_watchdog.stateChanged.connect(lambda: (self.ui.checkBox_watchdog_pwdwn.setEnabled(self.ui.checkBox_watchdog.isChecked()),
                                                                self.ui.checkBox_watchdog_pwdwn.setChecked(False) if self.ui.checkBox_watchdog.isEnabled() else None,
                                                                self.checkBit(not self.ui.checkBox_watchdog.isChecked(), 31, 0)))
        self.ui.checkBox_watchdog_pwdwn.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_watchdog_pwdwn.isChecked(), 30, 0))
        self.ui.checkBox_watchdog.setChecked(self.getBits(31, 0, 1, 0))
        self.ui.checkBox_watchdog_pwdwn.setChecked(self.getBits(30, 0, 1, 0) and self.ui.checkBox_watchdog.isChecked())
            
    def config_type_M051A_setup(self):
        self.ui.radioButton_bw_v_0.setText("4.5V")
        self.ui.radioButton_bw_v_1.setText("3.8V")
        self.config_type_M051B_setup()
    
    def config_type_M051B_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_2()

    def config_type_M258_setup(self):
        self.config_type_M251_setup()
        self.ui.gridGroupBox_bootclk.setVisible(True)
        self.ui.radioButton_mf_0.clicked.connect(lambda: self.updateBits(25, 0, 1, 0))
        self.ui.radioButton_mf_1.clicked.connect(lambda: self.updateBits(25, 1, 1, 0))
        self.ui.radioButton_mf_0.setChecked(self.getBits(25, 0, 1, 0))
        self.ui.radioButton_mf_1.setChecked(self.getBits(25, 0, 1, 0))
        
    def config_type_M251_setup(self):
        self.ui.gridGroupBox_bootclk.setVisible(False)
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.checkBox_watchdog.stateChanged.connect(lambda: (self.ui.checkBox_watchdog_pwdwn.setEnabled(self.ui.checkBox_watchdog.isChecked()),
                                                                self.ui.checkBox_watchdog_pwdwn.setChecked(False) if self.ui.checkBox_watchdog.isEnabled() else None,
                                                                self.checkBit(not self.ui.checkBox_watchdog.isChecked(), 31, 0), 
                                                                self.checkBitTwo(not self.ui.checkBox_watchdog.isChecked() or self.ui.checkBox_watchdog_pwdwn.isChecked(), 3, 0)))
        self.ui.checkBox_watchdog_pwdwn.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_watchdog_pwdwn.isChecked(), 30, 0),
                                                                      self.checkBitTwo(not self.ui.checkBox_watchdog.isChecked() or self.ui.checkBox_watchdog_pwdwn.isChecked(), 3, 0)))
        self.ui.checkBox_watchdog.setChecked(self.getBits(31, 0, 1, 0) or self.getBits(3, 0, 2, 0))
        self.ui.checkBox_watchdog_pwdwn.setChecked(self.getBits(30, 0, 1, 0) and self.ui.checkBox_watchdog.isChecked())
        self.checkBox_ice_lock_template(12)
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
    def config_type_M051D_setup(self):
        self.ui.gridGroupBox_multi_function.setVisible(False)
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 1, 1, 0))
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_2()
        
    def config_type_M058_setup(self):
        self.config_type_M051D_setup()
        self.ui.gridGroupBox_multi_function.setVisible(True)
        self.ui.radioButton_mf_0.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
        self.ui.radioButton_mf_1.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
        self.ui.radioButton_mf_0.setChecked(self.getBits(27, 0, 1, 0))
        self.ui.radioButton_mf_1.setChecked(self.getBits(27, 1, 1, 0))
    
    def config_type_NUC122_setup(self):
        self.config_type_NUC100_setup()
        self.ui.gridGroupBox_data_flash.setVisible(False)
        self.ui.lineEdit_config1.setVisible(False)
        self.ui.label_config1.setVisible(False)
        
    def config_type_NUC100_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.checkBox_security_lock_template()
        self.doubleSpinBox_pagesize_template() 
        self.radioButton_bt_template_2()
        
    def config_type_NUC123AN_setup(self):
        self.config_type_NUC123AE_setup()
        self.ui.gridGroupBox_io_state.setVisible(False)
        
    def config_type_NUC123AE_setup(self):
        self.ui.checkBox_ice_lock.setVisible(False)
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_mf_0.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
        self.ui.radioButton_mf_1.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
        self.ui.radioButton_mf_0.setChecked(self.getBits(27, 0, 1, 0))
        self.ui.radioButton_mf_1.setChecked(self.getBits(27, 0, 1, 0))
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 1, 1, 0))
        #data flash
        self.doubleSpinBox_pagesize_template()
        self.ui.checkBox_dataflash_size.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_dataflash_size.isChecked(), 2, 0))
        self.ui.checkBox_dataflash_size.setChecked(self.getBits(2, 0, 1, 0))
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()

    def config_type_NUC200_setup(self):
        self.config_type_NUC123AE_setup()
        self.ui.radioButton_bw_v_0.setText("4.4V")
        self.ui.radioButton_bw_v_1.setText("3.7V")
        self.ui.gridGroupBox_multi_function.setTitle("GPF[1:0] Multi-Function Options")
        self.ui.checkBox_dataflash_size.setVisible(False)
        self.ui.checkBox_security_lock.setVisible(False)

    def config_type_M0564_setup(self):
        self.config_type_NUC123AE_setup()
        self.ui.radioButton_bw_v_1.setText("3.7V")
        self.ui.gridGroupBox_multi_function.setTitle("PF[4:3] Multi-Function Options")
        self.ui.checkBox_dataflash_size.setVisible(False)
        
    def config_type_MINI51_setup(self):
        self.ui.radioButton_bw_v_0.clicked.connect(lambda: self.updateBits(21, 1, 2, 0))
        self.ui.radioButton_bw_v_1.clicked.connect(lambda: self.updateBits(21, 2, 2, 0))
        self.ui.radioButton_bw_v_2.clicked.connect(lambda: self.updateBits(21, 3, 2, 0))
        self.ui.radioButton_bw_v_0.setChecked(self.getBits(21, 1, 2, 0) or self.getBits(21, 0, 2, 0))
        self.ui.radioButton_bw_v_1.setChecked(self.getBits(21, 2, 2, 0)) 
        self.ui.radioButton_bw_v_2.setChecked(self.getBits(21, 3, 2, 0))
        self.checkBox_bw_1_template(20)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_2()
        
    def config_type_MINI51CN_setup(self):
        self.ui.radioButton_bw_v_0.clicked.connect(lambda: self.updateBits(21, 3, 3, 0))
        self.ui.radioButton_bw_v_1.clicked.connect(lambda: self.updateBits(21, 2, 3, 0))
        self.ui.radioButton_bw_v_2.clicked.connect(lambda: self.updateBits(21, 1, 3, 0))
        self.ui.radioButton_bw_v_3.clicked.connect(lambda: self.updateBits(21, 0, 3, 0))
        self.ui.radioButton_bw_v_4.clicked.connect(lambda: self.updateBits(21, 7, 3, 0))
        self.ui.radioButton_bw_v_0.setChecked(self.getBits(21, 3, 3, 0))
        self.ui.radioButton_bw_v_1.setChecked(self.getBits(21, 2, 3, 0)) 
        self.ui.radioButton_bw_v_2.setChecked(self.getBits(21, 1, 3, 0))
        self.ui.radioButton_bw_v_3.setChecked(self.getBits(21, 0, 3, 0))
        self.ui.radioButton_bw_v_4.setChecked(self.getBits(21, 7, 3, 0))
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
    
    def config_type_NANO100_setup(self):
        self.radioButton_bw_template_4(19)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.ui.checkBox_watchdog.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_watchdog.isChecked(), 31, 0))
        self.ui.checkBox_watchdog.setChecked(self.getBits(31, 0, 1, 0))
        self.radioButton_bt_template_4()
    
    def config_type_NANO112_setup(self):
        self.config_type_NANO100_setup()
        self.ui.checkBox_watchdog.setVisible(False)
        
    def config_type_NANO103_setup(self):
        self.ui.radioButton_bw_v_0.clicked.connect(lambda: self.updateBits(19, 15, 4, 0))
        self.ui.radioButton_bw_v_1.clicked.connect(lambda: self.updateBits(19, 13, 4, 0))
        self.ui.radioButton_bw_v_2.clicked.connect(lambda: self.updateBits(19, 12, 4, 0))
        self.ui.radioButton_bw_v_3.clicked.connect(lambda: self.updateBits(19, 11, 4, 0))
        self.ui.radioButton_bw_v_4.clicked.connect(lambda: self.updateBits(19, 10, 4, 0))
        self.ui.radioButton_bw_v_5.clicked.connect(lambda: self.updateBits(19, 9, 4, 0))
        self.ui.radioButton_bw_v_6.clicked.connect(lambda: self.updateBits(19, 8, 4, 0))
        self.ui.radioButton_bw_v_7.clicked.connect(lambda: self.updateBits(19, 7, 4, 0))
        self.ui.radioButton_bw_v_8.clicked.connect(lambda: self.updateBits(19, 6, 4, 0))
        self.ui.radioButton_bw_v_9.clicked.connect(lambda: self.updateBits(19, 5, 4, 0))
        self.ui.radioButton_bw_v_10.clicked.connect(lambda: self.updateBits(19, 4, 4, 0))
        self.ui.radioButton_bw_v_11.clicked.connect(lambda: self.updateBits(19, 3, 4, 0))
        self.ui.radioButton_bw_v_12.clicked.connect(lambda: self.updateBits(19, 2, 4, 0))
        self.ui.radioButton_bw_v_13.clicked.connect(lambda: self.updateBits(19, 1, 4, 0))
        self.ui.radioButton_bw_v_0.setChecked(self.getBits(19, 15, 4, 0))
        self.ui.radioButton_bw_v_1.setChecked(self.getBits(19, 13, 4, 0))
        self.ui.radioButton_bw_v_2.setChecked(self.getBits(19, 12, 4, 0))
        self.ui.radioButton_bw_v_3.setChecked(self.getBits(19, 11, 4, 0))
        self.ui.radioButton_bw_v_4.setChecked(self.getBits(19, 10, 4, 0))
        self.ui.radioButton_bw_v_5.setChecked(self.getBits(19, 9, 4, 0))
        self.ui.radioButton_bw_v_6.setChecked(self.getBits(19, 8, 4, 0))
        self.ui.radioButton_bw_v_7.setChecked(self.getBits(19, 7, 4, 0))
        self.ui.radioButton_bw_v_8.setChecked(self.getBits(19, 6, 4, 0))
        self.ui.radioButton_bw_v_9.setChecked(self.getBits(19, 5, 4, 0))
        self.ui.radioButton_bw_v_10.setChecked(self.getBits(19, 4, 4, 0))
        self.ui.radioButton_bw_v_11.setChecked(self.getBits(19, 3, 4, 0))
        self.ui.radioButton_bw_v_12.setChecked(self.getBits(19, 2, 4, 0))
        self.ui.radioButton_bw_v_13.setChecked(self.getBits(19, 1, 4, 0))
        self.checkBox_bw_0_template(23)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.ui.checkBox.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox.isChecked(), 12, 0))
        self.ui.checkBox.setChecked(self.getBits(12, 0, 1, 0))
        self.radioButton_bt_template_4()
        
    def config_type_MINI55_setup(self):
        self.ui.radioButton_bw_v_0.clicked.connect(lambda: self.updateBits(19, 14, 5, 0))
        self.ui.radioButton_bw_v_1.clicked.connect(lambda: self.updateBits(19, 10, 5, 0))
        self.ui.radioButton_bw_v_2.clicked.connect(lambda: self.updateBits(19, 15, 5, 0))
        self.ui.radioButton_bw_v_3.clicked.connect(lambda: self.updateBits(19, 6, 5, 0))
        self.ui.radioButton_bw_v_4.clicked.connect(lambda: self.updateBits(19, 11, 5, 0))
        self.ui.radioButton_bw_v_5.clicked.connect(lambda: self.updateBits(19, 2, 5, 0))
        self.ui.radioButton_bw_v_6.clicked.connect(lambda: self.updateBits(19, 7, 5, 0))
        self.ui.radioButton_bw_v_7.clicked.connect(lambda: self.updateBits(19, 3, 5, 0))
        self.ui.radioButton_bw_v_8.clicked.connect(lambda: self.updateBits(19, 31, 5, 0))
        self.ui.radioButton_bw_v_0.setChecked(self.getBits(19, 14, 5, 0))
        self.ui.radioButton_bw_v_1.setChecked(self.getBits(19, 10, 5, 0))
        self.ui.radioButton_bw_v_2.setChecked(self.getBits(19, 15, 5, 0))
        self.ui.radioButton_bw_v_3.setChecked(self.getBits(19, 6, 5, 0))
        self.ui.radioButton_bw_v_4.setChecked(self.getBits(19, 11, 5, 0))
        self.ui.radioButton_bw_v_5.setChecked(self.getBits(19, 2, 5, 0))
        self.ui.radioButton_bw_v_6.setChecked(self.getBits(19, 7, 5, 0))
        self.ui.radioButton_bw_v_7.setChecked(self.getBits(19, 3, 5, 0))
        self.ui.radioButton_bw_v_8.setChecked(self.getBits(19, 31, 5, 0))
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.ui.radioButton_rc_0.clicked.connect(lambda: (self.updateBits(15, 0, 1, 0),
                                                          self.updateBits(27, 1, 1, 0)))
        self.ui.radioButton_rc_1.clicked.connect(lambda: (self.updateBits(15, 1, 1, 0),
                                                          self.updateBits(27, 1, 1, 0)))
        self.ui.radioButton_rc_2.clicked.connect(lambda: (self.updateBits(15, 0, 1, 0),
                                                          self.updateBits(27, 0, 1, 0)))
        self.ui.radioButton_rc_3.clicked.connect(lambda: (self.updateBits(15, 1, 1, 0),
                                                          self.updateBits(27, 0, 1, 0)))
        self.ui.radioButton_rc_0.setChecked(self.getBits(15, 0, 1, 0) and self.getBits(27, 1, 1, 0))
        self.ui.radioButton_rc_1.setChecked(self.getBits(15, 1, 1, 0) and self.getBits(27, 1, 1, 0))
        self.ui.radioButton_rc_2.setChecked(self.getBits(15, 0, 1, 0) and self.getBits(27, 0, 1, 0))
        self.ui.radioButton_rc_3.setChecked(self.getBits(15, 1, 1, 0) and self.getBits(27, 0, 1, 0))
        self.radioButton_bt_template_4()
        
    def config_type_NM1120_setup(self):
        self.radioButton_bw_template_8(13)
        self.checkBox_bw_0_template(11)
        self.checkBox_bw_1_template(12)
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.radioButton_gpa0_0.clicked.connect(lambda: self.updateBits(16, 0, 2, 0))
        self.ui.radioButton_gpa0_1.clicked.connect(lambda: self.updateBits(16, 1, 2, 0))
        self.ui.radioButton_gpa0_2.clicked.connect(lambda: self.updateBits(16, 3, 2, 0))
        self.ui.radioButton_gpa0_0.setChecked(self.getBits(16, 0, 2, 0))
        self.ui.radioButton_gpa0_1.setChecked(self.getBits(16, 1, 2, 0))
        self.ui.radioButton_gpa0_2.setChecked(self.getBits(16, 3, 2, 0))
        self.ui.radioButton_gpa1_0.clicked.connect(lambda: self.updateBits(18, 0, 2, 0))
        self.ui.radioButton_gpa1_1.clicked.connect(lambda: self.updateBits(18, 1, 2, 0))
        self.ui.radioButton_gpa1_2.clicked.connect(lambda: self.updateBits(18, 3, 2, 0))
        self.ui.radioButton_gpa1_0.setChecked(self.getBits(18, 0, 2, 0))
        self.ui.radioButton_gpa1_1.setChecked(self.getBits(18, 1, 2, 0))
        self.ui.radioButton_gpa1_2.setChecked(self.getBits(18, 3, 2, 0))
        self.ui.radioButton_gpa2_0.clicked.connect(lambda: self.updateBits(20, 0, 2, 0))
        self.ui.radioButton_gpa2_1.clicked.connect(lambda: self.updateBits(20, 1, 2, 0))
        self.ui.radioButton_gpa2_2.clicked.connect(lambda: self.updateBits(20, 3, 2, 0))
        self.ui.radioButton_gpa2_0.setChecked(self.getBits(20, 0, 2, 0))
        self.ui.radioButton_gpa2_1.setChecked(self.getBits(20, 1, 2, 0))
        self.ui.radioButton_gpa2_2.setChecked(self.getBits(20, 3, 2, 0))
        self.ui.radioButton_gpa3_0.clicked.connect(lambda: self.updateBits(22, 0, 2, 0))
        self.ui.radioButton_gpa3_1.clicked.connect(lambda: self.updateBits(22, 1, 2, 0))
        self.ui.radioButton_gpa3_2.clicked.connect(lambda: self.updateBits(22, 3, 2, 0))
        self.ui.radioButton_gpa3_0.setChecked(self.getBits(22, 0, 2, 0))
        self.ui.radioButton_gpa3_1.setChecked(self.getBits(22, 1, 2, 0))
        self.ui.radioButton_gpa3_2.setChecked(self.getBits(22, 3, 2, 0))
        self.ui.radioButton_gpa4_0.clicked.connect(lambda: self.updateBits(24, 0, 2, 0))
        self.ui.radioButton_gpa4_1.clicked.connect(lambda: self.updateBits(24, 1, 2, 0))
        self.ui.radioButton_gpa4_2.clicked.connect(lambda: self.updateBits(24, 3, 2, 0))
        self.ui.radioButton_gpa4_0.setChecked(self.getBits(24, 0, 2, 0))
        self.ui.radioButton_gpa4_1.setChecked(self.getBits(24, 1, 2, 0))
        self.ui.radioButton_gpa4_2.setChecked(self.getBits(24, 3, 2, 0))
        self.ui.radioButton_gpa5_0.clicked.connect(lambda: self.updateBits(26, 0, 2, 0))
        self.ui.radioButton_gpa5_1.clicked.connect(lambda: self.updateBits(26, 1, 2, 0))
        self.ui.radioButton_gpa5_2.clicked.connect(lambda: self.updateBits(26, 3, 2, 0))
        self.ui.radioButton_gpa5_0.setChecked(self.getBits(26, 0, 2, 0))
        self.ui.radioButton_gpa5_1.setChecked(self.getBits(26, 1, 2, 0))
        self.ui.radioButton_gpa5_2.setChecked(self.getBits(26, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
    def config_type_NM1500_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.ui.checkBox.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox.isChecked(), 12, 0))
        self.ui.checkBox.setChecked(self.getBits(12, 1, 1, 0))
        self.ui.checkBox_2.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_2.isChecked(), 8, 0))
        self.ui.checkBox_2.setChecked(self.getBits(8, 1, 1, 0))
        self.ui.checkBox_3.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_3.isChecked(), 9, 0))
        self.ui.checkBox_3.setChecked(self.getBits(9, 1, 1, 0))
        self.ui.checkBox_4.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_4.isChecked(), 10, 0))
        self.ui.checkBox_4.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.checkBox_5.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_5.isChecked(), 11, 0))
        self.ui.checkBox_5.setChecked(self.getBits(11, 1, 1, 0))
        self.radioButton_bt_template_4()
        
    def config_type_NUC400_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.radioButton_mf_0.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
        self.ui.radioButton_mf_1.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
        self.ui.radioButton_mf_0.setChecked(self.getBits(27, 0, 1, 0))
        self.ui.radioButton_mf_1.setChecked(self.getBits(27, 1, 1, 0))
        self.ui.radioButton_mf2_0.clicked.connect(lambda: self.updateBits(14, 0, 1, 0))
        self.ui.radioButton_mf2_1.clicked.connect(lambda: self.updateBits(14, 1, 1, 0))
        self.ui.radioButton_mf2_0.setChecked(self.getBits(14, 0, 1, 0))
        self.ui.radioButton_mf2_1.setChecked(self.getBits(14, 1, 1, 0))
        self.ui.radioButton.clicked.connect(lambda: self.updateBits(15, 0, 1, 0))
        self.ui.radioButton_2.clicked.connect(lambda: self.updateBits(15, 1, 1, 0))
        self.ui.radioButton.setChecked(self.getBits(15, 0, 1, 0))
        self.ui.radioButton_2.setChecked(self.getBits(15, 1, 1, 0))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
    def config_type_M451_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.radioButton_hxt_template()
        self.ui.radioButton_wdt_0.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_1.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.ui.radioButton_wdt_2.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_0.setChecked(self.getBits(31, 1, 1, 0))
        self.ui.radioButton_wdt_1.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.ui.radioButton_wdt_2.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
    
    def config_type_NUC1262_setup(self):
        self.config_type_NUC123AE_setup()
        self.ui.radioButton_bw_v_1.setText("3.7V")
        self.ui.gridGroupBox_multi_function.setVisible(False)
        self.ui.checkBox_dataflash_size.setVisible(False)
       
    def config_type_M031_setup(self):
        self.radioButton_bt_template_4()
        self.ui.radioButton_rst_0.clicked.connect(lambda: self.updateBits(8, 1, 1, 0))
        self.ui.radioButton_rst_1.clicked.connect(lambda: self.updateBits(8, 0, 1, 0))
        self.ui.radioButton_rst_0.setChecked(self.getBits(8, 1, 1, 0))
        self.ui.radioButton_rst_1.setChecked(self.getBits(8, 0, 1, 0))
        self.ui.radioButton_ext_0.clicked.connect(lambda: self.updateBits(9, 1, 1, 0))
        self.ui.radioButton_ext_1.clicked.connect(lambda: self.updateBits(9, 0, 1, 0))
        self.ui.radioButton_ext_0.setChecked(self.getBits(9, 1, 1, 0))
        self.ui.radioButton_ext_1.setChecked(self.getBits(9, 0, 1, 0))
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.radioButton_bw_v_0.clicked.connect(lambda: self.updateBits(21, 1, 1, 0))
        self.ui.radioButton_bw_v_1.clicked.connect(lambda: self.updateBits(21, 0, 1, 0))
        self.ui.radioButton_bw_v_0.setChecked(self.getBits(21, 1, 1, 0))
        self.ui.radioButton_bw_v_1.setChecked(self.getBits(21, 0, 1, 0)) 
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_hxt_template()
        self.ui.radioButton_wdt_0.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_1.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.ui.radioButton_wdt_2.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_0.setChecked(self.getBits(31, 1, 1, 0))
        self.ui.radioButton_wdt_1.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.ui.radioButton_wdt_2.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0),
                                                                     self.ui.lineEdit_security.setEnabled(self.ui.checkBox_security_lock.isChecked()),
                                                                     self.ui.lineEdit_security.setText(f'{(0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A):02X}'),
                                                                     self.updateBits(0, (0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))
        self.ui.lineEdit_security.editingFinished.connect(lambda: (self.ui.lineEdit_security.setText(f'{((int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A)& 0x5A):02X}'),
                                                                   self.updateBits(0,(int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))                                                            
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(12)
       
    def config_type_M030G_setup(self):
        self.config_type_M031_setup()
        self.ui.gridGroupBox_brownout.setVisible(False)
        self.ui.gridGroupBox_hxt.setVisible(False)
        self.ui.radioButton_wdt_2.setVisible(False)
        
    def config_type_M0A21_setup(self):
        self.radioButton_bt_template_4()
        self.ui.radioButton_rst_0.clicked.connect(lambda: self.updateBits(8, 1, 1, 0))
        self.ui.radioButton_rst_1.clicked.connect(lambda: self.updateBits(8, 0, 1, 0))
        self.ui.radioButton_rst_0.setChecked(self.getBits(8, 1, 1, 0))
        self.ui.radioButton_rst_1.setChecked(self.getBits(8, 0, 1, 0))
        self.ui.radioButton_ext_0.clicked.connect(lambda: self.updateBits(9, 1, 1, 0))
        self.ui.radioButton_ext_1.clicked.connect(lambda: self.updateBits(9, 0, 1, 0))
        self.ui.radioButton_ext_0.setChecked(self.getBits(9, 1, 1, 0))
        self.ui.radioButton_ext_1.setChecked(self.getBits(9, 0, 1, 0))
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_mode_0.clicked.connect(lambda: self.updateBits(25, 1, 1, 0))
        self.ui.radioButton_mode_1.clicked.connect(lambda: self.updateBits(25, 0, 1, 0))
        self.ui.radioButton_mode_0.setChecked(self.getBits(25, 1, 1, 0))
        self.ui.radioButton_mode_1.setChecked(self.getBits(25, 0, 1, 0))
        self.radioButton_hxt_template()
        self.ui.radioButton_wdt_0.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_1.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.ui.radioButton_wdt_2.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_0.setChecked(self.getBits(31, 1, 1, 0))
        self.ui.radioButton_wdt_1.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.ui.radioButton_wdt_2.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0),
                                                                     self.ui.lineEdit_security.setEnabled(self.ui.checkBox_security_lock.isChecked()),
                                                                     self.ui.lineEdit_security.setText(f'{(0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A):02X}'),
                                                                     self.updateBits(0, (0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))
        self.ui.lineEdit_security.editingFinished.connect(lambda: (self.ui.lineEdit_security.setText(f'{((int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A)& 0x5A):02X}'),
                                                                   self.updateBits(0,(int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))                                                                   
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(12)
        
    def config_type_M480_setup(self):
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_bt_template_4()
        self.radioButton_hxt_template()
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.checkBox.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox.isChecked(), 5, 0))
        self.ui.checkBox.setChecked(self.getBits(5, 0, 1, 0))
        self.ui.radioButton_mf_0.clicked.connect(lambda: self.updateBits(4, 0, 2, 3))
        self.ui.radioButton_mf_1.clicked.connect(lambda: self.updateBits(4, 1, 2, 3))
        self.ui.radioButton_mf_2.clicked.connect(lambda: self.updateBits(4, 2, 2, 3))
        self.ui.radioButton_mf_3.clicked.connect(lambda: self.updateBits(4, 3, 2, 3))
        self.ui.radioButton_mf_0.setChecked(self.getBits(4, 0, 2, 3))
        self.ui.radioButton_mf_1.setChecked(self.getBits(4, 1, 2, 3)) 
        self.ui.radioButton_mf_2.setChecked(self.getBits(4, 2, 2, 3))
        self.ui.radioButton_mf_3.setChecked(self.getBits(4, 3, 2, 3))
        self.ui.radioButton_mf2_0.clicked.connect(lambda: self.updateBits(0, 0, 2, 3))
        self.ui.radioButton_mf2_1.clicked.connect(lambda: self.updateBits(0, 1, 2, 3))
        self.ui.radioButton_mf2_2.clicked.connect(lambda: self.updateBits(0, 2, 2, 3))
        self.ui.radioButton_mf2_3.clicked.connect(lambda: self.updateBits(0, 3, 2, 3))
        self.ui.radioButton_mf2_0.setChecked(self.getBits(0, 0, 2, 3))
        self.ui.radioButton_mf2_1.setChecked(self.getBits(0, 1, 2, 3)) 
        self.ui.radioButton_mf2_2.setChecked(self.getBits(0, 2, 2, 3))
        self.ui.radioButton_mf2_3.setChecked(self.getBits(0, 3, 2, 3))
        self.doubleSpinBox_pagesize_template()
        self.ui.checkBox_watchdog.stateChanged.connect(lambda: (self.ui.checkBox_watchdog_pwdwn.setEnabled(self.ui.checkBox_watchdog.isChecked()),
                                                                self.ui.checkBox_watchdog_pwdwn.setChecked(False) if self.ui.checkBox_watchdog.isEnabled() else None,
                                                                self.checkBit(not self.ui.checkBox_watchdog.isChecked(), 31, 0), 
                                                                self.checkBitTwo(not self.ui.checkBox_watchdog.isChecked() or self.ui.checkBox_watchdog_pwdwn.isChecked(), 3, 0)))
        self.ui.checkBox_watchdog_pwdwn.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_watchdog_pwdwn.isChecked(), 30, 0),
                                                                      self.checkBitTwo(not self.ui.checkBox_watchdog.isChecked() or self.ui.checkBox_watchdog_pwdwn.isChecked(), 3, 0)))
        self.ui.checkBox_watchdog.setChecked(self.getBits(31, 0, 1, 0) or self.getBits(3, 0, 2, 0))
        self.ui.checkBox_watchdog_pwdwn.setChecked(self.getBits(30, 0, 1, 0) and self.ui.checkBox_watchdog.isChecked())
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0),
                                                                     self.updateValue((0xFFFF5A00 if self.ui.checkBox_security_lock.isChecked() else 0xFFFF5A5A), 2)))                                                        
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        self.ui.checkBox_sprom_lock.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_sprom_lock.isChecked(), 12, 0))
        self.ui.checkBox_sprom_lock.setChecked(self.getBits(12, 0, 1, 0))
        
    def config_type_M480LD_setup(self):
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_bt_template_4()
        self.radioButton_hxt_template()
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.ui.checkBox.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox.isChecked(), 5, 0))
        self.ui.checkBox.setChecked(self.getBits(5, 0, 1, 0))
        self.doubleSpinBox_pagesize_template()
        self.ui.checkBox_watchdog.stateChanged.connect(lambda: (self.ui.checkBox_watchdog_pwdwn.setEnabled(self.ui.checkBox_watchdog.isChecked()),
                                                                self.ui.checkBox_watchdog_pwdwn.setChecked(False) if self.ui.checkBox_watchdog.isEnabled() else None,
                                                                self.checkBit(not self.ui.checkBox_watchdog.isChecked(), 31, 0), 
                                                                self.checkBitTwo(not self.ui.checkBox_watchdog.isChecked() or self.ui.checkBox_watchdog_pwdwn.isChecked(), 3, 0)))
        self.ui.checkBox_watchdog_pwdwn.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_watchdog_pwdwn.isChecked(), 30, 0),
                                                                      self.checkBitTwo(not self.ui.checkBox_watchdog.isChecked() or self.ui.checkBox_watchdog_pwdwn.isChecked(), 3, 0)))
        self.ui.checkBox_watchdog.setChecked(self.getBits(31, 0, 1, 0) or self.getBits(3, 0, 2, 0))
        self.ui.checkBox_watchdog_pwdwn.setChecked(self.getBits(30, 0, 1, 0) and self.ui.checkBox_watchdog.isChecked())
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0),
                                                                     self.updateBits(0,(0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))                                                        
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        self.ui.checkBox_security_boot_lock.stateChanged.connect(lambda: self.updateBits(8,(0x00 if self.ui.checkBox_security_boot_lock.isChecked() else 0x5A), 8, 2))                                                        
        self.ui.checkBox_security_boot_lock.setChecked(self.getBits(8, 0, 8, 2))
        
    def config_type_M460_setup(self):
        self.radioButton_bt_template_2()
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_wdt_0.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_1.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.ui.radioButton_wdt_2.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_0.setChecked(self.getBits(31, 1, 1, 0))
        self.ui.radioButton_wdt_1.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.ui.radioButton_wdt_2.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.ui.checkBox_isp_uart.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_uart.isChecked(), 8, 3))                                                        
        self.ui.checkBox_isp_uart.setChecked(self.getBits(8, 1, 1, 3))
        self.ui.checkBox_isp_usb.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_isp_usb.isChecked(), 9, 3))                                                        
        self.ui.checkBox_isp_usb.setChecked(self.getBits(9, 0, 1, 3))
        self.ui.checkBox_isp_can.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_can.isChecked(), 10, 3))                                                        
        self.ui.checkBox_isp_can.setChecked(self.getBits(10, 1, 1, 3))
        self.ui.checkBox_isp_i2c.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_i2c.isChecked(), 11, 3))                                                        
        self.ui.checkBox_isp_i2c.setChecked(self.getBits(11, 1, 1, 3))
        self.ui.checkBox_isp_spi.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_spi.isChecked(), 12, 3))                                                        
        self.ui.checkBox_isp_spi.setChecked(self.getBits(12, 1, 1, 3))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_ice_lock_template(11)
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0),
                                                                     self.ui.lineEdit_security.setEnabled(self.ui.checkBox_security_lock.isChecked()),
                                                                     self.ui.lineEdit_protect.setEnabled(self.ui.checkBox_security_lock.isChecked()),
                                                                     self.ui.lineEdit_security.setText(f'{(0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A):02X}'),
                                                                     self.ui.lineEdit_protect.setText(f'{(0x5A):02X}'), 
                                                                     self.updateBits(0, (0x5A00 if self.ui.checkBox_security_lock.isChecked() else 0x5A5A), 16, 2)))
        self.ui.lineEdit_security.editingFinished.connect(lambda: (self.ui.lineEdit_security.setText(f'{((int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A)& 0x5A):02X}'),
                                                                   self.updateBits(0,(int(self.ui.lineEdit_protect.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))
        self.ui.lineEdit_protect.editingFinished.connect(lambda: (self.ui.lineEdit_protect.setText(f'{((int(self.ui.lineEdit_protect.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A)& 0x5A):02X}'),
                                                                  self.updateBits(8,(int(self.ui.lineEdit_protect.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))                                                                                                                                    
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))

    def config_type_M2351_setup(self):
        self.config_type_M2354_setup()
        self.ui.checkBox_tamper.setVisible(False)
        
    def config_type_M2354_setup(self):
        self.radioButton_bt_template_2()
        self.ui.checkBox_bt.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_bt.isChecked(), 5, 0))                                                        
        self.ui.checkBox_bt.setChecked(self.getBits(5, 0, 1, 0))
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_hxt_template()
        self.ui.radioButton_wdt_0.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_1.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.ui.radioButton_wdt_2.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_0.setChecked(self.getBits(31, 1, 1, 0))
        self.ui.radioButton_wdt_1.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.ui.radioButton_wdt_2.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.ui.radioButton_mf2_0.clicked.connect(lambda: self.updateBits(0, 7, 3, 3))
        self.ui.radioButton_mf2_1.clicked.connect(lambda: self.updateBits(0, 3, 3, 3))
        self.ui.radioButton_mf2_2.clicked.connect(lambda: self.updateBits(0, 2, 3, 3))
        self.ui.radioButton_mf2_3.clicked.connect(lambda: self.updateBits(0, 1, 3, 3))
        self.ui.radioButton_mf2_4.clicked.connect(lambda: self.updateBits(0, 0, 3, 3))
        self.ui.radioButton_mf2_0.setChecked(self.getBits(0, 7, 3, 3))
        self.ui.radioButton_mf2_1.setChecked(self.getBits(0, 3, 3, 3)) 
        self.ui.radioButton_mf2_2.setChecked(self.getBits(0, 2, 3, 3))
        self.ui.radioButton_mf2_3.setChecked(self.getBits(0, 1, 3, 3))
        self.ui.radioButton_mf2_4.setChecked(self.getBits(0, 0, 3, 3))
        self.ui.checkBox_tamper.stateChanged.connect(lambda: self.updateBits(16,(0x5AA5 if self.ui.checkBox_tamper.isChecked() else 0xFFFF), 16, 3))                                                                      
        self.ui.checkBox_tamper.setChecked(self.getBits(16, 0x5AA5, 16, 3))
        
    def config_type_M471_setup(self):
        self.radioButton_bt_template_4()
        self.ui.radioButton_io_0.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.ui.radioButton_io_0.setChecked(self.getBits(10, 1, 1, 0))
        self.ui.radioButton_io_1.setChecked(self.getBits(10, 0, 1, 0))
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_wdt_0.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_1.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.ui.radioButton_wdt_2.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_0.setChecked(self.getBits(31, 1, 1, 0))
        self.ui.radioButton_wdt_1.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.ui.radioButton_wdt_2.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0),
                                                                     self.ui.lineEdit_security.setEnabled(self.ui.checkBox_security_lock.isChecked()),
                                                                     self.ui.lineEdit_security.setText(f'{(0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A):02X}'),
                                                                     self.updateBits(0, (0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))
        self.ui.lineEdit_security.editingFinished.connect(lambda: (self.ui.lineEdit_security.setText(f'{((int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A)& 0x5A):02X}'),
                                                                   self.updateBits(0,(int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))                                                                   
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        
    def config_type_M2L31_setup(self):
        self.radioButton_bt_template_2()
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.ui.radioButton_wdt_0.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.ui.radioButton_wdt_1.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.ui.radioButton_wdt_0.setChecked(self.getBits(31, 1, 1, 0))
        self.ui.radioButton_wdt_1.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.ui.checkBox_isp_uart.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_uart.isChecked(), 8, 3))                                                        
        self.ui.checkBox_isp_uart.setChecked(self.getBits(8, 1, 1, 3))
        self.ui.checkBox_isp_usb.stateChanged.connect(lambda: self.checkBit(not self.ui.checkBox_isp_usb.isChecked(), 9, 3))                                                        
        self.ui.checkBox_isp_usb.setChecked(self.getBits(9, 0, 1, 3))
        self.ui.checkBox_isp_can.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_can.isChecked(), 10, 3))                                                        
        self.ui.checkBox_isp_can.setChecked(self.getBits(10, 1, 1, 3))
        self.ui.checkBox_isp_i2c.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_i2c.isChecked(), 11, 3))                                                        
        self.ui.checkBox_isp_i2c.setChecked(self.getBits(11, 1, 1, 3))
        self.ui.checkBox_isp_spi.stateChanged.connect(lambda: self.checkBit(self.ui.checkBox_isp_spi.isChecked(), 12, 3))                                                        
        self.ui.checkBox_isp_spi.setChecked(self.getBits(12, 1, 1, 3))
        self.ui.radioButton_mf_0.clicked.connect(lambda: self.updateBits(0, 0, 2, 3))
        self.ui.radioButton_mf_1.clicked.connect(lambda: self.updateBits(0, 1, 2, 3))
        self.ui.radioButton_mf_2.clicked.connect(lambda: self.updateBits(0, 2, 2, 3))
        self.ui.radioButton_mf_3.clicked.connect(lambda: self.updateBits(0, 3, 2, 3))
        self.ui.radioButton_mf_0.setChecked(self.getBits(0, 0, 2, 3))
        self.ui.radioButton_mf_1.setChecked(self.getBits(0, 1, 2, 3)) 
        self.ui.radioButton_mf_2.setChecked(self.getBits(0, 2, 2, 3))
        self.ui.radioButton_mf_3.setChecked(self.getBits(0, 3, 2, 3))
        self.secure_conceal_pagesize_template()
        self.ui.checkBox_security_lock.stateChanged.connect(lambda: (self.checkBit(not self.ui.checkBox_security_lock.isChecked(), 1, 0),
                                                                     self.ui.lineEdit_security.setEnabled(self.ui.checkBox_security_lock.isChecked()),
                                                                     self.ui.lineEdit_protect.setEnabled(self.ui.checkBox_security_lock.isChecked()),
                                                                     self.ui.lineEdit_security.setText(f'{(0x00 if self.ui.checkBox_security_lock.isChecked() else 0x5A):02X}'),
                                                                     self.ui.lineEdit_protect.setText(f'{(0x5A):02X}'), 
                                                                     self.updateBits(0, (0x5A00 if self.ui.checkBox_security_lock.isChecked() else 0x5A5A), 16, 2)))
        self.ui.lineEdit_security.editingFinished.connect(lambda: (self.ui.lineEdit_security.setText(f'{((int(self.ui.lineEdit_security.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A)& 0x5A):02X}'),
                                                                   self.updateBits(0,(int(self.ui.lineEdit_protect.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))
        self.ui.lineEdit_protect.editingFinished.connect(lambda: (self.ui.lineEdit_protect.setText(f'{((int(self.ui.lineEdit_protect.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A)& 0x5A):02X}'),
                                                                  self.updateBits(8,(int(self.ui.lineEdit_protect.text(), base = 16) if self.ui.checkBox_security_lock.isChecked() else 0x5A), 8, 2)))                                                                                                                                    
        self.ui.checkBox_security_lock.setChecked(self.getBits(1, 0, 1, 0))
        self.check_secure_region()
        self.checkBox_ice_lock_template(11)
        self.ui.radioButton_lv0.clicked.connect(lambda: (self.updateBits(0, 0xFFFFFFFF, 32, 10),
                                                         self.ui.radioButton_pin0.setChecked(True),
                                                         self.ui.GroupBox_pin.setEnabled(False)))
        self.ui.radioButton_lv1.clicked.connect(lambda: (self.updateBits(0, 0x005A, 16, 10),
                                                         self.ui.radioButton_pin0.setChecked(True),
                                                         self.ui.GroupBox_pin.setEnabled(False)))
        self.ui.radioButton_lv2.clicked.connect(lambda: (self.updateBits(0, 0x335A, 16, 10),
                                                         self.ui.radioButton_pin0.setChecked(True),
                                                         self.ui.GroupBox_pin.setEnabled(True)))
        self.ui.radioButton_lv3.clicked.connect(lambda: (self.updateBits(0, 0x995A, 16, 10),
                                                         self.ui.radioButton_pin0.setChecked(True),
                                                         self.ui.GroupBox_pin.setEnabled(True)))
        self.ui.radioButton_pin0.clicked.connect(lambda: self.updateBits(0, 0xA, 4, 10))
        self.ui.radioButton_pin1.clicked.connect(lambda: self.updateBits(0, 0xB, 4, 10))
        self.ui.radioButton_pin2.clicked.connect(lambda: self.updateBits(0, 0xC, 4, 10))
        self.ui.radioButton_pin3.clicked.connect(lambda: self.updateBits(0, 0xD, 4, 10))
        self.ui.radioButton_lv0.setChecked(True)
        self.ui.radioButton_pin0.setChecked(True)
                     
    def valid_setting(self):
        reg_key8 = QRegExpValidator(QRegExp("[0-9A-Fa-f]{1,8}"))
        reg_key2 = QRegExpValidator(QRegExp("[0-9A-Fa-f]{1,2}"))
        if hasattr(self.ui, 'lineEdit_data_address'):
            line_edit = getattr(self.ui, 'lineEdit_data_address')
            line_edit.setValidator(reg_key8)
            
        if hasattr(self.ui, 'lineEdit_security'):
            line_edit = getattr(self.ui, 'lineEdit_security')
            line_edit.setValidator(reg_key2)
            
        if hasattr(self.ui, 'lineEdit_protect'):
            line_edit = getattr(self.ui, 'lineEdit_protect')
            line_edit.setValidator(reg_key2)
                     
    def exportFile(self):
        for i in range(0, 14):
            self.parent.wconfig[i] = self.wconfig[i]
        print("Success")
        self.close()
    

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    w = ConfigDialog()
    w.__init__()
    w.show()
    sys.exit(app.exec_())

