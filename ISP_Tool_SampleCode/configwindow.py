#!/usr/bin/env python
from ctypes import *
import json
import os

from PySide6.QtCore import QDateTime, QPointF, QRegularExpression, Qt, QTimer, QFile
from PySide6.QtGui import QColor, QIntValidator, QRegularExpressionValidator, QValidator
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QFileDialog, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel,
        QLineEdit, QMessageBox, QPlainTextEdit, QProgressBar, QPushButton, QRadioButton, QScrollBar,
        QSizePolicy, QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QStyle)
from PySide6.QtUiTools import QUiLoader

from PartNumID import *
from config_selection import *

class ConfigDialog(QDialog):
    def __init__(self, parent=None, ctp = None):
        super().__init__(parent)

        self.parent = parent
        self.ctp = ctp
        #self.ui = ui
        #self.ui.setupUi(self)
        self.setWindowTitle("Config Setting")
        self.wconfig = (c_uint * 19)(0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                     0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                     0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,0xFFFFFFFF,
                                     0xFFFFFFFF)
        for i in range(0, 19):
            self.wconfig[i] = self.parent.wconfig[i]
            
        self.size = float(self.parent.memory_size / 1024)
        self.page_size = float(self.parent.page_size / 1024)
        
        root = QVBoxLayout(self)
        
        self.tabs = QTabWidget()
        
        tab_tank = None
        self.page_0 = None
        self.page_1 = None
        self.page_2 = None
        self.page_3 = None
        
        if config_setting_str(ctp) == "NUC100":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc100.ui")]
            func = self.config_type_NUC100_setup
        elif config_setting_str(ctp) == "NUC122":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc102.ui")]
            func = self.config_type_NUC122_setup
        elif config_setting_str(ctp) == "NUC123AN":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc103.ui")]
            func = self.config_type_NUC123AN_setup
        elif config_setting_str(ctp) == "NUC123AE":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc103bn.ui")]
            func = self.config_type_NUC123AE_setup
        elif config_setting_str(ctp) == "NUC131":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc103bn.ui")]
            func = self.config_type_NUC123AE_setup
        elif config_setting_str(ctp) == "NUC200":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc200.ui")]
            func = self.config_type_NUC200_setup
        elif config_setting_str(ctp) == "NANO100":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nano100.ui")]
            func = self.config_type_NANO100_setup
        elif config_setting_str(ctp) == "NANO103":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nano103.ui")]
            func = self.config_type_NANO103_setup
        elif config_setting_str(ctp) == "NANO112":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nano112.ui")]
            func = self.config_type_NANO112_setup
        elif config_setting_str(ctp) == "M051A":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_m051.ui")]
            func = self.config_type_M051A_setup
        elif config_setting_str(ctp) == "M051B":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_m051.ui")]
            func = self.config_type_M051B_setup
        elif config_setting_str(ctp) == "M051D":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_m051cn.ui")]
            func = self.config_type_M051D_setup
        elif config_setting_str(ctp) == "M058":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_m058.ui")]
            func = self.config_type_M058_setup
        elif config_setting_str(ctp) == "MINI51":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_mini51.ui")]
            func = self.config_type_MINI51_setup
        elif config_setting_str(ctp) == "MINI51CN":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_mini51cn.ui")]
            func = self.config_type_MINI51CN_setup
        elif config_setting_str(ctp) == "MINI55":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nm1200.ui")]
            func = self.config_type_MINI55_setup
        elif config_setting_str(ctp) == "NM1500":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_mt500.ui")]
            func = self.config_type_NM1500_setup
        elif config_setting_str(ctp) == "NUC400":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc400.ui")]
            func = self.config_type_NUC400_setup
        elif config_setting_str(ctp) == "M3331":
            tab_tank = [(self.page_0, "Config 0-6",  "ui/idd_dialog_chip_setting_cfg_m3331.ui"),
                        (self.page_1, "Config 8-10", "ui/idd_dialog_chip_setting_apwprot.ui"),
                        (self.page_2, "Config 11-13","ui/idd_dialog_chip_setting_nscba_lock.ui"),
                        (self.page_3, "Config 16-18","ui/idd_dialog_chip_setting_ldwprot.ui")]
            func = self.config_type_M3331_setup  #todo
        elif config_setting_str(ctp) == "NM1120":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nm1120.ui")]
            func = self.config_type_NM1120_setup
            '''
        elif config_setting_str(ctp) == "8051":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_ot8051.ui")]
            func = self.config_type_8051_setup
            '''
        elif config_setting_str(ctp) == "M0564":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_m0564.ui")]
            func = self.config_type_M0564_setup
        elif config_setting_str(ctp) == "NUC1262":
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_configuration_nuc1262.ui")]
            func = self.config_type_NUC1262_setup
        elif config_setting_str(ctp) == "M480":
            tab_tank = [(self.page_0, "Config 0-3",  "ui/idd_dialog_configuration_m480.ui")]
            func = self.config_type_M480_setup
        elif config_setting_str(ctp) == "M480LD":
            tab_tank = [(self.page_0, "Config 0-3",  "ui/idd_dialog_configuration_m480ld.ui")]
            func = self.config_type_M480LD_setup
        elif config_setting_str(ctp) == "M460":
            tab_tank = [(self.page_0, "Config 0-3",  "ui/idd_dialog_chip_setting_cfg_m460.ui")]
            func = self.config_type_M460_setup
        elif config_setting_str(ctp) == "M2351":
            tab_tank = [(self.page_0, "Config 0, 3",  "ui/idd_dialog_chip_setting_cfg_m2351.ui")]
            func = self.config_type_M2351_setup
        elif config_setting_str(ctp) == "M2354":
            tab_tank = [(self.page_0, "Config 0, 3",  "ui/idd_dialog_chip_setting_cfg_m2351.ui")]
            func = self.config_type_M2354_setup
        elif config_setting_str(ctp) == "M2L31":
            tab_tank = [(self.page_0, "Config 0-3",  "ui/idd_dialog_chip_setting_cfg_m2l31.ui"),
                        (self.page_1, "Config 8-10", "ui/idd_dialog_chip_setting_apwprot.ui")]
            func = self.config_type_M2L31_setup
        elif config_setting_str(ctp) == "M2A23":
            tab_tank = [(self.page_0, "Config 0-2",  "ui/idd_dialog_chip_setting_cfg_m0a21.ui"),
                        (self.page_1, "Config 8-10", "ui/idd_dialog_chip_setting_apwprot.ui")]
            func = self.config_type_M2A23_setup  
        elif config_setting_str(ctp) == "M2003":
            tab_tank = [(self.page_0, "Config 0-2",  "ui/idd_dialog_chip_setting_cfg_m0a21.ui")]
            func = self.config_type_M2003_setup 
        elif config_setting_str(ctp) == "M2U51":
            tab_tank = [(self.page_0, "Config 0-2",  "ui/idd_dialog_chip_setting_cfg_m2u51.ui"),
                        (self.page_1, "Config 8-10", "ui/idd_dialog_chip_setting_apwprot.ui")]
            func = self.config_type_M2U51_setup 
        elif config_setting_str(ctp) == "M55M1":
            tab_tank = [(self.page_0, "Config 0-6",  "ui/idd_dialog_chip_setting_cfg_m55m1.ui"),
                        (self.page_1, "Config 8-10", "ui/idd_dialog_chip_setting_apwprot.ui"),
                        (self.page_2, "Config 11-13", "ui/idd_dialog_chip_setting_nscba_lock.ui")]
            func = self.config_type_M55M1_setup
        elif config_setting_str(ctp) == "M251":
            tab_tank = [(self.page_0, "Config 0",  "ui/idd_dialog_chip_setting_cfg_m251.ui")]
            func = self.config_type_M251_setup 
        elif config_setting_str(ctp) == "M258":
            tab_tank = [(self.page_0, "Config 0",  "ui/idd_dialog_chip_setting_cfg_m258.ui")]
            func = self.config_type_M258_setup 
        elif config_setting_str(ctp) == "M031":
            tab_tank = [(self.page_0, "Config 0-2",  "ui/idd_dialog_chip_setting_cfg_m0a21.ui")]
            func = self.config_type_M031_setup 
        elif config_setting_str(ctp) == "M0A21":
            tab_tank = [(self.page_0, "Config 0-2",  "ui/idd_dialog_chip_setting_cfg_m0a21.ui")]
            func = self.config_type_M0A21_setup 
        elif config_setting_str(ctp) == "M030G": 
            tab_tank = [(self.page_0, "Config 0-2",  "ui/idd_dialog_chip_setting_cfg_m0a21.ui")]
            func = self.config_type_M030G_setup
        elif config_setting_str(ctp) == "M451": 
            tab_tank = [(self.page_0, "Config 0-1",  "ui/idd_dialog_chip_setting_cfg_m0a21.ui")]
            func = self.config_type_M451_setup  
        elif config_setting_str(ctp) == "M471": 
            tab_tank = [(self.page_0, "Config 0-2",  "ui/idd_dialog_chip_setting_cfg_m0a21.ui")]
            func = self.config_type_M471_setup 
            
        for page, title, ui_path in tab_tank:
            page = self.widget_from_ui_file(ui_path)
            self.tabs.addTab(page, title)
            self.bind_children(page)
        
        root.addWidget(self.tabs)
        
        if not hasattr(self, 'IDOK'):
            base = QHBoxLayout(self)
            self.IDOK = QPushButton()
            self.IDOK.setText("OK")
            self.IDCANCEL = QPushButton()
            self.IDCANCEL.setText("CANCEL")
            base.addWidget(self.IDOK)
            base.addWidget(self.IDCANCEL)
            root.addLayout(base)
            
        
        if hasattr(self, 'IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT'):
            int_validator = QIntValidator(0, 100, self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT)
            self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.setValidator(int_validator)
        
        self.IDOK.clicked.connect(self.exportFile)
        self.IDCANCEL.clicked.connect(self.close)
        self.get_config()
        
        func()
        
        self.resize(600, 400)
        
    def exportFile(self):
        for i in range(0, 19):
            self.parent.wconfig[i] = self.wconfig[i]
        print("Success")
        self.close()
        
    def add_tab(self, title: str, text: str):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel(text))
        # Example content
        btn_row = QHBoxLayout()
        add_btn = QPushButton("Add another tab")
        add_btn.clicked.connect(lambda: self.add_tab("New", "A freshly created tab."))
        btn_row.addWidget(add_btn)
        btn_row.addStretch()
        layout.addLayout(btn_row)

        # Add to tab widget (with a standard icon just to show how)
        icon = self.style().standardIcon(QStyle.SP_FileIcon)
        index = self.tabs.addTab(page, icon, title)
        self.tabs.setCurrentIndex(index)
        
    def add_plus_tab(self):
        """Adds a trailing '+' tab that, when selected, creates a new tab."""
        dummy = QWidget()  # empty page
        self.tabs.addTab(dummy, "+")
        # keep it disabled-looking: we’ll intercept selection to create a real tab
        self.tabs.setTabEnabled(self.tabs.count() - 1, True)
        
    def widget_from_ui_file(self, path: str):
        f = QFile(path)
        f.open(QFile.ReadOnly)
        try:
            return QUiLoader().load(f)  # returns a QWidget built from the .ui
        finally:
            f.close()
            
    def bind_children(self, widget):
        for child in widget.findChildren(object):
            setattr(self, child.objectName(), child)
            
    def get_config(self):
        for i in range(0, 19):
            self.wconfig[i] = self.parent.config[i] if (self.parent.connect_flag is True) else self.parent.wconfig[i]

        for i in range(0, 19):
            line_edit_name = f'IDC_STATIC_CONFIG_VALUE_{i}'
            if hasattr(self, line_edit_name):
                line_edit = getattr(self, line_edit_name)
                line_edit.setText(f'0x{self.wconfig[i]:08X}')
                
        if hasattr(self, 'IDC_GROUP_BOOT_SELECT'):
            self.IDC_GROUP_BOOT_SELECT.setEnabled(False)

    def updateValue(self, value, cfg_num):
        self.wconfig[cfg_num] = value
        cfg_text = self.wconfig[cfg_num]
        line_edit_name = f'IDC_STATIC_CONFIG_VALUE_{cfg_num}'
        if hasattr(self, line_edit_name):
            line_edit = getattr(self, line_edit_name)
            line_edit.setText(f'0x{cfg_text:08X}')

    def updateBits(self, lsb, val, bits = 1, cfg_num = 0):
        _mask = (1 << bits) - 1
        self.wconfig[cfg_num] &= ~(_mask << lsb)
        self.wconfig[cfg_num] |= ((val &_mask) << lsb)
        cfg_text = self.wconfig[cfg_num]
        line_edit_name = f'IDC_STATIC_CONFIG_VALUE_{cfg_num}'
        if hasattr(self, line_edit_name):
            line_edit = getattr(self, line_edit_name)
            line_edit.setText(f'0x{cfg_text:08X}')

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
        if hasattr(self, 'IDC_RADIO_BOV_3'):
            order_box = [self.IDC_RADIO_BOV_0, self.IDC_RADIO_BOV_1, self.IDC_RADIO_BOV_2, self.IDC_RADIO_BOV_3]
        if hasattr(self, 'IDC_RADIO_BOV_DISABLE'):
            order_box = [self.IDC_RADIO_BOV_DISABLE, self.IDC_RADIO_BOV_0, self.IDC_RADIO_BOV_1, self.IDC_RADIO_BOV_2]
        order_box[0].clicked.connect(lambda: self.updateBits(place, 3, 2, 0))
        order_box[1].clicked.connect(lambda: self.updateBits(place, 2, 2, 0))
        order_box[2].clicked.connect(lambda: self.updateBits(place, 1, 2, 0))
        order_box[3].clicked.connect(lambda: self.updateBits(place, 0, 2, 0))
        order_box[0].setChecked(self.getBits(place, 3, 2, 0))
        order_box[1].setChecked(self.getBits(place, 2, 2, 0))
        order_box[2].setChecked(self.getBits(place, 1, 2, 0))
        order_box[3].setChecked(self.getBits(place, 0, 2, 0))
        
    def radioButton_bw_template_8(self, place):
        self.IDC_RADIO_BOV_0.clicked.connect(lambda: self.updateBits(place, 7, 3, 0))
        self.IDC_RADIO_BOV_1.clicked.connect(lambda: self.updateBits(place, 6, 3, 0))
        self.IDC_RADIO_BOV_2.clicked.connect(lambda: self.updateBits(place, 5, 3, 0))
        self.IDC_RADIO_BOV_3.clicked.connect(lambda: self.updateBits(place, 4, 3, 0))
        self.IDC_RADIO_BOV_4.clicked.connect(lambda: self.updateBits(place, 3, 3, 0))
        self.IDC_RADIO_BOV_5.clicked.connect(lambda: self.updateBits(place, 2, 3, 0))
        self.IDC_RADIO_BOV_6.clicked.connect(lambda: self.updateBits(place, 1, 3, 0))
        self.IDC_RADIO_BOV_7.clicked.connect(lambda: self.updateBits(place, 0, 3, 0))
        self.IDC_RADIO_BOV_0.setChecked(self.getBits(place, 7, 3, 0))
        self.IDC_RADIO_BOV_1.setChecked(self.getBits(place, 6, 3, 0))
        self.IDC_RADIO_BOV_2.setChecked(self.getBits(place, 5, 3, 0))
        self.IDC_RADIO_BOV_3.setChecked(self.getBits(place, 4, 3, 0))
        self.IDC_RADIO_BOV_4.setChecked(self.getBits(place, 3, 3, 0))
        self.IDC_RADIO_BOV_5.setChecked(self.getBits(place, 2, 3, 0))
        self.IDC_RADIO_BOV_6.setChecked(self.getBits(place, 1, 3, 0))
        self.IDC_RADIO_BOV_7.setChecked(self.getBits(place, 0, 3, 0))
        
    def checkBox_bw_0_template(self, place):
        if hasattr(self, 'IDC_CHECK_BROWN_OUT_DETECT'):
            self.IDC_CHECK_BROWN_OUT_DETECT.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_BROWN_OUT_DETECT.isChecked(), place, 0))
            self.IDC_CHECK_BROWN_OUT_DETECT.setChecked(self.getBits(place, 0, 1, 0))
        elif hasattr(self, 'IDC_CHECK_BROWN_OUT_ENABLE'):
            self.IDC_CHECK_BROWN_OUT_ENABLE.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_BROWN_OUT_ENABLE.isChecked(), place, 0))
            self.IDC_CHECK_BROWN_OUT_ENABLE.setChecked(self.getBits(place, 0, 1, 0))
            
    def checkBox_bw_1_template(self, place):
        self.IDC_CHECK_BROWN_OUT_RESET.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_BROWN_OUT_RESET.isChecked(), place, 0))
        self.IDC_CHECK_BROWN_OUT_RESET.setChecked(self.getBits(place, 0, 1, 0))
        
    def checkBox_security_lock_template(self):
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_SECURITY_LOCK.isChecked(), 1, 0))
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        
    def checkBox_ice_lock_template(self, place):
        self.IDC_CHECK_ICE_LOCK.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_ICE_LOCK.isChecked(), place, 0))
        self.IDC_CHECK_ICE_LOCK.setChecked(self.getBits(place, 0, 1, 0))
        
    def radioButton_io_template_2(self, x):
        self.IDC_RADIO_IO_TRI.clicked.connect(lambda: self.updateBits(x, 1, 1, 0))
        self.IDC_RADIO_IO_TRI.setChecked(self.getBits(x, 1, 1, 0))
        if hasattr(self, 'IDC_RADIO_IO_BI'):
            self.IDC_RADIO_IO_BI.clicked.connect(lambda: self.updateBits(x, 0, 1, 0))
            self.IDC_RADIO_IO_BI.setChecked(self.getBits(x, 0, 1, 0))
        elif hasattr(self, 'IDC_RADIO_IO_PO'):
            self.IDC_RADIO_IO_PO.clicked.connect(lambda: self.updateBits(x, 0, 1, 0))
            self.IDC_RADIO_IO_PO.setChecked(self.getBits(x, 0, 1, 0))
            
    def checkBox_dataflash_stateChanged(self):
        self.checkBit(not self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked(), 0, 0)
        self.IDC_SPIN_DATA_FLASH_SIZE.setEnabled(self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked())
        self.updateValue((0xFFFFFFFF if not self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked() else int(1024 * (self.size - self.IDC_SPIN_DATA_FLASH_SIZE.value())) ), 1)
        self.IDC_EDIT_FLASH_BASE_ADDRESS.setText(f'{(0xFFFFFFFF if not self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked() else (int(1024 * (self.size - self.IDC_SPIN_DATA_FLASH_SIZE.value())))):08X}')
        
    def doubleSpinBox_pagesize_template(self):
        self.IDC_CHECK_DATA_FLASH_ENABLE.stateChanged.connect(self.checkBox_dataflash_stateChanged)
        self.IDC_SPIN_DATA_FLASH_SIZE.setEnabled(self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked())
        self.IDC_SPIN_DATA_FLASH_SIZE.setSingleStep(self.page_size)
        self.IDC_SPIN_DATA_FLASH_SIZE.setRange(self.page_size, self.size - self.page_size)
        self.IDC_SPIN_DATA_FLASH_SIZE.valueChanged.connect(lambda: (self.updateValue(int(1024 * (self.size - self.IDC_SPIN_DATA_FLASH_SIZE.value())), 1),
                                                                     self.IDC_EDIT_FLASH_BASE_ADDRESS.setText(f'{(int(1024 * (self.size - self.IDC_SPIN_DATA_FLASH_SIZE.value()))):08X}')))
        self.IDC_SPIN_DATA_FLASH_SIZE.lineEdit().setReadOnly(True)
        self.IDC_EDIT_FLASH_BASE_ADDRESS.setReadOnly(True)
        self.IDC_CHECK_DATA_FLASH_ENABLE.setChecked(self.getBits(0, 0, 1, 0))
        
    def checkBox_watchdog_pwdwn_template(self):
        self.IDC_CHECK_WDT_ENABLE.stateChanged.connect(lambda: (self.IDC_CHECK_WDT_POWER_DOWN.setEnabled(self.IDC_CHECK_WDT_ENABLE.isChecked()),
                                                                self.IDC_CHECK_WDT_POWER_DOWN.setChecked(False) if self.IDC_CHECK_WDT_ENABLE.isEnabled() else None,
                                                                self.checkBit(not self.IDC_CHECK_WDT_ENABLE.isChecked(), 31, 0)))
        self.IDC_CHECK_WDT_POWER_DOWN.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 30, 0))
        self.IDC_CHECK_WDT_ENABLE.setChecked(self.getBits(31, 0, 1, 0))
        self.IDC_CHECK_WDT_POWER_DOWN.setChecked(self.getBits(30, 0, 1, 0) and self.ui.IDC_CHECK_WDT_ENABLE.isChecked())
        
    def radioButton_hxt_template(self):
        self.IDC_RADIO_GPF_CRYSTAL.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
        self.IDC_RADIO_GPF_GPIO.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
        self.IDC_RADIO_GPF_CRYSTAL.setChecked(self.getBits(27, 1, 1, 0))
        self.IDC_RADIO_GPF_GPIO.setChecked(self.getBits(27, 0, 1, 0))
        
    def radioButton_bt_template_2(self):
        if hasattr(self, 'IDC_RADIO_BS_APROM'):
            self.IDC_RADIO_BS_LDROM.setChecked(self.getBits(7, 0, 1, 0))
            self.IDC_RADIO_BS_APROM.setChecked(self.getBits(7, 1, 1, 0))
        elif hasattr(self, 'IDC_RADIO_BS_APROM_LDROM'):
            self.IDC_RADIO_BS_LDROM_APROM.setChecked(self.getBits(7, 0, 1, 0))
            self.IDC_RADIO_BS_APROM_LDROM.setChecked(self.getBits(7, 1, 1, 0))
        
    def radioButton_bt_template_4(self):
        self.IDC_RADIO_BS_LDROM.setChecked(self.getBits(6, 1, 2, 0))
        self.IDC_RADIO_BS_APROM.setChecked(self.getBits(6, 3, 2, 0))
        self.IDC_RADIO_BS_LDROM_APROM.setChecked(self.getBits(6, 0, 2, 0))
        self.IDC_RADIO_BS_APROM_LDROM.setChecked(self.getBits(6, 2, 2, 0))
        
    def secure_conceal_pagesize_template(self):
        self.IDC_CHECK_DATA_FLASH_ENABLE.stateChanged.connect(self.checkBox_dataflash_stateChanged)
        self.IDC_SPIN_DATA_FLASH_SIZE.setEnabled(self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked())
        self.IDC_SPIN_DATA_FLASH_SIZE.setSingleStep(self.page_size)
        self.IDC_SPIN_DATA_FLASH_SIZE.setRange(self.page_size, self.size - self.page_size)
        self.IDC_SPIN_DATA_FLASH_SIZE.valueChanged.connect(lambda: (self.updateValue(int(1024 * (self.size - self.IDC_SPIN_DATA_FLASH_SIZE.value())), 1),
                                                                     self.IDC_EDIT_FLASH_BASE_ADDRESS.setText(f'{(int(1024 * (self.size - self.IDC_SPIN_DATA_FLASH_SIZE.value()))):08X}')))
        self.IDC_SPIN_DATA_FLASH_SIZE.lineEdit().setReadOnly(True)
        self.IDC_EDIT_FLASH_BASE_ADDRESS.setReadOnly(True)
        self.IDC_CHECK_DATA_FLASH_ENABLE.setChecked(self.getBits(0, 0, 1, 0))
        self.IDC_CHECK_SECURE_CONCEAL.stateChanged.connect(self.checkBox_secure_conceal_with_flash_stateChanged)
        self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.setEnabled(self.IDC_CHECK_SECURE_CONCEAL.isChecked())
        self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.setEnabled(self.IDC_CHECK_SECURE_CONCEAL.isChecked())
        self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.editingFinished.connect(self.lineEdit_baddress_editingFinished)
        self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.editingFinished.connect(self.lineEdit_pcount_editingFinished)
        
    def checkBox_secure_conceal_with_flash_stateChanged(self):
        self.IDC_CHECK_DATA_FLASH_ENABLE.setEnabled(not self.IDC_CHECK_SECURE_CONCEAL.isChecked())
        self.IDC_CHECK_DATA_FLASH_ENABLE.setChecked(False if self.IDC_CHECK_SECURE_CONCEAL.isChecked() else self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked())
        self.checkBit(1, 0, 0)
        self.IDC_SPIN_DATA_FLASH_SIZE.setEnabled(False)
        self.updateValue(0xFFFFFFFF, 1)
        self.IDC_EDIT_FLASH_BASE_ADDRESS.setText('0xFFFFFFFF')
        self.checkBox_secure_conceal_stateChanged()
        
    def checkBox_secure_conceal_stateChanged(self):
        self.updateValue((0x55AA5AA5 if self.IDC_CHECK_SECURE_CONCEAL.isChecked() else 0xFFFFFFFF), 6)
        self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.setText(f'{(int((self.size - self.page_size) * 1024) if self.IDC_CHECK_SECURE_CONCEAL.isChecked() else 0xFFFFFFFF):08X}')
        self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.setText(f'{(1 if self.IDC_CHECK_SECURE_CONCEAL.isChecked() else 0)}')
        self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.setEnabled(self.IDC_CHECK_SECURE_CONCEAL.isChecked())
        self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.setEnabled(self.IDC_CHECK_SECURE_CONCEAL.isChecked())
        
    def lineEdit_baddress_editingFinished(self):
        self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.setText(f'{(int(self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.text(), 16) & 0xFFFFF000):08X}')
        self.updateValue((int(self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.text(),16) & 0xFFFFF000), 4)
        self.lineEdit_pcount_editingFinished()

    def lineEdit_pcount_editingFinished(self):
        self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.setText(f'{min(int(self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.text()),(self.size - int(self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.text(), 16) // 1024))}')
        self.updateValue(int(self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.text()), 5)
        
    def lineEdit_security_protect_editingFinished_connect(self):
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.editingFinished.connect(self.lineEdit_security_editingFinished_connect)
        self.IDC_EDIT_FLASH_KEYSTORE_LOCK.editingFinished.connect(self.lineEdit_protect_editingFinished_connect)
        
    def lineEdit_security_editingFinished(self):
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.setText(f'{((int(self.IDC_EDIT_FLASH_ADVANCE_LOCK.text(), base = 16) if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A)& 0x5A):02X}')
        self.updateBits(0,(int(self.IDC_EDIT_FLASH_ADVANCE_LOCK.text(), base = 16) if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A), 8, 2)
        
    def lineEdit_security_editingFinished_connect(self):
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.setText(f'{(int(self.IDC_EDIT_FLASH_ADVANCE_LOCK.text(), 16) & 0x5A) if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A:02X}')
        self.updateBits(0,(int(self.IDC_EDIT_FLASH_KEYSTORE_LOCK.text(), 16) if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A), 8, 2)

    def lineEdit_protect_editingFinished_connect(self):
        self.IDC_EDIT_FLASH_KEYSTORE_LOCK.setText(f'{(int(self.IDC_EDIT_FLASH_KEYSTORE_LOCK.text(), 16) & 0x5A) if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A:02X}')
        self.updateBits(8,(int(self.IDC_EDIT_FLASH_KEYSTORE_LOCK.text(), 16) if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A), 8, 2)
        
    def checkBox_security_lock_stateChanged(self):
        self.checkBit(not self.IDC_CHECK_SECURITY_LOCK.isChecked(), 1, 0)
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.setEnabled(self.IDC_CHECK_SECURITY_LOCK.isChecked())
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.setText(f'{(0x00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A):02X}')
        self.updateBits(0, (0x00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A), 8, 2)
        
    def secure_conceal_pagesize_only_template(self):
        self.IDC_CHECK_SECURE_CONCEAL.stateChanged.connect(self.checkBox_secure_conceal_stateChanged)
        self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.setEnabled(self.IDC_CHECK_SECURE_CONCEAL.isChecked())
        self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.setEnabled(self.IDC_CHECK_SECURE_CONCEAL.isChecked())
        self.IDC_EDIT_SECURE_CONCEAL_BASE_ADDR.editingFinished.connect(self.lineEdit_baddress_editingFinished)
        self.IDC_EDIT_SECURE_CONCEAL_PAGE_COUNT.editingFinished.connect(self.lineEdit_pcount_editingFinished)
        
    def check_secure_region(self, full):
        for i in range (0, 32):
            getattr(self, (f'IDC_CHECK_APROM_WPROT_{i}')).stateChanged.connect(lambda _, i=i: self.checkBit(not getattr(self, (f'IDC_CHECK_APROM_WPROT_{i}')).isChecked(), i, 8))
        if full != 0:
            for i in range (0, 32):
                getattr(self, (f'IDC_CHECK_APROM_WPROT_{i + 32}')).stateChanged.connect(lambda _, i=i: self.checkBit(not getattr(self, (f'IDC_CHECK_APROM_WPROT_{i+32}')).isChecked(), i, 9))
    
    def update_region_address(self):
        raddr = int(self.IDC_EDIT_FLASH_BASE_ADDRESS.text(), 16) & 0x7FFFFFFF
        raddr = int(raddr / 0x2000) * 0x2000
        raddr = raddr if raddr < 0x2FE000 else 0x2FE000
        raddr = raddr if raddr > 0x102000 else 0x102000
        self.IDC_EDIT_FLASH_BASE_ADDRESS.setText(f'{raddr:08X}')
        self.updateValue(raddr, 12)
    
    def config_type_NUC100_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.checkBox_security_lock_template()
        self.doubleSpinBox_pagesize_template()
        self.radioButton_bt_template_2()
        
    def config_type_NUC122_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_2()
        
    def config_type_NUC123AN_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        if hasattr(self, 'IDC_RADIO_GPF_GPIO'):
            self.IDC_RADIO_GPF_GPIO.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
            self.IDC_RADIO_GPF_CRYSTAL.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
            self.IDC_RADIO_GPF_GPIO.setChecked(self.getBits(27, 0, 1, 0))
            self.IDC_RADIO_GPF_CRYSTAL.setChecked(self.getBits(27, 0, 1, 0))
        self.doubleSpinBox_pagesize_template()
        if hasattr(self, 'IDC_CHECK_DATA_FLASH_VAR_SIZE_ENABLE'):
            self.IDC_CHECK_DATA_FLASH_VAR_SIZE_ENABLE.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_DATA_FLASH_VAR_SIZE_ENABLE.isChecked(), 2, 0))
            self.IDC_CHECK_DATA_FLASH_VAR_SIZE_ENABLE.setChecked(self.getBits(2, 0, 1, 0))
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
    def config_type_NUC123AE_setup(self):
        self.config_type_NUC123AN_setup()
        self.IDC_RADIO_IO_TRI.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.IDC_RADIO_IO_BI.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.IDC_RADIO_IO_TRI.setChecked(self.getBits(10, 0, 1, 0))
        self.IDC_RADIO_IO_BI.setChecked(self.getBits(10, 1, 1, 0))
        
    def config_type_NUC200_setup(self):
        self.config_type_NUC123AE_setup()
        self.IDC_RADIO_BOV_0.setText("4.4V")
        self.IDC_RADIO_BOV_1.setText("3.7V")
        self.IDC_GROUP_GPF.setTitle("GPF[1:0] Multi-Function Options")
        
    def config_type_NANO100_setup(self):
        self.radioButton_bw_template_4(19)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        if hasattr(self, 'IDC_CHECK_WDT_ENABLE'):
            self.IDC_CHECK_WDT_ENABLE.stateChanged.connect(lambda: self.checkBit(not self.ui.IDC_CHECK_WDT_ENABLE.isChecked(), 31, 0))
            self.IDC_CHECK_WDT_ENABLE.setChecked(self.getBits(31, 0, 1, 0))
        self.radioButton_bt_template_4()

    def config_type_NANO112_setup(self):
        self.config_type_NANO100_setup()
        
    def config_type_NANO103_setup(self):
        self.IDC_RADIO_BOV_0.clicked.connect(lambda: self.updateBits(19, 15, 4, 0))
        self.IDC_RADIO_BOV_1.clicked.connect(lambda: self.updateBits(19, 13, 4, 0))
        self.IDC_RADIO_BOV_2.clicked.connect(lambda: self.updateBits(19, 12, 4, 0))
        self.IDC_RADIO_BOV_3.clicked.connect(lambda: self.updateBits(19, 11, 4, 0))
        self.IDC_RADIO_BOV_4.clicked.connect(lambda: self.updateBits(19, 10, 4, 0))
        self.IDC_RADIO_BOV_5.clicked.connect(lambda: self.updateBits(19, 9, 4, 0))
        self.IDC_RADIO_BOV_6.clicked.connect(lambda: self.updateBits(19, 8, 4, 0))
        self.IDC_RADIO_BOV_7.clicked.connect(lambda: self.updateBits(19, 7, 4, 0))
        self.IDC_RADIO_BOV_8.clicked.connect(lambda: self.updateBits(19, 6, 4, 0))
        self.IDC_RADIO_BOV_9.clicked.connect(lambda: self.updateBits(19, 5, 4, 0))
        self.IDC_RADIO_BOV_A.clicked.connect(lambda: self.updateBits(19, 4, 4, 0))
        self.IDC_RADIO_BOV_B.clicked.connect(lambda: self.updateBits(19, 3, 4, 0))
        self.IDC_RADIO_BOV_C.clicked.connect(lambda: self.updateBits(19, 2, 4, 0))
        self.IDC_RADIO_BOV_D.clicked.connect(lambda: self.updateBits(19, 1, 4, 0))
        self.IDC_RADIO_BOV_0.setChecked(self.getBits(19, 15, 4, 0))
        self.IDC_RADIO_BOV_1.setChecked(self.getBits(19, 13, 4, 0))
        self.IDC_RADIO_BOV_2.setChecked(self.getBits(19, 12, 4, 0))
        self.IDC_RADIO_BOV_3.setChecked(self.getBits(19, 11, 4, 0))
        self.IDC_RADIO_BOV_4.setChecked(self.getBits(19, 10, 4, 0))
        self.IDC_RADIO_BOV_5.setChecked(self.getBits(19, 9, 4, 0))
        self.IDC_RADIO_BOV_6.setChecked(self.getBits(19, 8, 4, 0))
        self.IDC_RADIO_BOV_7.setChecked(self.getBits(19, 7, 4, 0))
        self.IDC_RADIO_BOV_8.setChecked(self.getBits(19, 6, 4, 0))
        self.IDC_RADIO_BOV_9.setChecked(self.getBits(19, 5, 4, 0))
        self.IDC_RADIO_BOV_A.setChecked(self.getBits(19, 4, 4, 0))
        self.IDC_RADIO_BOV_B.setChecked(self.getBits(19, 3, 4, 0))
        self.IDC_RADIO_BOV_C.setChecked(self.getBits(19, 2, 4, 0))
        self.IDC_RADIO_BOV_D.setChecked(self.getBits(19, 1, 4, 0))
        self.checkBox_bw_0_template(23)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.IDC_CHECK_CLOCK_STOP_DETECT.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_CLOCK_STOP_DETECT.isChecked(), 12, 0))
        self.IDC_CHECK_CLOCK_STOP_DETECT.setChecked(self.getBits(12, 0, 1, 0))
        self.radioButton_bt_template_4()
        
    def config_type_M051A_setup(self):
        self.IDC_RADIO_BOV_0.setText("4.5V")
        self.IDC_RADIO_BOV_1.setText("3.8V")
        self.config_type_M051B_setup()

    def config_type_M051B_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_2()
    
    def config_type_M051D_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_IO_TRI.clicked.connect(lambda: self.updateBits(10, 0, 1, 0))
        self.IDC_RADIO_IO_BI.clicked.connect(lambda: self.updateBits(10, 1, 1, 0))
        self.IDC_RADIO_IO_TRI.setChecked(self.getBits(10, 0, 1, 0))
        self.IDC_RADIO_IO_BI.setChecked(self.getBits(10, 1, 1, 0))
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_2()
        
    def config_type_M058_setup(self):
        self.config_type_M051D_setup()
        self.IDC_RADIO_GPF_GPIO.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
        self.IDC_RADIO_GPF_CRYSTAL.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
        self.IDC_RADIO_GPF_GPIO.setChecked(self.getBits(27, 0, 1, 0))
        self.IDC_RADIO_GPF_CRYSTAL.setChecked(self.getBits(27, 1, 1, 0))
        
    def config_type_MINI51_setup(self):
        self.IDC_RADIO_BOV_1.clicked.connect(lambda: self.updateBits(21, 1, 2, 0))
        self.IDC_RADIO_BOV_0.clicked.connect(lambda: self.updateBits(21, 2, 2, 0))
        self.IDC_RADIO_BOV_DISABLE.clicked.connect(lambda: self.updateBits(21, 3, 2, 0))
        self.IDC_RADIO_BOV_1.setChecked(self.getBits(21, 1, 2, 0) or self.getBits(21, 0, 2, 0))
        self.IDC_RADIO_BOV_0.setChecked(self.getBits(21, 2, 2, 0))
        self.IDC_RADIO_BOV_DISABLE.setChecked(self.getBits(21, 3, 2, 0))
        self.checkBox_bw_1_template(20)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_2()
        
    def config_type_MINI51CN_setup(self):
        self.IDC_RADIO_BOV_0.clicked.connect(lambda: self.updateBits(21, 3, 3, 0))
        self.IDC_RADIO_BOV_1.clicked.connect(lambda: self.updateBits(21, 2, 3, 0))
        self.IDC_RADIO_BOV_2.clicked.connect(lambda: self.updateBits(21, 1, 3, 0))
        self.IDC_RADIO_BOV_3.clicked.connect(lambda: self.updateBits(21, 0, 3, 0))
        self.IDC_RADIO_BOV_DISABLE.clicked.connect(lambda: self.updateBits(21, 7, 3, 0))
        self.IDC_RADIO_BOV_0.setChecked(self.getBits(21, 3, 3, 0))
        self.IDC_RADIO_BOV_1.setChecked(self.getBits(21, 2, 3, 0))
        self.IDC_RADIO_BOV_2.setChecked(self.getBits(21, 1, 3, 0))
        self.IDC_RADIO_BOV_3.setChecked(self.getBits(21, 0, 3, 0))
        self.IDC_RADIO_BOV_DISABLE.setChecked(self.getBits(21, 7, 3, 0))
        self.checkBox_bw_1_template(20)
        self.radioButton_io_template_2(10)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
    def config_type_MINI55_setup(self):
        self.IDC_RADIO_BOV_7.clicked.connect(lambda: self.updateBits(19, 14, 5, 0))
        self.IDC_RADIO_BOV_6.clicked.connect(lambda: self.updateBits(19, 10, 5, 0))
        self.IDC_RADIO_BOV_5.clicked.connect(lambda: self.updateBits(19, 15, 5, 0))
        self.IDC_RADIO_BOV_4.clicked.connect(lambda: self.updateBits(19, 6, 5, 0))
        self.IDC_RADIO_BOV_3.clicked.connect(lambda: self.updateBits(19, 11, 5, 0))
        self.IDC_RADIO_BOV_2.clicked.connect(lambda: self.updateBits(19, 2, 5, 0))
        self.IDC_RADIO_BOV_1.clicked.connect(lambda: self.updateBits(19, 7, 5, 0))
        self.IDC_RADIO_BOV_0.clicked.connect(lambda: self.updateBits(19, 3, 5, 0))
        self.IDC_RADIO_BOV_DISABLE.clicked.connect(lambda: self.updateBits(19, 31, 5, 0))
        self.IDC_RADIO_BOV_7.setChecked(self.getBits(19, 14, 5, 0))
        self.IDC_RADIO_BOV_6.setChecked(self.getBits(19, 10, 5, 0))
        self.IDC_RADIO_BOV_5.setChecked(self.getBits(19, 15, 5, 0))
        self.IDC_RADIO_BOV_4.setChecked(self.getBits(19, 6, 5, 0))
        self.IDC_RADIO_BOV_3.setChecked(self.getBits(19, 11, 5, 0))
        self.IDC_RADIO_BOV_2.setChecked(self.getBits(19, 2, 5, 0))
        self.IDC_RADIO_BOV_1.setChecked(self.getBits(19, 7, 5, 0))
        self.IDC_RADIO_BOV_0.setChecked(self.getBits(19, 3, 5, 0))
        self.IDC_RADIO_BOV_DISABLE.setChecked(self.getBits(19, 31, 5, 0))
        self.checkBox_bw_1_template(20)
        self.radioButton_io_template_2(10)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.IDC_RADIO_RC_44M.clicked.connect(lambda: (self.updateBits(15, 0, 1, 0),
                                                          self.updateBits(27, 1, 1, 0)))
        self.IDC_RADIO_RC_22M.clicked.connect(lambda: (self.updateBits(15, 1, 1, 0),
                                                          self.updateBits(27, 1, 1, 0)))
        self.IDC_RADIO_RC_48M.clicked.connect(lambda: (self.updateBits(15, 0, 1, 0),
                                                          self.updateBits(27, 0, 1, 0)))
        self.IDC_RADIO_RC_24M.clicked.connect(lambda: (self.updateBits(15, 1, 1, 0),
                                                          self.updateBits(27, 0, 1, 0)))
        self.IDC_RADIO_RC_44M.setChecked(self.getBits(15, 0, 1, 0) and self.getBits(27, 1, 1, 0))
        self.IDC_RADIO_RC_22M.setChecked(self.getBits(15, 1, 1, 0) and self.getBits(27, 1, 1, 0))
        self.IDC_RADIO_RC_22M.setChecked(self.getBits(15, 0, 1, 0) and self.getBits(27, 0, 1, 0))
        self.IDC_RADIO_RC_48M.setChecked(self.getBits(15, 1, 1, 0) and self.getBits(27, 0, 1, 0))
        self.radioButton_bt_template_4()
        
    def config_type_NM1500_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.doubleSpinBox_pagesize_template()
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.IDC_CHECK_CHZ_BPWM_Ctrl.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_CHZ_BPWM_Ctrl.isChecked(), 12, 0))
        self.IDC_CHECK_CHZ_BPWM_Ctrl.setChecked(self.getBits(12, 1, 1, 0))
        self.IDC_CHECK_CHZ_Even0_Ctrl.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_CHZ_Even0_Ctrl.isChecked(), 8, 0))
        self.IDC_CHECK_CHZ_Even0_Ctrl.setChecked(self.getBits(8, 1, 1, 0))
        self.IDC_CHECK_CHZ_Odd0_Ctrl.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_CHZ_Even1_Ctrl.isChecked(), 9, 0))
        self.IDC_CHECK_CHZ_Odd0_Ctrl.setChecked(self.getBits(9, 1, 1, 0))
        self.IDC_CHECK_CHZ_Even1_Ctrl.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_CHZ_Odd0_Ctrl.isChecked(), 10, 0))
        self.IDC_CHECK_CHZ_Even1_Ctrl.setChecked(self.getBits(10, 1, 1, 0))
        self.IDC_CHECK_CHZ_Odd1_Ctrl.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_CHZ_Odd1_Ctrl.isChecked(), 11, 0))
        self.IDC_CHECK_CHZ_Odd1_Ctrl.setChecked(self.getBits(11, 1, 1, 0))
        self.radioButton_bt_template_4()
        
    def config_type_NUC400_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.radioButton_io_template_2(10)
        self.IDC_RADIO_GPF_GPIO.clicked.connect(lambda: self.updateBits(27, 0, 1, 0))
        self.IDC_RADIO_GPF_CRYSTAL.clicked.connect(lambda: self.updateBits(27, 1, 1, 0))
        self.IDC_RADIO_GPF_GPIO.setChecked(self.getBits(27, 0, 1, 0))
        self.IDC_RADIO_GPF_CRYSTAL.setChecked(self.getBits(27, 1, 1, 0))
        self.IDC_RADIO_GPG2_GPIO.clicked.connect(lambda: self.updateBits(14, 0, 1, 0))
        self.IDC_RADIO_GPG2_32K.clicked.connect(lambda: self.updateBits(14, 1, 1, 0))
        self.IDC_RADIO_GPG2_GPIO.setChecked(self.getBits(14, 0, 1, 0))
        self.IDC_RADIO_GPG2_32K.setChecked(self.getBits(14, 1, 1, 0))
        self.IDC_RADIO_MII_MODE.clicked.connect(lambda: self.updateBits(15, 0, 1, 0))
        self.IDC_RADIO_RMII_MODE.clicked.connect(lambda: self.updateBits(15, 1, 1, 0))
        self.IDC_RADIO_MII_MODE.setChecked(self.getBits(15, 0, 1, 0))
        self.IDC_RADIO_RMII_MODE.setChecked(self.getBits(15, 1, 1, 0))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_watchdog_pwdwn_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
    
    def config_type_M3331_setup(self):
        self.radioButton_bt_template_2()
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 2, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 1, 1, 0) and self.getBits(3, 2, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_CHECK_ISP_MODE_UART.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_UART.isChecked(), 8, 3))
        self.IDC_CHECK_ISP_MODE_UART.setChecked(self.getBits(8, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_USB.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_ISP_MODE_USB.isChecked(), 9, 3))
        self.IDC_CHECK_ISP_MODE_USB.setChecked(self.getBits(9, 0, 1, 3))
        self.IDC_CHECK_ISP_MODE_CAN.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_CAN.isChecked(), 10, 3))
        self.IDC_CHECK_ISP_MODE_CAN.setChecked(self.getBits(10, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_I2C.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_I2C.isChecked(), 11, 3))
        self.IDC_CHECK_ISP_MODE_I2C.setChecked(self.getBits(11, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_SPI.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_SPI.isChecked(), 12, 3))
        self.IDC_CHECK_ISP_MODE_SPI.setChecked(self.getBits(12, 1, 1, 3))
        self.secure_conceal_pagesize_only_template()
        self.check_secure_region(1)
        self.checkBox_ice_lock_template(11)
        self.IDC_RADIO_APROM_WPROT_LEVEL0.clicked.connect(lambda: (self.updateBits(0, 0xFFFFFFFF, 32, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL1.clicked.connect(lambda: (self.updateBits(0, 0x005A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL2.clicked.connect(lambda: (self.updateBits(0, 0x335A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_LEVEL3.clicked.connect(lambda: (self.updateBits(0, 0x995A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_PIN_A.clicked.connect(lambda: self.updateBits(0, 0xA, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_B.clicked.connect(lambda: self.updateBits(0, 0xB, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_C.clicked.connect(lambda: self.updateBits(0, 0xC, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_D.clicked.connect(lambda: self.updateBits(0, 0xD, 4, 10))
        self.IDC_RADIO_APROM_WPROT_LEVEL0.setChecked(True)
        self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True)
        self.IDC_CHECK_MIRROR_BOUNDARY.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_MIRROR_BOUNDARY.isChecked(), 31, 12))
        self.IDC_CHECK_MIRROR_BOUNDARY.setChecked(self.getBits(31, 1, 1, 12))
        self.IDC_CHECK_DATA_FLASH_ENABLE.setChecked(not self.getBits(0, 0x7FFFFFFF, 31, 12))
        self.IDC_CHECK_DATA_FLASH_ENABLE.stateChanged.connect(lambda: self.IDC_EDIT_FLASH_BASE_ADDRESS.setEnabled(self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked()))
        self.IDC_EDIT_FLASH_BASE_ADDRESS.setEnabled(self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked())
        self.IDC_EDIT_FLASH_BASE_ADDRESS.editingFinished.connect(self.update_region_address)
        self.IDC_CHECK_SECURITYBOOT_LOCK.setChecked(self.getBits(0, 0x5A, 8, 11))
        self.IDC_CHECK_SECURITYBOOT_LOCK.clicked.connect(lambda: self.updateValue((0xFFFFFF5A if self.IDC_CHECK_SECURITYBOOT_LOCK.isChecked() else 0xFFFFFFFF), 11))
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(0, 0x5A, 8, 13))
        self.IDC_CHECK_SECURITY_LOCK.clicked.connect(lambda: self.updateValue((0xFFFFFF5A if self.IDC_CHECK_SECURITYBOOT_LOCK.isChecked() else 0xFFFFFFFF), 13))
        self.IDC_CHECK_LDROM_WPROT_0.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_LDROM_WPROT_0.isChecked(), 0, 16))
        self.IDC_RADIO_LDROM_WPROT_LEVEL0.clicked.connect(lambda: (self.updateBits(0, 0xFFFFFFFF, 32, 17)))
        self.IDC_RADIO_LDROM_WPROT_LEVEL1.clicked.connect(lambda: (self.updateBits(0, 0x005A, 16, 17)))
        self.IDC_RADIO_LDROM_WPROT_LEVEL0.setChecked(True)
        for i in range (0, 4):
            getattr(self, (f'IDC_CHECK_DATAFLASH_WPROT_{i}')).stateChanged.connect(lambda _, i=i: self.checkBit(not getattr(self, (f'IDC_CHECK_DATAFLASH_WPROT_{i}')).isChecked(), i, 18))
        
    def config_type_NM1120_setup(self):
        self.radioButton_bw_template_8(13)
        self.checkBox_bw_0_template(11)
        self.checkBox_bw_1_template(12)
        self.radioButton_io_template_2(10)
        tar = [0, 1, 3]
        self.IDC_COMBO_GPA0_RINI.currentIndexChanged.connect(lambda: self.updateBits(16, tar[self.IDC_COMBO_GPA0_RINI.currentIndex()], 2, 0))
        self.IDC_COMBO_GPA1_RINI.currentIndexChanged.connect(lambda: self.updateBits(18, tar[self.IDC_COMBO_GPA1_RINI.currentIndex()], 2, 0))
        self.IDC_COMBO_GPA2_RINI.currentIndexChanged.connect(lambda: self.updateBits(20, tar[self.IDC_COMBO_GPA2_RINI.currentIndex()], 2, 0))
        self.IDC_COMBO_GPA3_RINI.currentIndexChanged.connect(lambda: self.updateBits(22, tar[self.IDC_COMBO_GPA3_RINI.currentIndex()], 2, 0))
        self.IDC_COMBO_GPA4_RINI.currentIndexChanged.connect(lambda: self.updateBits(24, tar[self.IDC_COMBO_GPA4_RINI.currentIndex()], 2, 0))
        self.IDC_COMBO_GPA5_RINI.currentIndexChanged.connect(lambda: self.updateBits(26, tar[self.IDC_COMBO_GPA5_RINI.currentIndex()], 2, 0))
        self.IDC_COMBO_GPA0_RINI.setCurrentIndex(tar.index(self.getBits(16, 0, 2, 0)))
        self.IDC_COMBO_GPA1_RINI.setCurrentIndex(tar.index(self.getBits(18, 0, 2, 0)))
        self.IDC_COMBO_GPA2_RINI.setCurrentIndex(tar.index(self.getBits(20, 0, 2, 0)))
        self.IDC_COMBO_GPA3_RINI.setCurrentIndex(tar.index(self.getBits(22, 0, 2, 0)))
        self.IDC_COMBO_GPA4_RINI.setCurrentIndex(tar.index(self.getBits(24, 0, 2, 0)))
        self.IDC_COMBO_GPA5_RINI.setCurrentIndex(tar.index(self.getBits(26, 0, 2, 0)))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
    def config_type_M0564_setup(self):
        self.config_type_NUC123AE_setup()
        
    def config_type_NUC1262_setup(self):
        self.config_type_NUC123AE_setup()
        self.checkBox_ice_lock_template(12)
        
    def config_type_M480_setup(self):
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_bt_template_4()
        self.radioButton_hxt_template()
        self.radioButton_io_template_2(10)
        self.IDC_CHECK_BOOT_LOADER.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_BOOT_LOADER.isChecked(), 5, 0))
        self.IDC_CHECK_BOOT_LOADER.setChecked(self.getBits(5, 0, 1, 0))
        self.IDC_RADIO_SPIM_SEL0.clicked.connect(lambda: self.updateBits(4, 0, 2, 3))
        self.IDC_RADIO_SPIM_SEL1.clicked.connect(lambda: self.updateBits(4, 1, 2, 3))
        self.IDC_RADIO_SPIM_SEL2.clicked.connect(lambda: self.updateBits(4, 2, 2, 3))
        self.IDC_RADIO_SPIM_SEL3.clicked.connect(lambda: self.updateBits(4, 3, 2, 3))
        self.IDC_RADIO_SPIM_SEL0.setChecked(self.getBits(4, 0, 2, 3))
        self.IDC_RADIO_SPIM_SEL1.setChecked(self.getBits(4, 1, 2, 3))
        self.IDC_RADIO_SPIM_SEL2.setChecked(self.getBits(4, 2, 2, 3))
        self.IDC_RADIO_SPIM_SEL3.setChecked(self.getBits(4, 3, 2, 3))
        self.IDC_RADIO_UART1_SEL0.clicked.connect(lambda: self.updateBits(0, 0, 2, 3))
        self.IDC_RADIO_UART1_SEL1.clicked.connect(lambda: self.updateBits(0, 1, 2, 3))
        self.IDC_RADIO_UART1_SEL2.clicked.connect(lambda: self.updateBits(0, 2, 2, 3))
        self.IDC_RADIO_UART1_SEL3.clicked.connect(lambda: self.updateBits(0, 3, 2, 3))
        self.IDC_RADIO_UART1_SEL0.setChecked(self.getBits(0, 0, 2, 3))
        self.IDC_RADIO_UART1_SEL1.setChecked(self.getBits(0, 1, 2, 3))
        self.IDC_RADIO_UART1_SEL2.setChecked(self.getBits(0, 2, 2, 3))
        self.IDC_RADIO_UART1_SEL3.setChecked(self.getBits(0, 3, 2, 3))
        self.doubleSpinBox_pagesize_template()
        self.IDC_CHECK_WDT_ENABLE.stateChanged.connect(lambda: (self.IDC_CHECK_WDT_POWER_DOWN.setEnabled(self.IDC_CHECK_WDT_ENABLE.isChecked()),
                                                                self.IDC_CHECK_WDT_POWER_DOWN.setChecked(False) if self.IDC_CHECK_WDT_ENABLE.isEnabled() else None,
                                                                self.checkBit(not self.IDC_CHECK_WDT_ENABLE.isChecked(), 31, 0),
                                                                self.checkBitTwo(not self.IDC_CHECK_WDT_ENABLE.isChecked() or self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 3, 0)))
        self.IDC_CHECK_WDT_POWER_DOWN.stateChanged.connect(lambda: (self.checkBit(not self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 30, 0),
                                                                      self.checkBitTwo(not self.IDC_CHECK_WDT_ENABLE.isChecked() or self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 3, 0)))
        self.IDC_CHECK_WDT_ENABLE.setChecked(self.getBits(31, 0, 1, 0) or self.getBits(3, 0, 2, 0))
        self.IDC_CHECK_WDT_POWER_DOWN.setChecked(self.getBits(30, 0, 1, 0) and self.IDC_CHECK_WDT_ENABLE.isChecked())
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(lambda: (self.checkBit(not self.IDC_CHECK_SECURITY_LOCK.isChecked(), 1, 0),
                                                                     self.updateValue((0xFFFF5A00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0xFFFF5A5A), 2)))
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        self.IDC_SPROM_LOCK_CACHEABLE.stateChanged.connect(lambda: self.checkBit(self.IDC_SPROM_LOCK_CACHEABLE.isChecked(), 12, 0))
        self.IDC_SPROM_LOCK_CACHEABLE.setChecked(self.getBits(12, 0, 1, 0))
        
    def config_type_M480LD_setup(self):
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_bt_template_4()
        self.radioButton_hxt_template()
        self.radioButton_io_template_2(10)
        self.IDC_CHECK_BOOT_LOADER.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_BOOT_LOADER.isChecked(), 5, 0))
        self.IDC_CHECK_BOOT_LOADER.setChecked(self.getBits(5, 0, 1, 0))
        self.doubleSpinBox_pagesize_template()
        self.ui.IDC_CHECK_WDT_ENABLE.stateChanged.connect(lambda: (self.IDC_CHECK_WDT_POWER_DOWN.setEnabled(self.IDC_CHECK_WDT_ENABLE.isChecked()),
                                                                self.IDC_CHECK_WDT_POWER_DOWN.setChecked(False) if self.IDC_CHECK_WDT_ENABLE.isEnabled() else None,
                                                                self.checkBit(not self.IDC_CHECK_WDT_ENABLE.isChecked(), 31, 0),
                                                                self.checkBitTwo(not self.IDC_CHECK_WDT_ENABLE.isChecked() or self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 3, 0)))
        self.IDC_CHECK_WDT_POWER_DOWN.stateChanged.connect(lambda: (self.checkBit(not self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 30, 0),
                                                                      self.checkBitTwo(not self.IDC_CHECK_WDT_ENABLE.isChecked() or self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 3, 0)))
        self.ui.IDC_CHECK_WDT_ENABLE.setChecked(self.getBits(31, 0, 1, 0) or self.getBits(3, 0, 2, 0))
        self.IDC_CHECK_WDT_POWER_DOWN.setChecked(self.getBits(30, 0, 1, 0) and self.IDC_CHECK_WDT_ENABLE.isChecked())
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(lambda: (self.checkBit(not self.IDC_CHECK_SECURITY_LOCK.isChecked(), 1, 0),
                                                                     self.updateBits(0,(0x00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A), 8, 2)))
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        self.IDC_CHECK_SECURITY_BOOT_LOCK.stateChanged.connect(lambda: self.updateBits(8,(0x00 if self.IDC_CHECK_SECURITY_BOOT_LOCK.isChecked() else 0x5A), 8, 2))
        self.IDC_CHECK_SECURITY_BOOT_LOCK.setChecked(self.getBits(8, 0, 8, 2))
        
    def config_type_M460_setup(self):
        self.radioButton_bt_template_2()
        self.radioButton_io_template_2(10)
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.IDC_CHECK_ISP_MODE_UART.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_UART.isChecked(), 8, 3))
        self.IDC_CHECK_ISP_MODE_UART.setChecked(self.getBits(8, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_USB.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_ISP_MODE_USB.isChecked(), 9, 3))
        self.IDC_CHECK_ISP_MODE_USB.setChecked(self.getBits(9, 0, 1, 3))
        self.ui.IDC_CHECK_ISP_MODE_CAN.stateChanged.connect(lambda: self.checkBit(self.ui.IDC_CHECK_ISP_MODE_CAN.isChecked(), 10, 3))
        self.ui.IDC_CHECK_ISP_MODE_CAN.setChecked(self.getBits(10, 1, 1, 3))
        self.ui.IDC_CHECK_ISP_MODE_I2C.stateChanged.connect(lambda: self.checkBit(self.ui.IDC_CHECK_ISP_MODE_I2C.isChecked(), 11, 3))
        self.ui.IDC_CHECK_ISP_MODE_I2C.setChecked(self.getBits(11, 1, 1, 3))
        self.ui.IDC_CHECK_ISP_MODE_SPI.stateChanged.connect(lambda: self.checkBit(self.ui.IDC_CHECK_ISP_MODE_SPI.isChecked(), 12, 3))
        self.ui.IDC_CHECK_ISP_MODE_SPI.setChecked(self.getBits(12, 1, 1, 3))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_ice_lock_template(11)
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(lambda: (self.checkBit(not self.IDC_CHECK_SECURITY_LOCK.isChecked(), 1, 0),
                                                                     self.IDC_EDIT_FLASH_ADVANCE_LOCK.setEnabled(self.IDC_CHECK_SECURITY_LOCK.isChecked()),
                                                                     self.IDC_EDIT_FLASH_KEYSTORE_LOCK.setEnabled(self.IDC_CHECK_SECURITY_LOCK.isChecked()),
                                                                     self.IDC_EDIT_FLASH_ADVANCE_LOCK.setText(f'{(0x00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A):02X}'),
                                                                     self.IDC_EDIT_FLASH_KEYSTORE_LOCK.setText(f'{(0x5A):02X}'),
                                                                     self.updateBits(0, (0x5A00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A5A), 16, 2)))
        self.lineEdit_security_protect_editingFinished_connect()
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))

    def config_type_M2351_setup(self):
        self.radioButton_bt_template_2()
        self.IDC_CHECK_BS_MKROM.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_BS_MKROM.isChecked(), 5, 0))
        self.IDC_CHECK_BS_MKROM.setChecked(self.getBits(5, 0, 1, 0))
        self.radioButton_io_template_2(10)
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_hxt_template()
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.IDC_RADIO_UART1_SEL4.clicked.connect(lambda: self.updateBits(0, 7, 3, 3))
        self.IDC_RADIO_UART1_SEL3.clicked.connect(lambda: self.updateBits(0, 3, 3, 3))
        self.IDC_RADIO_UART1_SEL2.clicked.connect(lambda: self.updateBits(0, 2, 3, 3))
        self.IDC_RADIO_UART1_SEL1.clicked.connect(lambda: self.updateBits(0, 1, 3, 3))
        self.IDC_RADIO_UART1_SEL0.clicked.connect(lambda: self.updateBits(0, 0, 3, 3))
        self.IDC_RADIO_UART1_SEL4.setChecked(self.getBits(0, 7, 3, 3))
        self.IDC_RADIO_UART1_SEL3.setChecked(self.getBits(0, 3, 3, 3))
        self.IDC_RADIO_UART1_SEL2.setChecked(self.getBits(0, 2, 3, 3))
        self.IDC_RADIO_UART1_SEL1.setChecked(self.getBits(0, 1, 3, 3))
        self.IDC_RADIO_UART1_SEL0.setChecked(self.getBits(0, 0, 3, 3))
        self.IDC_CHECK_TAMPER_POWER_DOWN.setVisible(False)
        
    def config_type_M2354_setup(self):
        self.config_type_M2351_setup()
        self.IDC_GROUP_UART1_SELECT.setVisible(False)
        self.IDC_CHECK_TAMPER_POWER_DOWN.setVisible(True)
        self.IDC_CHECK_TAMPER_POWER_DOWN.stateChanged.connect(lambda: self.updateBits(16,(0x5AA5 if self.IDC_CHECK_TAMPER_POWER_DOWN.isChecked() else 0xFFFF), 16, 3))
        self.IDC_CHECK_TAMPER_POWER_DOWN.setChecked(self.getBits(16, 0x5AA5, 16, 3))
        
    def config_type_M2L31_setup(self):
        self.radioButton_bt_template_2()
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_CHECK_ISP_MODE_UART.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_UART.isChecked(), 8, 3))
        self.IDC_CHECK_ISP_MODE_UART.setChecked(self.getBits(8, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_USB.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_ISP_MODE_USB.isChecked(), 9, 3))
        self.IDC_CHECK_ISP_MODE_USB.setChecked(self.getBits(9, 0, 1, 3))
        self.IDC_CHECK_ISP_MODE_CAN.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_CAN.isChecked(), 10, 3))
        self.IDC_CHECK_ISP_MODE_CAN.setChecked(self.getBits(10, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_I2C.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_I2C.isChecked(), 11, 3))
        self.IDC_CHECK_ISP_MODE_I2C.setChecked(self.getBits(11, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_SPI.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_SPI.isChecked(), 12, 3))
        self.IDC_CHECK_ISP_MODE_SPI.setChecked(self.getBits(12, 1, 1, 3))
        self.IDC_RADIO_BLISP_UART_SEL_0.clicked.connect(lambda: self.updateBits(0, 0, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_1.clicked.connect(lambda: self.updateBits(0, 1, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_2.clicked.connect(lambda: self.updateBits(0, 2, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_3.clicked.connect(lambda: self.updateBits(0, 3, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_0.setChecked(self.getBits(0, 0, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_1.setChecked(self.getBits(0, 1, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_2.setChecked(self.getBits(0, 2, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_3.setChecked(self.getBits(0, 3, 2, 3))
        self.secure_conceal_pagesize_template()
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(lambda: (self.checkBit(not self.IDC_CHECK_SECURITY_LOCK.isChecked(), 1, 0),
                                                                     self.IDC_EDIT_FLASH_ADVANCE_LOCK.setEnabled(self.IDC_CHECK_SECURITY_LOCK.isChecked()),
                                                                     self.IDC_EDIT_FLASH_KEYSTORE_LOCK.setEnabled(self.IDC_CHECK_SECURITY_LOCK.isChecked()),
                                                                     self.IDC_EDIT_FLASH_ADVANCE_LOCK.setText(f'{(0x00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A):02X}'),
                                                                     self.IDC_EDIT_FLASH_KEYSTORE_LOCK.setText(f'{(0x5A):02X}'),
                                                                     self.updateBits(0, (0x5A00 if self.IDC_CHECK_SECURITY_LOCK.isChecked() else 0x5A5A), 16, 2)))
        self.lineEdit_security_protect_editingFinished_connect()
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.check_secure_region(1)
        self.checkBox_ice_lock_template(11)
        self.IDC_RADIO_APROM_WPROT_LEVEL0.clicked.connect(lambda: (self.updateBits(0, 0xFFFFFFFF, 32, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL1.clicked.connect(lambda: (self.updateBits(0, 0x005A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL2.clicked.connect(lambda: (self.updateBits(0, 0x335A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_LEVEL3.clicked.connect(lambda: (self.updateBits(0, 0x995A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_PIN_A.clicked.connect(lambda: self.updateBits(0, 0xA, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_B.clicked.connect(lambda: self.updateBits(0, 0xB, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_C.clicked.connect(lambda: self.updateBits(0, 0xC, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_D.clicked.connect(lambda: self.updateBits(0, 0xD, 4, 10))
        self.IDC_RADIO_APROM_WPROT_LEVEL0.setChecked(True)
        self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True)
        
    def config_type_M2A23_setup(self):
        self.radioButton_bt_template_4()
        self.IDC_RADIO_RST_PIN_WIDTH_1.clicked.connect(lambda: self.updateBits(8, 1, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_0.clicked.connect(lambda: self.updateBits(8, 0, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_1.setChecked(self.getBits(8, 1, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_0.setChecked(self.getBits(8, 0, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_1.clicked.connect(lambda: self.updateBits(9, 1, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_0.clicked.connect(lambda: self.updateBits(9, 0, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_1.setChecked(self.getBits(9, 1, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_0.setChecked(self.getBits(9, 0, 1, 0))
        self.radioButton_io_template_2(10)
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_GROUP_RPD.setVisible(False)
        self.IDC_GROUP_GPF.setVisible(False)
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(self.checkBox_security_lock_stateChanged)
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.editingFinished.connect(self.lineEdit_security_editingFinished)
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(12)
        self.check_secure_region(0)
        self.IDC_RADIO_APROM_WPROT_LEVEL0.clicked.connect(lambda: (self.updateBits(0, 0xFFFFFFFF, 32, 10)))
        self.IDC_RADIO_APROM_WPROT_LEVEL1.clicked.connect(lambda: (self.updateBits(0, 0x005A, 16, 10)))
        self.IDC_RADIO_APROM_WPROT_LEVEL2.clicked.connect(lambda: (self.updateBits(0, 0x335A, 16, 10)))
        self.IDC_RADIO_APROM_WPROT_LEVEL3.clicked.connect(lambda: (self.updateBits(0, 0x995A, 16, 10)))
        self.IDC_RADIO_APROM_WPROT_LEVEL0.setChecked(True)
        
    def config_type_M2003_setup(self):
        self.radioButton_bt_template_2()
        self.radioButton_io_template_2(10)
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_IO_TRI.clicked.connect(lambda: self.updateBits(25, 1, 1, 0))
        self.IDC_RADIO_IO_BI.clicked.connect(lambda: self.updateBits(25, 0, 1, 0))
        self.IDC_RADIO_IO_TRI.setChecked(self.getBits(25, 1, 1, 0))
        self.IDC_RADIO_IO_BI.setChecked(self.getBits(25, 0, 1, 0))
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(self.checkBox_security_lock_stateChanged)
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.editingFinished.connect(self.lineEdit_security_editingFinished)
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(12)
        self.IDC_RADIO_BS_APROM_LDROM.setVisible(False)
        self.IDC_RADIO_BS_LDROM_APROM.setVisible(False)
        self.IDC_GROUP_RST_PIN_WIDTH.setVisible(False)
        self.IDC_GROUP_CHIPRESET_TIMEEXT.setVisible(False)
        self.IDC_GROUP_GPF.setVisible(False)
        self.IDC_GROUP_RPD.setTitle("PE.15 Mode Selection")
        self.IDC_RADIO_BOV_3.setText("4.4V")
        self.IDC_RADIO_BOV_2.setText("3.7V")
        self.IDC_RADIO_BOV_1.setText("2.7V")
        self.IDC_RADIO_BOV_0.setText("2.2V")
        self.IDC_GROUP_DATA_FLASH.setVisible(False)
        
    def config_type_M2U51_setup(self):
        self.radioButton_bt_template_2()
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.IDC_RADIO_CWDTCSEL_NORMAL.clicked.connect(lambda: (self.updateBits(28, 1, 1, 0)))
        self.IDC_RADIO_CWDTCSEL_HIGH_ACCURACY.clicked.connect(lambda: (self.updateBits(28, 0, 1, 0)))
        self.IDC_RADIO_CWDTCSEL_NORMAL.setChecked(self.updateBits(28, 1, 1, 0))
        self.IDC_RADIO_CWDTCSEL_HIGH_ACCURACY.setChecked(self.updateBits(28, 0, 1, 0))
        self.doubleSpinBox_pagesize_template()
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(self.checkBox_security_lock_stateChanged)
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.editingFinished.connect(self.lineEdit_security_editingFinished)
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        self.check_secure_region(1)
        self.IDC_RADIO_APROM_WPROT_LEVEL0.clicked.connect(lambda: (self.updateBits(0, 0xFFFFFFFF, 32, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL1.clicked.connect(lambda: (self.updateBits(0, 0x005A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL2.clicked.connect(lambda: (self.updateBits(0, 0x335A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_LEVEL3.clicked.connect(lambda: (self.updateBits(0, 0x995A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_PIN_A.clicked.connect(lambda: self.updateBits(0, 0xA, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_B.clicked.connect(lambda: self.updateBits(0, 0xB, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_C.clicked.connect(lambda: self.updateBits(0, 0xC, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_D.clicked.connect(lambda: self.updateBits(0, 0xD, 4, 10))
        self.IDC_RADIO_APROM_WPROT_LEVEL0.setChecked(True)
        self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True)
        
    def config_type_M55M1_setup(self):
        self.radioButton_bt_template_2()
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_CHECK_ISP_MODE_UART.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_UART.isChecked(), 8, 3))
        self.IDC_CHECK_ISP_MODE_UART.setChecked(self.getBits(8, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_USB.stateChanged.connect(lambda: self.checkBit(not self.IDC_CHECK_ISP_MODE_USB.isChecked(), 9, 3))
        self.IDC_CHECK_ISP_MODE_USB.setChecked(self.getBits(9, 0, 1, 3))
        self.IDC_CHECK_ISP_MODE_CAN.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_CAN.isChecked(), 10, 3))
        self.IDC_CHECK_ISP_MODE_CAN.setChecked(self.getBits(10, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_I2C.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_I2C.isChecked(), 11, 3))
        self.IDC_CHECK_ISP_MODE_I2C.setChecked(self.getBits(11, 1, 1, 3))
        self.IDC_CHECK_ISP_MODE_SPI.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_ISP_MODE_SPI.isChecked(), 12, 3))
        self.IDC_CHECK_ISP_MODE_SPI.setChecked(self.getBits(12, 1, 1, 3))
        self.IDC_RADIO_BLISP_UART_SEL_0.clicked.connect(lambda: self.updateBits(0, 0, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_1.clicked.connect(lambda: self.updateBits(0, 1, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_2.clicked.connect(lambda: self.updateBits(0, 2, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_3.clicked.connect(lambda: self.updateBits(0, 3, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_0.setChecked(self.getBits(0, 0, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_1.setChecked(self.getBits(0, 1, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_2.setChecked(self.getBits(0, 2, 2, 3))
        self.IDC_RADIO_BLISP_UART_SEL_3.setChecked(self.getBits(0, 3, 2, 3))
        self.secure_conceal_pagesize_only_template()
        self.check_secure_region(1)
        self.checkBox_ice_lock_template(11)
        self.IDC_RADIO_APROM_WPROT_LEVEL0.clicked.connect(lambda: (self.updateBits(0, 0xFFFFFFFF, 32, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL1.clicked.connect(lambda: (self.updateBits(0, 0x005A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(False)))
        self.IDC_RADIO_APROM_WPROT_LEVEL2.clicked.connect(lambda: (self.updateBits(0, 0x335A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_LEVEL3.clicked.connect(lambda: (self.updateBits(0, 0x995A, 16, 10),
                                                         self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True),
                                                         self.IDC_GROUP_APROM_WPROT_PIN.setEnabled(True)))
        self.IDC_RADIO_APROM_WPROT_PIN_A.clicked.connect(lambda: self.updateBits(0, 0xA, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_B.clicked.connect(lambda: self.updateBits(0, 0xB, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_C.clicked.connect(lambda: self.updateBits(0, 0xC, 4, 10))
        self.IDC_RADIO_APROM_WPROT_PIN_D.clicked.connect(lambda: self.updateBits(0, 0xD, 4, 10))
        self.IDC_RADIO_APROM_WPROT_LEVEL0.setChecked(True)
        self.IDC_RADIO_APROM_WPROT_PIN_A.setChecked(True)
        #NSCBA
        self.IDC_CHECK_MIRROR_BOUNDARY.stateChanged.connect(lambda: self.checkBit(self.IDC_CHECK_MIRROR_BOUNDARY.isChecked(), 31, 12))
        self.IDC_CHECK_MIRROR_BOUNDARY.setChecked(self.getBits(31, 1, 1, 12))
        self.IDC_CHECK_DATA_FLASH_ENABLE.setChecked(not self.getBits(0, 0x7FFFFFFF, 31, 12))
        self.IDC_CHECK_DATA_FLASH_ENABLE.stateChanged.connect(lambda: self.IDC_EDIT_FLASH_BASE_ADDRESS.setEnabled(self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked()))
        self.IDC_EDIT_FLASH_BASE_ADDRESS.setEnabled(self.IDC_CHECK_DATA_FLASH_ENABLE.isChecked())
        self.IDC_EDIT_FLASH_BASE_ADDRESS.editingFinished.connect(self.update_region_address)
        self.IDC_CHECK_SECURITYBOOT_LOCK.setVisible(False)
        self.IDC_CHECK_SECURITY_LOCK.setVisible(False)
        
    def config_type_M251_setup(self):
        self.radioButton_bw_template_8(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_io_template_2(10)
        self.IDC_CHECK_WDT_ENABLE.stateChanged.connect(lambda: (self.IDC_CHECK_WDT_POWER_DOWN.setEnabled(self.IDC_CHECK_WDT_ENABLE.isChecked()),
                                                                self.IDC_CHECK_WDT_POWER_DOWN.setChecked(False) if self.IDC_CHECK_WDT_ENABLE.isEnabled() else None,
                                                                self.checkBit(not self.IDC_CHECK_WDT_ENABLE.isChecked(), 31, 0),
                                                                self.checkBitTwo(not self.IDC_CHECK_WDT_ENABLE.isChecked() or self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 3, 0)))
        self.IDC_CHECK_WDT_POWER_DOWN.stateChanged.connect(lambda: (self.checkBit(not self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 30, 0),
                                                                      self.checkBitTwo(not self.IDC_CHECK_WDT_ENABLE.isChecked() or self.IDC_CHECK_WDT_POWER_DOWN.isChecked(), 3, 0)))
        self.IDC_CHECK_WDT_ENABLE.setChecked(self.getBits(31, 0, 1, 0) or self.getBits(3, 0, 2, 0))
        self.IDC_CHECK_WDT_POWER_DOWN.setChecked(self.getBits(30, 0, 1, 0) and self.IDC_CHECK_WDT_ENABLE.isChecked())
        self.checkBox_ice_lock_template(12)
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
    def config_type_M258_setup(self):
        self.config_type_M251_setup()
        self.IDC_RADIO_BOOT_CLOCK_SELECT_0.clicked.connect(lambda: self.updateBits(25, 0, 1, 0))
        self.IDC_RADIO_BOOT_CLOCK_SELECT_1.clicked.connect(lambda: self.updateBits(25, 1, 1, 0))
        self.IDC_RADIO_BOOT_CLOCK_SELECT_0.setChecked(self.getBits(25, 0, 1, 0))
        self.IDC_RADIO_BOOT_CLOCK_SELECT_1.setChecked(self.getBits(25, 1, 1, 0))
        
    def config_type_M031_setup(self):
        self.radioButton_bt_template_4()
        self.IDC_RADIO_RST_PIN_WIDTH_1.clicked.connect(lambda: self.updateBits(8, 1, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_0.clicked.connect(lambda: self.updateBits(8, 0, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_1.setChecked(self.getBits(8, 1, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_0.setChecked(self.getBits(8, 0, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_1.clicked.connect(lambda: self.updateBits(9, 1, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_0.clicked.connect(lambda: self.updateBits(9, 0, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_1.setChecked(self.getBits(9, 1, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_0.setChecked(self.getBits(9, 0, 1, 0))
        self.radioButton_io_template_2(10)
        self.IDC_RADIO_BOV_3.clicked.connect(lambda: self.updateBits(21, 1, 1, 0))
        self.IDC_RADIO_BOV_2.clicked.connect(lambda: self.updateBits(21, 0, 1, 0))
        self.IDC_RADIO_BOV_3.setChecked(self.getBits(21, 1, 1, 0))
        self.IDC_RADIO_BOV_2.setChecked(self.getBits(21, 0, 1, 0))
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.radioButton_hxt_template()
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(self.checkBox_security_lock_stateChanged)
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.editingFinished.connect(self.lineEdit_security_editingFinished)
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(12)
        
        self.IDC_GROUP_RPD.setVisible(False)
        self.IDC_RADIO_BOV_1.setVisible(False)
        self.IDC_RADIO_BOV_0.setVisible(False)
        
    def config_type_M0A21_setup(self):
        self.radioButton_bt_template_4()
        self.IDC_RADIO_RST_PIN_WIDTH_1.clicked.connect(lambda: self.updateBits(8, 1, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_0.clicked.connect(lambda: self.updateBits(8, 0, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_1.setChecked(self.getBits(8, 1, 1, 0))
        self.IDC_RADIO_RST_PIN_WIDTH_0.setChecked(self.getBits(8, 0, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_1.clicked.connect(lambda: self.updateBits(9, 1, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_0.clicked.connect(lambda: self.updateBits(9, 0, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_1.setChecked(self.getBits(9, 1, 1, 0))
        self.IDC_RADIO_CHIPRESET_TIMEEXT_0.setChecked(self.getBits(9, 0, 1, 0))
        self.radioButton_io_template_2(10)
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_RPD_RESET.clicked.connect(lambda: self.updateBits(25, 1, 1, 0))
        self.IDC_RADIO_RPD_INPUT.clicked.connect(lambda: self.updateBits(25, 0, 1, 0))
        self.IDC_RADIO_RPD_RESET.setChecked(self.getBits(25, 1, 1, 0))
        self.IDC_RADIO_RPD_INPUT.setChecked(self.getBits(25, 0, 1, 0))
        self.radioButton_hxt_template()
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(self.checkBox_security_lock_stateChanged)
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.editingFinished.connect(self.lineEdit_security_editingFinished)
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(12)
        
    def config_type_M030G_setup(self):
        self.config_type_M031_setup()
        self.IDC_GROUP_BROWN_OUT_VOLTAGE.setVisible(False)
        self.IDC_GROUP_GPF.setVisible(False)
        self.IDC_RADIO_WDT_ENABLE_STOP.setVisible(False)
        
    def config_type_M451_setup(self):
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(23)
        self.checkBox_bw_1_template(20)
        self.radioButton_hxt_template()
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.doubleSpinBox_pagesize_template()
        self.checkBox_security_lock_template()
        self.radioButton_bt_template_4()
        
        self.IDC_GROUP_RST_PIN_WIDTH.setVisible(False)
        self.IDC_GROUP_CHIPRESET_TIMEEXT.setVisible(False)
        self.IDC_GROUP_RPD.setVisible(False)
        self.IDC_RADIO_BOV_3.setText("4.5V")
        self.IDC_RADIO_BOV_2.setText("3.7V")
        self.IDC_RADIO_BOV_1.setText("2.7V")
        self.IDC_RADIO_BOV_0.setText("2.2V")
        self.IDC_STATIC_CONFIG_2.setVisible(False)
        self.IDC_STATIC_CONFIG_VALUE_2.setVisible(False)
        
    def config_type_M471_setup(self):
        self.radioButton_bt_template_4()
        self.radioButton_io_template_2(10)
        self.radioButton_bw_template_4(21)
        self.checkBox_bw_0_template(19)
        self.checkBox_bw_1_template(20)
        self.IDC_RADIO_WDT_DISABLE.clicked.connect(lambda: (self.updateBits(31, 1, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_KEEP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 0, 2, 0)))
        self.IDC_RADIO_WDT_ENABLE_STOP.clicked.connect(lambda: (self.updateBits(31, 0, 1, 0),
                                                           self.updateBits(3, 3, 2, 0)))
        self.IDC_RADIO_WDT_DISABLE.setChecked(self.getBits(31, 1, 1, 0))
        self.IDC_RADIO_WDT_ENABLE_KEEP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 0, 2, 0))
        self.IDC_RADIO_WDT_ENABLE_STOP.setChecked(self.getBits(31, 0, 1, 0) and self.getBits(3, 3, 2, 0))
        self.IDC_CHECK_SECURITY_LOCK.stateChanged.connect(self.checkBox_security_lock_stateChanged)
        self.IDC_EDIT_FLASH_ADVANCE_LOCK.editingFinished.connect(self.lineEdit_security_editingFinished)
        self.IDC_CHECK_SECURITY_LOCK.setChecked(self.getBits(1, 0, 1, 0))
        self.checkBox_ice_lock_template(11)
        
        self.IDC_GROUP_RST_PIN_WIDTH.setVisible(False)
        self.IDC_GROUP_CHIPRESET_TIMEEXT.setVisible(False)
        self.IDC_GROUP_GPF.setVisible(False)
        self.IDC_GROUP_RPD.setVisible(False)
        self.IDC_RADIO_BOV_3.setText("4.5V")
        self.IDC_RADIO_BOV_2.setText("3.7V")
        self.IDC_RADIO_BOV_1.setText("2.7V")
        self.IDC_RADIO_BOV_0.setText("2.4V")
        self.IDC_GROUP_DATA_FLASH.setVisible(False)
