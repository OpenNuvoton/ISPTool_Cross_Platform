# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_type_M460.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 720)
        Dialog.setBaseSize(QtCore.QSize(600, 720))
        self.gridLayout_8 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 433, 637))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridGroupBox_brownout = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_brownout.setObjectName("gridGroupBox_brownout")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridGroupBox_brownout)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.radioButton_bw_v_2 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_2.setObjectName("radioButton_bw_v_2")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_2, 0, 2, 1, 1)
        self.radioButton_bw_v_1 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_1.setObjectName("radioButton_bw_v_1")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_1, 0, 1, 1, 1)
        self.radioButton_bw_v_3 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_3.setObjectName("radioButton_bw_v_3")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_3, 0, 3, 1, 1)
        self.radioButton_bw_v_0 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_0.setObjectName("radioButton_bw_v_0")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_0, 0, 0, 1, 1)
        self.checkBox_bw_1 = QtWidgets.QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_1.setObjectName("checkBox_bw_1")
        self.gridLayout_7.addWidget(self.checkBox_bw_1, 2, 2, 1, 1)
        self.checkBox_bw_0 = QtWidgets.QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_0.setObjectName("checkBox_bw_0")
        self.gridLayout_7.addWidget(self.checkBox_bw_0, 2, 0, 1, 1)
        self.radioButton_bw_v_4 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_4.setObjectName("radioButton_bw_v_4")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_4, 1, 0, 1, 1)
        self.radioButton_bw_v_5 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_5.setObjectName("radioButton_bw_v_5")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_5, 1, 1, 1, 1)
        self.radioButton_bw_v_6 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_6.setObjectName("radioButton_bw_v_6")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_6, 1, 2, 1, 1)
        self.radioButton_bw_v_7 = QtWidgets.QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_7.setObjectName("radioButton_bw_v_7")
        self.gridLayout_7.addWidget(self.radioButton_bw_v_7, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_brownout)
        self.gridGroupBox_boot = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_boot.setObjectName("gridGroupBox_boot")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridGroupBox_boot)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioButton_bt_0_0 = QtWidgets.QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_0.setObjectName("radioButton_bt_0_0")
        self.gridLayout_6.addWidget(self.radioButton_bt_0_0, 0, 0, 1, 1)
        self.radioButton_bt_0_1 = QtWidgets.QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_1.setObjectName("radioButton_bt_0_1")
        self.gridLayout_6.addWidget(self.radioButton_bt_0_1, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_boot)
        self.gridGroupBox_isp = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_isp.setObjectName("gridGroupBox_isp")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridGroupBox_isp)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.checkBox_isp_usb = QtWidgets.QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_usb.setObjectName("checkBox_isp_usb")
        self.gridLayout_11.addWidget(self.checkBox_isp_usb, 0, 1, 1, 1)
        self.checkBox_isp_i2c = QtWidgets.QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_i2c.setObjectName("checkBox_isp_i2c")
        self.gridLayout_11.addWidget(self.checkBox_isp_i2c, 1, 1, 1, 1)
        self.checkBox_isp_can = QtWidgets.QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_can.setObjectName("checkBox_isp_can")
        self.gridLayout_11.addWidget(self.checkBox_isp_can, 1, 0, 1, 1)
        self.checkBox_isp_uart = QtWidgets.QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_uart.setObjectName("checkBox_isp_uart")
        self.gridLayout_11.addWidget(self.checkBox_isp_uart, 0, 0, 1, 1)
        self.checkBox_isp_spi = QtWidgets.QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_spi.setObjectName("checkBox_isp_spi")
        self.gridLayout_11.addWidget(self.checkBox_isp_spi, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_isp)
        self.gridGroupBox_io_state = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_io_state.setObjectName("gridGroupBox_io_state")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridGroupBox_io_state)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioButton_io_0 = QtWidgets.QRadioButton(self.gridGroupBox_io_state)
        self.radioButton_io_0.setObjectName("radioButton_io_0")
        self.gridLayout_4.addWidget(self.radioButton_io_0, 0, 0, 1, 1)
        self.radioButton_io_1 = QtWidgets.QRadioButton(self.gridGroupBox_io_state)
        self.radioButton_io_1.setObjectName("radioButton_io_1")
        self.gridLayout_4.addWidget(self.radioButton_io_1, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_io_state)
        self.gridGroupBox_wdt = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_wdt.setObjectName("gridGroupBox_wdt")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridGroupBox_wdt)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.radioButton_wdt_0 = QtWidgets.QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_0.setObjectName("radioButton_wdt_0")
        self.gridLayout_10.addWidget(self.radioButton_wdt_0, 0, 0, 1, 1)
        self.radioButton_wdt_1 = QtWidgets.QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_1.setObjectName("radioButton_wdt_1")
        self.gridLayout_10.addWidget(self.radioButton_wdt_1, 1, 0, 1, 1)
        self.radioButton_wdt_2 = QtWidgets.QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_2.setObjectName("radioButton_wdt_2")
        self.gridLayout_10.addWidget(self.radioButton_wdt_2, 2, 0, 1, 1)
        self.gridLayout_10.setRowStretch(0, 1)
        self.gridLayout_10.setRowStretch(1, 1)
        self.gridLayout_10.setRowStretch(2, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_wdt)
        self.gridGroupBox_data_flash = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_data_flash.setObjectName("gridGroupBox_data_flash")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridGroupBox_data_flash)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.doubleSpinBox_pagesize = QtWidgets.QDoubleSpinBox(self.gridGroupBox_data_flash)
        self.doubleSpinBox_pagesize.setObjectName("doubleSpinBox_pagesize")
        self.gridLayout_9.addWidget(self.doubleSpinBox_pagesize, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridGroupBox_data_flash)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit_data_address = QtWidgets.QLineEdit(self.gridGroupBox_data_flash)
        self.lineEdit_data_address.setObjectName("lineEdit_data_address")
        self.gridLayout_9.addWidget(self.lineEdit_data_address, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridGroupBox_data_flash)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridGroupBox_data_flash)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 1, 3, 1, 1)
        self.checkBox_dataflash = QtWidgets.QCheckBox(self.gridGroupBox_data_flash)
        self.checkBox_dataflash.setObjectName("checkBox_dataflash")
        self.gridLayout_9.addWidget(self.checkBox_dataflash, 0, 0, 1, 1)
        self.gridLayout_9.setColumnStretch(0, 4)
        self.gridLayout_9.setColumnStretch(1, 2)
        self.gridLayout_9.setColumnStretch(2, 1)
        self.gridLayout_9.setColumnStretch(3, 1)
        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_data_flash)
        self.gridGroupBox_misc = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_misc.setObjectName("gridGroupBox_misc")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridGroupBox_misc)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.gridGroupBox_misc)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.checkBox_security_lock = QtWidgets.QCheckBox(self.gridGroupBox_misc)
        self.checkBox_security_lock.setObjectName("checkBox_security_lock")
        self.gridLayout_3.addWidget(self.checkBox_security_lock, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridGroupBox_misc)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.lineEdit_security = QtWidgets.QLineEdit(self.gridGroupBox_misc)
        self.lineEdit_security.setObjectName("lineEdit_security")
        self.gridLayout_3.addWidget(self.lineEdit_security, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridGroupBox_misc)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)
        self.checkBox_ice_lock = QtWidgets.QCheckBox(self.gridGroupBox_misc)
        self.checkBox_ice_lock.setObjectName("checkBox_ice_lock")
        self.gridLayout_3.addWidget(self.checkBox_ice_lock, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridGroupBox_misc)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 2, 1, 1)
        self.lineEdit_protect = QtWidgets.QLineEdit(self.gridGroupBox_misc)
        self.lineEdit_protect.setObjectName("lineEdit_protect")
        self.gridLayout_3.addWidget(self.lineEdit_protect, 1, 3, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 4)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_misc)
        self.gridGroupBox_config = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_config.setObjectName("gridGroupBox_config")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox_config)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_config2 = QtWidgets.QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config2.setObjectName("lineEdit_config2")
        self.gridLayout.addWidget(self.lineEdit_config2, 1, 1, 1, 1)
        self.label_config0 = QtWidgets.QLabel(self.gridGroupBox_config)
        self.label_config0.setObjectName("label_config0")
        self.gridLayout.addWidget(self.label_config0, 0, 0, 1, 1)
        self.lineEdit_config0 = QtWidgets.QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config0.setObjectName("lineEdit_config0")
        self.gridLayout.addWidget(self.lineEdit_config0, 0, 1, 1, 1)
        self.lineEdit_config1 = QtWidgets.QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config1.setObjectName("lineEdit_config1")
        self.gridLayout.addWidget(self.lineEdit_config1, 0, 3, 1, 1)
        self.label_config1 = QtWidgets.QLabel(self.gridGroupBox_config)
        self.label_config1.setObjectName("label_config1")
        self.gridLayout.addWidget(self.label_config1, 0, 2, 1, 1)
        self.label_config2 = QtWidgets.QLabel(self.gridGroupBox_config)
        self.label_config2.setObjectName("label_config2")
        self.gridLayout.addWidget(self.label_config2, 1, 0, 1, 1)
        self.label_config3 = QtWidgets.QLabel(self.gridGroupBox_config)
        self.label_config3.setObjectName("label_config3")
        self.gridLayout.addWidget(self.label_config3, 1, 2, 1, 1)
        self.lineEdit_config3 = QtWidgets.QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config3.setObjectName("lineEdit_config3")
        self.gridLayout.addWidget(self.lineEdit_config3, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_config)
        self.gridGroupBox_OK = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_OK.setObjectName("gridGroupBox_OK")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridGroupBox_OK)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.gridGroupBox_OK)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout_2.addWidget(self.pushButton_Cancel, 0, 3, 1, 1)
        self.pushButton_OK = QtWidgets.QPushButton(self.gridGroupBox_OK)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout_2.addWidget(self.pushButton_OK, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox_OK)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gridGroupBox_brownout.setTitle(_translate("Dialog", "Brown-out Voltage Options"))
        self.radioButton_bw_v_2.setText(_translate("Dialog", "2.6V"))
        self.radioButton_bw_v_1.setText(_translate("Dialog", "2.8V"))
        self.radioButton_bw_v_3.setText(_translate("Dialog", "2.4V"))
        self.radioButton_bw_v_0.setText(_translate("Dialog", "3.0V"))
        self.checkBox_bw_1.setText(_translate("Dialog", "Brown-out Reset"))
        self.checkBox_bw_0.setText(_translate("Dialog", "Brown-out Detector"))
        self.radioButton_bw_v_4.setText(_translate("Dialog", "2.2V"))
        self.radioButton_bw_v_5.setText(_translate("Dialog", "2.0V"))
        self.radioButton_bw_v_6.setText(_translate("Dialog", "1.8V"))
        self.radioButton_bw_v_7.setText(_translate("Dialog", "1.6V"))
        self.gridGroupBox_boot.setTitle(_translate("Dialog", "Boot Options"))
        self.radioButton_bt_0_0.setText(_translate("Dialog", "LDROM"))
        self.radioButton_bt_0_1.setText(_translate("Dialog", "APROM"))
        self.gridGroupBox_isp.setTitle(_translate("Dialog", "Boot Loader ISP Mode"))
        self.checkBox_isp_usb.setText(_translate("Dialog", "USB"))
        self.checkBox_isp_i2c.setText(_translate("Dialog", "I2C(PC.0/PC.1)"))
        self.checkBox_isp_can.setText(_translate("Dialog", "CAN(PA.4/PA.5)"))
        self.checkBox_isp_uart.setText(_translate("Dialog", "UART(PB.12/PB.13)"))
        self.checkBox_isp_spi.setText(_translate("Dialog", "SPI"))
        self.gridGroupBox_io_state.setTitle(_translate("Dialog", "I/O Initial State Options"))
        self.radioButton_io_0.setText(_translate("Dialog", "Input Tri-state Mode"))
        self.radioButton_io_1.setText(_translate("Dialog", "Quasi-bidirectional Mode"))
        self.gridGroupBox_wdt.setTitle(_translate("Dialog", "Watchdog Timer Mode Selection"))
        self.radioButton_wdt_0.setText(_translate("Dialog", "WDT is inactive."))
        self.radioButton_wdt_1.setText(_translate("Dialog", "WDT is active and WDT clock is always on."))
        self.radioButton_wdt_2.setText(_translate("Dialog", "WDT is active and WDT clock is controlled by LIRCEN in power-down."))
        self.gridGroupBox_data_flash.setTitle(_translate("Dialog", "Data Flash Options"))
        self.label.setText(_translate("Dialog", "Base Address: 0x"))
        self.label_2.setText(_translate("Dialog", "Data Flash Size:"))
        self.label_3.setText(_translate("Dialog", "K"))
        self.checkBox_dataflash.setText(_translate("Dialog", "Data Flash"))
        self.label_6.setText(_translate("Dialog", "0x"))
        self.checkBox_security_lock.setText(_translate("Dialog", "Security Lock"))
        self.label_5.setText(_translate("Dialog", "Advanced Security Lock:"))
        self.label_7.setText(_translate("Dialog", "Key Store Protect Lock:"))
        self.checkBox_ice_lock.setText(_translate("Dialog", "ICE Lock"))
        self.label_4.setText(_translate("Dialog", "0x"))
        self.gridGroupBox_config.setTitle(_translate("Dialog", "Config Value"))
        self.label_config0.setText(_translate("Dialog", "Config 0:"))
        self.label_config1.setText(_translate("Dialog", "Config 1:"))
        self.label_config2.setText(_translate("Dialog", "Config 2:"))
        self.label_config3.setText(_translate("Dialog", "Config 3:"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_OK.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
