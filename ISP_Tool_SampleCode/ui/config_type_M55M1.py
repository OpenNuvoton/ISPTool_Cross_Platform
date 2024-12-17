# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_type_M55M1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(447, 782)
        self.gridLayout_8 = QGridLayout(Dialog)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 415, 733))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridGroupBox_brownout = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_brownout.setObjectName(u"gridGroupBox_brownout")
        self.gridLayout_7 = QGridLayout(self.gridGroupBox_brownout)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radioButton_bw_v_2 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_2.setObjectName(u"radioButton_bw_v_2")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_2, 0, 2, 1, 1)

        self.radioButton_bw_v_1 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_1.setObjectName(u"radioButton_bw_v_1")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_1, 0, 1, 1, 1)

        self.radioButton_bw_v_3 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_3.setObjectName(u"radioButton_bw_v_3")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_3, 0, 3, 1, 1)

        self.radioButton_bw_v_0 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_0.setObjectName(u"radioButton_bw_v_0")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_0, 0, 0, 1, 1)

        self.checkBox_bw_1 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_1.setObjectName(u"checkBox_bw_1")

        self.gridLayout_7.addWidget(self.checkBox_bw_1, 2, 2, 1, 1)

        self.checkBox_bw_0 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_0.setObjectName(u"checkBox_bw_0")

        self.gridLayout_7.addWidget(self.checkBox_bw_0, 2, 0, 1, 1)

        self.radioButton_bw_v_4 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_4.setObjectName(u"radioButton_bw_v_4")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_4, 1, 0, 1, 1)

        self.radioButton_bw_v_5 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_5.setObjectName(u"radioButton_bw_v_5")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_5, 1, 1, 1, 1)

        self.radioButton_bw_v_6 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_6.setObjectName(u"radioButton_bw_v_6")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_6, 1, 2, 1, 1)

        self.radioButton_bw_v_7 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_7.setObjectName(u"radioButton_bw_v_7")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_7, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_brownout)

        self.gridGroupBox_boot = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_boot.setObjectName(u"gridGroupBox_boot")
        self.gridLayout_6 = QGridLayout(self.gridGroupBox_boot)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_bt_0_0 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_0.setObjectName(u"radioButton_bt_0_0")

        self.gridLayout_6.addWidget(self.radioButton_bt_0_0, 0, 0, 1, 1)

        self.radioButton_bt_0_1 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_1.setObjectName(u"radioButton_bt_0_1")

        self.gridLayout_6.addWidget(self.radioButton_bt_0_1, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_boot)

        self.gridGroupBox_isp = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_isp.setObjectName(u"gridGroupBox_isp")
        self.gridLayout_11 = QGridLayout(self.gridGroupBox_isp)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.checkBox_isp_usb = QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_usb.setObjectName(u"checkBox_isp_usb")

        self.gridLayout_11.addWidget(self.checkBox_isp_usb, 1, 1, 1, 1)

        self.checkBox_isp_can = QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_can.setObjectName(u"checkBox_isp_can")

        self.gridLayout_11.addWidget(self.checkBox_isp_can, 1, 0, 1, 1)

        self.checkBox_isp_i2c = QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_i2c.setObjectName(u"checkBox_isp_i2c")

        self.gridLayout_11.addWidget(self.checkBox_isp_i2c, 0, 1, 1, 1)

        self.checkBox_isp_uart = QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_uart.setObjectName(u"checkBox_isp_uart")

        self.gridLayout_11.addWidget(self.checkBox_isp_uart, 0, 0, 1, 1)

        self.checkBox_isp_spi = QCheckBox(self.gridGroupBox_isp)
        self.checkBox_isp_spi.setObjectName(u"checkBox_isp_spi")

        self.gridLayout_11.addWidget(self.checkBox_isp_spi, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_isp)

        self.gridGroupBox_multi_function = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_multi_function.setObjectName(u"gridGroupBox_multi_function")
        self.gridLayout_4 = QGridLayout(self.gridGroupBox_multi_function)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_mf_0 = QRadioButton(self.gridGroupBox_multi_function)
        self.radioButton_mf_0.setObjectName(u"radioButton_mf_0")

        self.gridLayout_4.addWidget(self.radioButton_mf_0, 0, 0, 1, 1)

        self.radioButton_mf_1 = QRadioButton(self.gridGroupBox_multi_function)
        self.radioButton_mf_1.setObjectName(u"radioButton_mf_1")

        self.gridLayout_4.addWidget(self.radioButton_mf_1, 0, 1, 1, 1)

        self.radioButton_mf_2 = QRadioButton(self.gridGroupBox_multi_function)
        self.radioButton_mf_2.setObjectName(u"radioButton_mf_2")

        self.gridLayout_4.addWidget(self.radioButton_mf_2, 1, 0, 1, 1)

        self.radioButton_mf_3 = QRadioButton(self.gridGroupBox_multi_function)
        self.radioButton_mf_3.setObjectName(u"radioButton_mf_3")

        self.gridLayout_4.addWidget(self.radioButton_mf_3, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_multi_function)

        self.gridGroupBox_wdt = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_wdt.setObjectName(u"gridGroupBox_wdt")
        self.gridLayout_10 = QGridLayout(self.gridGroupBox_wdt)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.radioButton_wdt_0 = QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_0.setObjectName(u"radioButton_wdt_0")

        self.gridLayout_10.addWidget(self.radioButton_wdt_0, 0, 0, 1, 1)

        self.radioButton_wdt_1 = QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_1.setObjectName(u"radioButton_wdt_1")

        self.gridLayout_10.addWidget(self.radioButton_wdt_1, 1, 0, 1, 1)

        self.gridLayout_10.setRowStretch(0, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_wdt)

        self.gridGroupBox_misc = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_misc.setObjectName(u"gridGroupBox_misc")
        self.gridLayout_3 = QGridLayout(self.gridGroupBox_misc)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_mirror_boundary = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_mirror_boundary.setObjectName(u"checkBox_mirror_boundary")

        self.gridLayout_3.addWidget(self.checkBox_mirror_boundary, 1, 0, 1, 1)

        self.checkBox_n_region_lock = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_n_region_lock.setObjectName(u"checkBox_n_region_lock")

        self.gridLayout_3.addWidget(self.checkBox_n_region_lock, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridGroupBox_misc)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.lineEdit_n_region_addr = QLineEdit(self.gridGroupBox_misc)
        self.lineEdit_n_region_addr.setObjectName(u"lineEdit_n_region_addr")

        self.gridLayout_3.addWidget(self.lineEdit_n_region_addr, 0, 3, 1, 1)

        self.label_4 = QLabel(self.gridGroupBox_misc)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setColumnStretch(0, 4)

        self.verticalLayout.addWidget(self.gridGroupBox_misc)

        self.gridGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox.setObjectName(u"gridGroupBox")
        self.gridLayout_5 = QGridLayout(self.gridGroupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.checkBox_secure_conceal = QCheckBox(self.gridGroupBox)
        self.checkBox_secure_conceal.setObjectName(u"checkBox_secure_conceal")

        self.gridLayout_5.addWidget(self.checkBox_secure_conceal, 0, 0, 1, 1)

        self.label_9 = QLabel(self.gridGroupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 2, 1, 1)

        self.lineEdit_baddress = QLineEdit(self.gridGroupBox)
        self.lineEdit_baddress.setObjectName(u"lineEdit_baddress")

        self.gridLayout_5.addWidget(self.lineEdit_baddress, 0, 3, 1, 1)

        self.checkBox_ice_lock = QCheckBox(self.gridGroupBox)
        self.checkBox_ice_lock.setObjectName(u"checkBox_ice_lock")

        self.gridLayout_5.addWidget(self.checkBox_ice_lock, 2, 0, 1, 1)

        self.lineEdit_pcount = QLineEdit(self.gridGroupBox)
        self.lineEdit_pcount.setObjectName(u"lineEdit_pcount")

        self.gridLayout_5.addWidget(self.lineEdit_pcount, 1, 3, 1, 1)

        self.label_8 = QLabel(self.gridGroupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_10 = QLabel(self.gridGroupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 1, 1, 1)

        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setColumnStretch(0, 4)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.gridLayout_5.setColumnStretch(3, 2)

        self.verticalLayout.addWidget(self.gridGroupBox)

        self.gridGroupBox_config = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_config.setObjectName(u"gridGroupBox_config")
        self.gridLayout = QGridLayout(self.gridGroupBox_config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_config0 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config0.setObjectName(u"lineEdit_config0")

        self.gridLayout.addWidget(self.lineEdit_config0, 0, 1, 1, 1)

        self.lineEdit_config6 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config6.setObjectName(u"lineEdit_config6")

        self.gridLayout.addWidget(self.lineEdit_config6, 3, 1, 1, 1)

        self.label_config5 = QLabel(self.gridGroupBox_config)
        self.label_config5.setObjectName(u"label_config5")

        self.gridLayout.addWidget(self.label_config5, 2, 2, 1, 1)

        self.lineEdit_config5 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config5.setObjectName(u"lineEdit_config5")

        self.gridLayout.addWidget(self.lineEdit_config5, 2, 3, 1, 1)

        self.label_config6 = QLabel(self.gridGroupBox_config)
        self.label_config6.setObjectName(u"label_config6")

        self.gridLayout.addWidget(self.label_config6, 3, 0, 1, 1)

        self.label_config0 = QLabel(self.gridGroupBox_config)
        self.label_config0.setObjectName(u"label_config0")

        self.gridLayout.addWidget(self.label_config0, 0, 0, 1, 1)

        self.label_config4 = QLabel(self.gridGroupBox_config)
        self.label_config4.setObjectName(u"label_config4")

        self.gridLayout.addWidget(self.label_config4, 2, 0, 1, 1)

        self.lineEdit_config4 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config4.setObjectName(u"lineEdit_config4")

        self.gridLayout.addWidget(self.lineEdit_config4, 2, 1, 1, 1)

        self.lineEdit_config3 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config3.setObjectName(u"lineEdit_config3")

        self.gridLayout.addWidget(self.lineEdit_config3, 0, 3, 1, 1)

        self.label_config3 = QLabel(self.gridGroupBox_config)
        self.label_config3.setObjectName(u"label_config3")

        self.gridLayout.addWidget(self.label_config3, 0, 2, 1, 1)

        self.lineEdit_config12 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config12.setObjectName(u"lineEdit_config12")

        self.gridLayout.addWidget(self.lineEdit_config12, 3, 3, 1, 1)

        self.label_config12 = QLabel(self.gridGroupBox_config)
        self.label_config12.setObjectName(u"label_config12")

        self.gridLayout.addWidget(self.label_config12, 3, 2, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_config)

        self.gridGroupBox_OK = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_OK.setObjectName(u"gridGroupBox_OK")
        self.gridLayout_2 = QGridLayout(self.gridGroupBox_OK)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.pushButton_Cancel = QPushButton(self.gridGroupBox_OK)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.gridLayout_2.addWidget(self.pushButton_Cancel, 0, 3, 1, 1)

        self.pushButton_OK = QPushButton(self.gridGroupBox_OK)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.gridLayout_2.addWidget(self.pushButton_OK, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_OK)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.horizontalLayout_4 = QHBoxLayout(self.tab2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea_2 = QScrollArea(self.tab2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 415, 733))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridLayout_17 = QGridLayout(self.gridWidget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_11 = QLabel(self.gridWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_17.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.gridWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_17.addWidget(self.label_12, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.gridWidget)

        self.gridGroupBox_region = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_region.setObjectName(u"gridGroupBox_region")
        self.gridLayout_12 = QGridLayout(self.gridGroupBox_region)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(1, 1, 1, 1)
        self.checkBox_27 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_27.setObjectName(u"checkBox_27")

        self.gridLayout_12.addWidget(self.checkBox_27, 11, 1, 1, 1)

        self.checkBox_28 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_28.setObjectName(u"checkBox_28")

        self.gridLayout_12.addWidget(self.checkBox_28, 12, 1, 1, 1)

        self.checkBox_29 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_29.setObjectName(u"checkBox_29")

        self.gridLayout_12.addWidget(self.checkBox_29, 13, 1, 1, 1)

        self.checkBox_30 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_30.setObjectName(u"checkBox_30")

        self.gridLayout_12.addWidget(self.checkBox_30, 14, 1, 1, 1)

        self.checkBox_32 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_32.setObjectName(u"checkBox_32")

        self.gridLayout_12.addWidget(self.checkBox_32, 0, 2, 1, 1)

        self.checkBox_31 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_31.setObjectName(u"checkBox_31")

        self.gridLayout_12.addWidget(self.checkBox_31, 15, 1, 1, 1)

        self.checkBox_22 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout_12.addWidget(self.checkBox_22, 6, 1, 1, 1)

        self.checkBox_23 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout_12.addWidget(self.checkBox_23, 7, 1, 1, 1)

        self.checkBox_25 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout_12.addWidget(self.checkBox_25, 9, 1, 1, 1)

        self.checkBox_26 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.gridLayout_12.addWidget(self.checkBox_26, 10, 1, 1, 1)

        self.checkBox_24 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout_12.addWidget(self.checkBox_24, 8, 1, 1, 1)

        self.checkBox_36 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.gridLayout_12.addWidget(self.checkBox_36, 4, 2, 1, 1)

        self.checkBox_39 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.gridLayout_12.addWidget(self.checkBox_39, 7, 2, 1, 1)

        self.checkBox_38 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.gridLayout_12.addWidget(self.checkBox_38, 6, 2, 1, 1)

        self.checkBox_37 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.gridLayout_12.addWidget(self.checkBox_37, 5, 2, 1, 1)

        self.checkBox_42 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_42.setObjectName(u"checkBox_42")

        self.gridLayout_12.addWidget(self.checkBox_42, 10, 2, 1, 1)

        self.checkBox_41 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_41.setObjectName(u"checkBox_41")

        self.gridLayout_12.addWidget(self.checkBox_41, 9, 2, 1, 1)

        self.checkBox_43 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_43.setObjectName(u"checkBox_43")

        self.gridLayout_12.addWidget(self.checkBox_43, 11, 2, 1, 1)

        self.checkBox_40 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.gridLayout_12.addWidget(self.checkBox_40, 8, 2, 1, 1)

        self.checkBox_58 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_58.setObjectName(u"checkBox_58")

        self.gridLayout_12.addWidget(self.checkBox_58, 10, 3, 1, 1)

        self.checkBox_33 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_33.setObjectName(u"checkBox_33")

        self.gridLayout_12.addWidget(self.checkBox_33, 1, 2, 1, 1)

        self.checkBox_61 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_61.setObjectName(u"checkBox_61")

        self.gridLayout_12.addWidget(self.checkBox_61, 13, 3, 1, 1)

        self.checkBox_35 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_35.setObjectName(u"checkBox_35")

        self.gridLayout_12.addWidget(self.checkBox_35, 3, 2, 1, 1)

        self.checkBox_34 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_34.setObjectName(u"checkBox_34")

        self.gridLayout_12.addWidget(self.checkBox_34, 2, 2, 1, 1)

        self.checkBox_19 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout_12.addWidget(self.checkBox_19, 3, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout_12.addWidget(self.checkBox_13, 13, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_12.addWidget(self.checkBox_12, 12, 0, 1, 1)

        self.checkBox_0 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_0.setObjectName(u"checkBox_0")

        self.gridLayout_12.addWidget(self.checkBox_0, 0, 0, 1, 1)

        self.checkBox_20 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout_12.addWidget(self.checkBox_20, 4, 1, 1, 1)

        self.checkBox_21 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout_12.addWidget(self.checkBox_21, 5, 1, 1, 1)

        self.checkBox_56 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_56.setObjectName(u"checkBox_56")

        self.gridLayout_12.addWidget(self.checkBox_56, 8, 3, 1, 1)

        self.checkBox_63 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_63.setObjectName(u"checkBox_63")

        self.gridLayout_12.addWidget(self.checkBox_63, 15, 3, 1, 1)

        self.checkBox_57 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_57.setObjectName(u"checkBox_57")

        self.gridLayout_12.addWidget(self.checkBox_57, 9, 3, 1, 1)

        self.checkBox_55 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_55.setObjectName(u"checkBox_55")

        self.gridLayout_12.addWidget(self.checkBox_55, 7, 3, 1, 1)

        self.checkBox_16 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_12.addWidget(self.checkBox_16, 0, 1, 1, 1)

        self.checkBox_59 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_59.setObjectName(u"checkBox_59")

        self.gridLayout_12.addWidget(self.checkBox_59, 11, 3, 1, 1)

        self.checkBox_8 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_12.addWidget(self.checkBox_8, 8, 0, 1, 1)

        self.checkBox_17 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout_12.addWidget(self.checkBox_17, 1, 1, 1, 1)

        self.checkBox_18 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout_12.addWidget(self.checkBox_18, 2, 1, 1, 1)

        self.checkBox_44 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_44.setObjectName(u"checkBox_44")

        self.gridLayout_12.addWidget(self.checkBox_44, 12, 2, 1, 1)

        self.checkBox_60 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_60.setObjectName(u"checkBox_60")

        self.gridLayout_12.addWidget(self.checkBox_60, 12, 3, 1, 1)

        self.checkBox_62 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_62.setObjectName(u"checkBox_62")

        self.gridLayout_12.addWidget(self.checkBox_62, 14, 3, 1, 1)

        self.checkBox_45 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_45.setObjectName(u"checkBox_45")

        self.gridLayout_12.addWidget(self.checkBox_45, 13, 2, 1, 1)

        self.checkBox_46 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_46.setObjectName(u"checkBox_46")

        self.gridLayout_12.addWidget(self.checkBox_46, 14, 2, 1, 1)

        self.checkBox_47 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_47.setObjectName(u"checkBox_47")

        self.gridLayout_12.addWidget(self.checkBox_47, 15, 2, 1, 1)

        self.checkBox_48 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_48.setObjectName(u"checkBox_48")

        self.gridLayout_12.addWidget(self.checkBox_48, 0, 3, 1, 1)

        self.checkBox_49 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_49.setObjectName(u"checkBox_49")

        self.gridLayout_12.addWidget(self.checkBox_49, 1, 3, 1, 1)

        self.checkBox_50 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_50.setObjectName(u"checkBox_50")

        self.gridLayout_12.addWidget(self.checkBox_50, 2, 3, 1, 1)

        self.checkBox_52 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_52.setObjectName(u"checkBox_52")

        self.gridLayout_12.addWidget(self.checkBox_52, 4, 3, 1, 1)

        self.checkBox_51 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_51.setObjectName(u"checkBox_51")

        self.gridLayout_12.addWidget(self.checkBox_51, 3, 3, 1, 1)

        self.checkBox_53 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_53.setObjectName(u"checkBox_53")

        self.gridLayout_12.addWidget(self.checkBox_53, 5, 3, 1, 1)

        self.checkBox_9 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_12.addWidget(self.checkBox_9, 9, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_12.addWidget(self.checkBox_10, 10, 0, 1, 1)

        self.checkBox_54 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_54.setObjectName(u"checkBox_54")

        self.gridLayout_12.addWidget(self.checkBox_54, 6, 3, 1, 1)

        self.checkBox_11 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_12.addWidget(self.checkBox_11, 11, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_12.addWidget(self.checkBox_7, 7, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_12.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_12.addWidget(self.checkBox_6, 6, 0, 1, 1)

        self.checkBox_1 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.gridLayout_12.addWidget(self.checkBox_1, 1, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_12.addWidget(self.checkBox_3, 3, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_12.addWidget(self.checkBox_4, 4, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_12.addWidget(self.checkBox_5, 5, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_12.addWidget(self.checkBox_15, 15, 0, 1, 1)

        self.checkBox_14 = QCheckBox(self.gridGroupBox_region)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_12.addWidget(self.checkBox_14, 14, 0, 1, 1)

        self.gridLayout_12.setRowStretch(0, 1)
        self.gridLayout_12.setRowStretch(1, 1)
        self.gridLayout_12.setRowStretch(2, 1)
        self.gridLayout_12.setRowStretch(3, 1)
        self.gridLayout_12.setRowStretch(4, 1)
        self.gridLayout_12.setRowStretch(5, 1)
        self.gridLayout_12.setRowStretch(6, 1)
        self.gridLayout_12.setRowStretch(7, 1)
        self.gridLayout_12.setRowStretch(8, 1)
        self.gridLayout_12.setRowStretch(9, 1)
        self.gridLayout_12.setRowStretch(10, 1)
        self.gridLayout_12.setRowStretch(11, 1)
        self.gridLayout_12.setRowStretch(12, 1)
        self.gridLayout_12.setRowStretch(13, 1)
        self.gridLayout_12.setRowStretch(14, 1)
        self.gridLayout_12.setRowStretch(15, 1)
        self.gridLayout_12.setColumnStretch(0, 1)
        self.gridLayout_12.setColumnStretch(1, 1)
        self.gridLayout_12.setColumnStretch(2, 1)
        self.gridLayout_12.setColumnStretch(3, 1)

        self.verticalLayout_2.addWidget(self.gridGroupBox_region)

        self.gridGroupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_2.setObjectName(u"gridGroupBox_2")
        self.gridLayout_14 = QGridLayout(self.gridGroupBox_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.radioButton_lv0 = QRadioButton(self.gridGroupBox_2)
        self.radioButton_lv0.setObjectName(u"radioButton_lv0")

        self.gridLayout_14.addWidget(self.radioButton_lv0, 0, 0, 1, 1)

        self.radioButton_lv1 = QRadioButton(self.gridGroupBox_2)
        self.radioButton_lv1.setObjectName(u"radioButton_lv1")

        self.gridLayout_14.addWidget(self.radioButton_lv1, 0, 1, 1, 1)

        self.radioButton_lv2 = QRadioButton(self.gridGroupBox_2)
        self.radioButton_lv2.setObjectName(u"radioButton_lv2")

        self.gridLayout_14.addWidget(self.radioButton_lv2, 1, 0, 1, 1)

        self.radioButton_lv3 = QRadioButton(self.gridGroupBox_2)
        self.radioButton_lv3.setObjectName(u"radioButton_lv3")

        self.gridLayout_14.addWidget(self.radioButton_lv3, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.gridGroupBox_2)

        self.GroupBox_pin = QGroupBox(self.scrollAreaWidgetContents_2)
        self.GroupBox_pin.setObjectName(u"GroupBox_pin")
        self.GroupBox_pin.setEnabled(True)
        self.gridLayout_15 = QGridLayout(self.GroupBox_pin)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.radioButton_pin0 = QRadioButton(self.GroupBox_pin)
        self.radioButton_pin0.setObjectName(u"radioButton_pin0")

        self.gridLayout_15.addWidget(self.radioButton_pin0, 0, 0, 1, 1)

        self.radioButton_pin1 = QRadioButton(self.GroupBox_pin)
        self.radioButton_pin1.setObjectName(u"radioButton_pin1")

        self.gridLayout_15.addWidget(self.radioButton_pin1, 0, 1, 1, 1)

        self.radioButton_pin2 = QRadioButton(self.GroupBox_pin)
        self.radioButton_pin2.setObjectName(u"radioButton_pin2")

        self.gridLayout_15.addWidget(self.radioButton_pin2, 1, 0, 1, 1)

        self.radioButton_pin3 = QRadioButton(self.GroupBox_pin)
        self.radioButton_pin3.setObjectName(u"radioButton_pin3")

        self.gridLayout_15.addWidget(self.radioButton_pin3, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.GroupBox_pin)

        self.gridGroupBox_4 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_4.setObjectName(u"gridGroupBox_4")
        self.gridLayout_16 = QGridLayout(self.gridGroupBox_4)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_config8 = QLabel(self.gridGroupBox_4)
        self.label_config8.setObjectName(u"label_config8")

        self.gridLayout_16.addWidget(self.label_config8, 0, 0, 1, 1)

        self.lineEdit_config9 = QLineEdit(self.gridGroupBox_4)
        self.lineEdit_config9.setObjectName(u"lineEdit_config9")

        self.gridLayout_16.addWidget(self.lineEdit_config9, 0, 3, 1, 1)

        self.lineEdit_config8 = QLineEdit(self.gridGroupBox_4)
        self.lineEdit_config8.setObjectName(u"lineEdit_config8")

        self.gridLayout_16.addWidget(self.lineEdit_config8, 0, 1, 1, 1)

        self.label_config9 = QLabel(self.gridGroupBox_4)
        self.label_config9.setObjectName(u"label_config9")

        self.gridLayout_16.addWidget(self.label_config9, 0, 2, 1, 1)

        self.label_config10 = QLabel(self.gridGroupBox_4)
        self.label_config10.setObjectName(u"label_config10")

        self.gridLayout_16.addWidget(self.label_config10, 1, 0, 1, 1)

        self.lineEdit_config10 = QLineEdit(self.gridGroupBox_4)
        self.lineEdit_config10.setObjectName(u"lineEdit_config10")

        self.gridLayout_16.addWidget(self.lineEdit_config10, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.gridGroupBox_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_4.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), u"Config 8-10")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gridGroupBox_brownout.setTitle(QCoreApplication.translate("Dialog", u"Brown-out Voltage Options", None))
        self.radioButton_bw_v_2.setText(QCoreApplication.translate("Dialog", u"2.6V", None))
        self.radioButton_bw_v_1.setText(QCoreApplication.translate("Dialog", u"2.8V", None))
        self.radioButton_bw_v_3.setText(QCoreApplication.translate("Dialog", u"2.4V", None))
        self.radioButton_bw_v_0.setText(QCoreApplication.translate("Dialog", u"3.0V", None))
        self.checkBox_bw_1.setText(QCoreApplication.translate("Dialog", u"Brown-out Reset", None))
        self.checkBox_bw_0.setText(QCoreApplication.translate("Dialog", u"Brown-out Detector", None))
        self.radioButton_bw_v_4.setText(QCoreApplication.translate("Dialog", u"2.2V", None))
        self.radioButton_bw_v_5.setText(QCoreApplication.translate("Dialog", u"2.0V", None))
        self.radioButton_bw_v_6.setText(QCoreApplication.translate("Dialog", u"1.8V", None))
        self.radioButton_bw_v_7.setText(QCoreApplication.translate("Dialog", u"1.6V", None))
        self.gridGroupBox_boot.setTitle(QCoreApplication.translate("Dialog", u"Boot Options", None))
        self.radioButton_bt_0_0.setText(QCoreApplication.translate("Dialog", u"LDROM with IAP", None))
        self.radioButton_bt_0_1.setText(QCoreApplication.translate("Dialog", u"APROM with IAP", None))
        self.gridGroupBox_isp.setTitle(QCoreApplication.translate("Dialog", u"Boot Loader ISP Mode", None))
        self.checkBox_isp_usb.setText(QCoreApplication.translate("Dialog", u"USB", None))
        self.checkBox_isp_can.setText(QCoreApplication.translate("Dialog", u"CAN", None))
        self.checkBox_isp_i2c.setText(QCoreApplication.translate("Dialog", u"I2C", None))
        self.checkBox_isp_uart.setText(QCoreApplication.translate("Dialog", u"UART", None))
        self.checkBox_isp_spi.setText(QCoreApplication.translate("Dialog", u"SPI", None))
        self.gridGroupBox_multi_function.setTitle(QCoreApplication.translate("Dialog", u"Boot Loader UART1 TXD/RXD Multi-function Pin Select", None))
        self.radioButton_mf_0.setText(QCoreApplication.translate("Dialog", u"PB.12/PB.13", None))
        self.radioButton_mf_1.setText(QCoreApplication.translate("Dialog", u"PC.11/PC.12", None))
        self.radioButton_mf_2.setText(QCoreApplication.translate("Dialog", u"PA.6/PA.7", None))
        self.radioButton_mf_3.setText(QCoreApplication.translate("Dialog", u"PB.9/PB.8", None))
        self.gridGroupBox_wdt.setTitle(QCoreApplication.translate("Dialog", u"Watchdog Timer Mode Selection", None))
        self.radioButton_wdt_0.setText(QCoreApplication.translate("Dialog", u"WDT is inactive.", None))
        self.radioButton_wdt_1.setText(QCoreApplication.translate("Dialog", u"WDT is active and WDT clock is always on.", None))
        self.gridGroupBox_misc.setTitle(QCoreApplication.translate("Dialog", u"Secure Region Setting", None))
        self.checkBox_mirror_boundary.setText(QCoreApplication.translate("Dialog", u"Mirror Boundary", None))
        self.checkBox_n_region_lock.setText(QCoreApplication.translate("Dialog", u"Non Secure Region Lock", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Non Secure Base Addr", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"0x", None))
        self.gridGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Secure Conceal", None))
        self.checkBox_secure_conceal.setText(QCoreApplication.translate("Dialog", u"Secure Conceal Enable", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"0x", None))
        self.checkBox_ice_lock.setText(QCoreApplication.translate("Dialog", u"ICE Lock", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Base Address", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Page Count", None))
        self.gridGroupBox_config.setTitle(QCoreApplication.translate("Dialog", u"Config Value", None))
        self.label_config5.setText(QCoreApplication.translate("Dialog", u"Config 5:", None))
        self.label_config6.setText(QCoreApplication.translate("Dialog", u"Config 6:", None))
        self.label_config0.setText(QCoreApplication.translate("Dialog", u"Config 0:", None))
        self.label_config4.setText(QCoreApplication.translate("Dialog", u"Config 4:", None))
        self.label_config3.setText(QCoreApplication.translate("Dialog", u"Config 3:", None))
        self.label_config12.setText(QCoreApplication.translate("Dialog", u"Config 12:", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Config 0-6, 12", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Total Region Range: 0x100000 ~ 0x2FFFFF", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Single Region Size: 0x08000", None))
        self.gridGroupBox_region.setTitle(QCoreApplication.translate("Dialog", u"APROM Function Safety Protect", None))
        self.checkBox_27.setText(QCoreApplication.translate("Dialog", u"Region 27", None))
        self.checkBox_28.setText(QCoreApplication.translate("Dialog", u"Region 28", None))
        self.checkBox_29.setText(QCoreApplication.translate("Dialog", u"Region 29", None))
        self.checkBox_30.setText(QCoreApplication.translate("Dialog", u"Region 30", None))
        self.checkBox_32.setText(QCoreApplication.translate("Dialog", u"Region 32", None))
        self.checkBox_31.setText(QCoreApplication.translate("Dialog", u"Region 31", None))
        self.checkBox_22.setText(QCoreApplication.translate("Dialog", u"Region 22", None))
        self.checkBox_23.setText(QCoreApplication.translate("Dialog", u"Region 23", None))
        self.checkBox_25.setText(QCoreApplication.translate("Dialog", u"Region 25", None))
        self.checkBox_26.setText(QCoreApplication.translate("Dialog", u"Region 26", None))
        self.checkBox_24.setText(QCoreApplication.translate("Dialog", u"Region 24", None))
        self.checkBox_36.setText(QCoreApplication.translate("Dialog", u"Region 36", None))
        self.checkBox_39.setText(QCoreApplication.translate("Dialog", u"Region 39", None))
        self.checkBox_38.setText(QCoreApplication.translate("Dialog", u"Region 38", None))
        self.checkBox_37.setText(QCoreApplication.translate("Dialog", u"Region 37", None))
        self.checkBox_42.setText(QCoreApplication.translate("Dialog", u"Region 42", None))
        self.checkBox_41.setText(QCoreApplication.translate("Dialog", u"Region 41", None))
        self.checkBox_43.setText(QCoreApplication.translate("Dialog", u"Region 43", None))
        self.checkBox_40.setText(QCoreApplication.translate("Dialog", u"Region 40", None))
        self.checkBox_58.setText(QCoreApplication.translate("Dialog", u"Region 58", None))
        self.checkBox_33.setText(QCoreApplication.translate("Dialog", u"Region 33", None))
        self.checkBox_61.setText(QCoreApplication.translate("Dialog", u"Region 61", None))
        self.checkBox_35.setText(QCoreApplication.translate("Dialog", u"Region 35", None))
        self.checkBox_34.setText(QCoreApplication.translate("Dialog", u"Region 34", None))
        self.checkBox_19.setText(QCoreApplication.translate("Dialog", u"Region 19", None))
        self.checkBox_13.setText(QCoreApplication.translate("Dialog", u"Region 13", None))
        self.checkBox_12.setText(QCoreApplication.translate("Dialog", u"Region 12", None))
        self.checkBox_0.setText(QCoreApplication.translate("Dialog", u"Region 0", None))
        self.checkBox_20.setText(QCoreApplication.translate("Dialog", u"Region 20", None))
        self.checkBox_21.setText(QCoreApplication.translate("Dialog", u"Region 21", None))
        self.checkBox_56.setText(QCoreApplication.translate("Dialog", u"Region 56", None))
        self.checkBox_63.setText(QCoreApplication.translate("Dialog", u"Region 63", None))
        self.checkBox_57.setText(QCoreApplication.translate("Dialog", u"Region 57", None))
        self.checkBox_55.setText(QCoreApplication.translate("Dialog", u"Region 55", None))
        self.checkBox_16.setText(QCoreApplication.translate("Dialog", u"Region 16", None))
        self.checkBox_59.setText(QCoreApplication.translate("Dialog", u"Region 59", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Region 8", None))
        self.checkBox_17.setText(QCoreApplication.translate("Dialog", u"Region 17", None))
        self.checkBox_18.setText(QCoreApplication.translate("Dialog", u"Region 18", None))
        self.checkBox_44.setText(QCoreApplication.translate("Dialog", u"Region 44", None))
        self.checkBox_60.setText(QCoreApplication.translate("Dialog", u"Region 60", None))
        self.checkBox_62.setText(QCoreApplication.translate("Dialog", u"Region 62", None))
        self.checkBox_45.setText(QCoreApplication.translate("Dialog", u"Region 45", None))
        self.checkBox_46.setText(QCoreApplication.translate("Dialog", u"Region 46", None))
        self.checkBox_47.setText(QCoreApplication.translate("Dialog", u"Region 47", None))
        self.checkBox_48.setText(QCoreApplication.translate("Dialog", u"Region 48", None))
        self.checkBox_49.setText(QCoreApplication.translate("Dialog", u"Region 49", None))
        self.checkBox_50.setText(QCoreApplication.translate("Dialog", u"Region 50", None))
        self.checkBox_52.setText(QCoreApplication.translate("Dialog", u"Region 52", None))
        self.checkBox_51.setText(QCoreApplication.translate("Dialog", u"Region 51", None))
        self.checkBox_53.setText(QCoreApplication.translate("Dialog", u"Region 53", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"Region 9", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"Region 10", None))
        self.checkBox_54.setText(QCoreApplication.translate("Dialog", u"Region 54", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"Region 11", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Region 7", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Region 2", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Region 6", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Region 1", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Region 3", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Region 4", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Region 5", None))
        self.checkBox_15.setText(QCoreApplication.translate("Dialog", u"Region 15", None))
        self.checkBox_14.setText(QCoreApplication.translate("Dialog", u"Region 14", None))
        self.gridGroupBox_2.setTitle(QCoreApplication.translate("Dialog", u"APROM Write Protect One Time Lock Level Selection", None))
        self.radioButton_lv0.setText(QCoreApplication.translate("Dialog", u"Level 0", None))
        self.radioButton_lv1.setText(QCoreApplication.translate("Dialog", u"Level 1", None))
        self.radioButton_lv2.setText(QCoreApplication.translate("Dialog", u"Level 2", None))
        self.radioButton_lv3.setText(QCoreApplication.translate("Dialog", u"Level 3", None))
        self.GroupBox_pin.setTitle(QCoreApplication.translate("Dialog", u"Write Protect Lock Pin Selection", None))
        self.radioButton_pin0.setText(QCoreApplication.translate("Dialog", u"GPB.2", None))
        self.radioButton_pin1.setText(QCoreApplication.translate("Dialog", u"GPA.6", None))
        self.radioButton_pin2.setText(QCoreApplication.translate("Dialog", u"GPC.14", None))
        self.radioButton_pin3.setText(QCoreApplication.translate("Dialog", u"GPD.13", None))
        self.label_config8.setText(QCoreApplication.translate("Dialog", u"Config 8:", None))
        self.label_config9.setText(QCoreApplication.translate("Dialog", u"Config 9:", None))
        self.label_config10.setText(QCoreApplication.translate("Dialog", u"Config 10:", None))
    # retranslateUi

