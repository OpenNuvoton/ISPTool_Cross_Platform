# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ISP_Sample.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)
import nuvoton_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 845)
        MainWindow.setMinimumSize(QSize(400, 600))
        MainWindow.setMaximumSize(QSize(10000, 2000))
        MainWindow.setBaseSize(QSize(600, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(400, 600))
        self.centralwidget.setBaseSize(QSize(600, 800))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.comboBox_port = QComboBox(self.groupBox_3)
        self.comboBox_port.setObjectName(u"comboBox_port")

        self.gridLayout.addWidget(self.comboBox_port, 0, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.comboBox_interface = QComboBox(self.groupBox_3)
        self.comboBox_interface.addItem("")
        self.comboBox_interface.addItem("")
        self.comboBox_interface.addItem("")
        self.comboBox_interface.addItem("")
        self.comboBox_interface.addItem("")
        self.comboBox_interface.addItem("")
        self.comboBox_interface.setObjectName(u"comboBox_interface")

        self.gridLayout.addWidget(self.comboBox_interface, 0, 2, 1, 1)

        self.label_DeviceID = QLabel(self.groupBox_3)
        self.label_DeviceID.setObjectName(u"label_DeviceID")
        self.label_DeviceID.setLineWidth(2)

        self.gridLayout.addWidget(self.label_DeviceID, 1, 0, 1, 2)

        self.label_DeviceID_2 = QLabel(self.groupBox_3)
        self.label_DeviceID_2.setObjectName(u"label_DeviceID_2")

        self.gridLayout.addWidget(self.label_DeviceID_2, 1, 2, 1, 3)

        self.label_Size = QLabel(self.groupBox_3)
        self.label_Size.setObjectName(u"label_Size")
        self.label_Size.setLineWidth(2)

        self.gridLayout.addWidget(self.label_Size, 2, 0, 1, 2)

        self.label_Size_2 = QLabel(self.groupBox_3)
        self.label_Size_2.setObjectName(u"label_Size_2")

        self.gridLayout.addWidget(self.label_Size_2, 2, 2, 1, 3)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_Connection = QLabel(self.groupBox_2)
        self.label_Connection.setObjectName(u"label_Connection")

        self.verticalLayout_2.addWidget(self.label_Connection)

        self.btn_Connect = QPushButton(self.groupBox_2)
        self.btn_Connect.setObjectName(u"btn_Connect")

        self.verticalLayout_2.addWidget(self.btn_Connect)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalGroupBox_4 = QGroupBox(self.centralwidget)
        self.verticalGroupBox_4.setObjectName(u"verticalGroupBox_4")
        self.verticalGroupBox_4.setMaximumSize(QSize(16777215, 240))
        self.verticalLayout_6 = QVBoxLayout(self.verticalGroupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalGroupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setIndent(4)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_APROM = QLineEdit(self.verticalGroupBox_4)
        self.lineEdit_APROM.setObjectName(u"lineEdit_APROM")

        self.horizontalLayout.addWidget(self.lineEdit_APROM)

        self.btn_APROM = QPushButton(self.verticalGroupBox_4)
        self.btn_APROM.setObjectName(u"btn_APROM")

        self.horizontalLayout.addWidget(self.btn_APROM)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.verticalGroupBox_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setIndent(4)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_DataFlash = QLineEdit(self.verticalGroupBox_4)
        self.lineEdit_DataFlash.setObjectName(u"lineEdit_DataFlash")

        self.horizontalLayout_2.addWidget(self.lineEdit_DataFlash)

        self.btn_DataFlash = QPushButton(self.verticalGroupBox_4)
        self.btn_DataFlash.setObjectName(u"btn_DataFlash")

        self.horizontalLayout_2.addWidget(self.btn_DataFlash)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalGroupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setIndent(4)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_Config = QPushButton(self.verticalGroupBox_4)
        self.btn_Config.setObjectName(u"btn_Config")

        self.horizontalLayout_3.addWidget(self.btn_Config)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.verticalGroupBox_4)

        self.verticalGroupBox_2 = QGroupBox(self.centralwidget)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        self.verticalGroupBox_2.setMaximumSize(QSize(16777215, 240))
        self.verticalLayout_5 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, -1, 6)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.verticalGroupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setIndent(4)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.radioButton_APROM = QRadioButton(self.verticalGroupBox_2)
        self.radioButton_APROM.setObjectName(u"radioButton_APROM")

        self.horizontalLayout_9.addWidget(self.radioButton_APROM)

        self.radioButton_DataFlash = QRadioButton(self.verticalGroupBox_2)
        self.radioButton_DataFlash.setObjectName(u"radioButton_DataFlash")

        self.horizontalLayout_9.addWidget(self.radioButton_DataFlash)

        self.radioButton_Config = QRadioButton(self.verticalGroupBox_2)
        self.radioButton_Config.setObjectName(u"radioButton_Config")

        self.horizontalLayout_9.addWidget(self.radioButton_Config)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.verticalGroupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setIndent(4)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.checkBox_jump = QCheckBox(self.verticalGroupBox_2)
        self.checkBox_jump.setObjectName(u"checkBox_jump")

        self.horizontalLayout_6.addWidget(self.checkBox_jump)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.btn_Write = QPushButton(self.verticalGroupBox_2)
        self.btn_Write.setObjectName(u"btn_Write")

        self.horizontalLayout_5.addWidget(self.btn_Write)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btn_Erase = QPushButton(self.verticalGroupBox_2)
        self.btn_Erase.setObjectName(u"btn_Erase")

        self.horizontalLayout_5.addWidget(self.btn_Erase)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)

        self.verticalLayout.addWidget(self.verticalGroupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setIndent(4)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_4.addWidget(self.progressBar)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 6)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 4)
        self.verticalLayout.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 18))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.comboBox_interface.setItemText(0, QCoreApplication.translate("MainWindow", u"USB", None))
        self.comboBox_interface.setItemText(1, QCoreApplication.translate("MainWindow", u"UART", None))
        self.comboBox_interface.setItemText(2, QCoreApplication.translate("MainWindow", u"SPI", None))
        self.comboBox_interface.setItemText(3, QCoreApplication.translate("MainWindow", u"I2C", None))
        self.comboBox_interface.setItemText(4, QCoreApplication.translate("MainWindow", u"RS485", None))
        self.comboBox_interface.setItemText(5, QCoreApplication.translate("MainWindow", u"CAN", None))

        self.label_DeviceID.setText(QCoreApplication.translate("MainWindow", u"Device ID: 0xFFFFFFFF", None))
        self.label_DeviceID_2.setText(QCoreApplication.translate("MainWindow", u"Device Name: XXXXXX", None))
        self.label_Size.setText(QCoreApplication.translate("MainWindow", u"APROM Size: 256KB       ", None))
        self.label_Size_2.setText(QCoreApplication.translate("MainWindow", u"Data Flash Size:   0KB", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"ISP Connection", None))
        self.label_Connection.setText(QCoreApplication.translate("MainWindow", u"Status: Disconnected", None))
        self.btn_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.verticalGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"File Input: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"APROM", None))
        self.btn_APROM.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Flash:", None))
        self.btn_DataFlash.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.btn_Config.setText(QCoreApplication.translate("MainWindow", u"Config Setting", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Write Data", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Write Selection:", None))
        self.radioButton_APROM.setText(QCoreApplication.translate("MainWindow", u"APROM", None))
        self.radioButton_DataFlash.setText(QCoreApplication.translate("MainWindow", u"Data Flash", None))
        self.radioButton_Config.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.checkBox_jump.setText(QCoreApplication.translate("MainWindow", u"Jump to APROM", None))
        self.btn_Write.setText(QCoreApplication.translate("MainWindow", u"Start Write", None))
        self.btn_Erase.setText(QCoreApplication.translate("MainWindow", u"Erase All", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Write Progress:", None))
    # retranslateUi

