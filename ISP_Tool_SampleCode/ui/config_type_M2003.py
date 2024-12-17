# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_type_M2003.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(456, 650)
        Dialog.setBaseSize(QSize(600, 720))
#if QT_CONFIG(tooltip)
        Dialog.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.gridLayout_8 = QGridLayout(Dialog)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 442, 636))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridGroupBox_brownout = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_brownout.setObjectName(u"gridGroupBox_brownout")
        self.gridLayout_7 = QGridLayout(self.gridGroupBox_brownout)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radioButton_bw_v_2 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_2.setObjectName(u"radioButton_bw_v_2")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_2, 0, 2, 1, 1)

        self.radioButton_bw_v_1 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_1.setObjectName(u"radioButton_bw_v_1")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_1, 0, 1, 1, 1)

        self.radioButton_bw_v_0 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_0.setObjectName(u"radioButton_bw_v_0")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_0, 0, 0, 1, 1)

        self.checkBox_bw_0 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_0.setObjectName(u"checkBox_bw_0")

        self.gridLayout_7.addWidget(self.checkBox_bw_0, 1, 0, 1, 1)

        self.radioButton_bw_v_3 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_3.setObjectName(u"radioButton_bw_v_3")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_3, 0, 3, 1, 1)

        self.checkBox_bw_1 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_1.setObjectName(u"checkBox_bw_1")

        self.gridLayout_7.addWidget(self.checkBox_bw_1, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_brownout)

        self.gridGroupBox_boot = QGroupBox(self.scrollAreaWidgetContents_2)
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

        self.gridGroupBox_mode = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_mode.setObjectName(u"gridGroupBox_mode")
        self.gridLayout_13 = QGridLayout(self.gridGroupBox_mode)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.radioButton_mode_0 = QRadioButton(self.gridGroupBox_mode)
        self.radioButton_mode_0.setObjectName(u"radioButton_mode_0")

        self.gridLayout_13.addWidget(self.radioButton_mode_0, 0, 0, 1, 1)

        self.radioButton_mode_1 = QRadioButton(self.gridGroupBox_mode)
        self.radioButton_mode_1.setObjectName(u"radioButton_mode_1")

        self.gridLayout_13.addWidget(self.radioButton_mode_1, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_mode)

        self.gridGroupBox_io_state = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_io_state.setObjectName(u"gridGroupBox_io_state")
        self.gridLayout_4 = QGridLayout(self.gridGroupBox_io_state)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_io_0 = QRadioButton(self.gridGroupBox_io_state)
        self.radioButton_io_0.setObjectName(u"radioButton_io_0")

        self.gridLayout_4.addWidget(self.radioButton_io_0, 0, 0, 1, 1)

        self.radioButton_io_1 = QRadioButton(self.gridGroupBox_io_state)
        self.radioButton_io_1.setObjectName(u"radioButton_io_1")

        self.gridLayout_4.addWidget(self.radioButton_io_1, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_io_state)

        self.gridGroupBox_wdt = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_wdt.setObjectName(u"gridGroupBox_wdt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridGroupBox_wdt.sizePolicy().hasHeightForWidth())
        self.gridGroupBox_wdt.setSizePolicy(sizePolicy)
        self.gridLayout_10 = QGridLayout(self.gridGroupBox_wdt)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.radioButton_wdt_0 = QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_0.setObjectName(u"radioButton_wdt_0")

        self.gridLayout_10.addWidget(self.radioButton_wdt_0, 0, 0, 1, 1)

        self.radioButton_wdt_1 = QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_1.setObjectName(u"radioButton_wdt_1")

        self.gridLayout_10.addWidget(self.radioButton_wdt_1, 1, 0, 1, 1)

        self.radioButton_wdt_2 = QRadioButton(self.gridGroupBox_wdt)
        self.radioButton_wdt_2.setObjectName(u"radioButton_wdt_2")

        self.gridLayout_10.addWidget(self.radioButton_wdt_2, 2, 0, 1, 1)

        self.gridLayout_10.setRowStretch(0, 1)
        self.gridLayout_10.setRowStretch(1, 1)
        self.gridLayout_10.setRowStretch(2, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_wdt)

        self.gridGroupBox_misc = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_misc.setObjectName(u"gridGroupBox_misc")
        self.gridLayout_3 = QGridLayout(self.gridGroupBox_misc)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_ice_lock = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_ice_lock.setObjectName(u"checkBox_ice_lock")

        self.gridLayout_3.addWidget(self.checkBox_ice_lock, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridGroupBox_misc)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)

        self.lineEdit_security = QLineEdit(self.gridGroupBox_misc)
        self.lineEdit_security.setObjectName(u"lineEdit_security")

        self.gridLayout_3.addWidget(self.lineEdit_security, 0, 2, 1, 1)

        self.checkBox_security_lock = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_security_lock.setObjectName(u"checkBox_security_lock")

        self.gridLayout_3.addWidget(self.checkBox_security_lock, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridGroupBox_misc)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 4)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_misc)

        self.gridGroupBox_config = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gridGroupBox_config.setObjectName(u"gridGroupBox_config")
        self.gridLayout = QGridLayout(self.gridGroupBox_config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_config0 = QLabel(self.gridGroupBox_config)
        self.label_config0.setObjectName(u"label_config0")

        self.gridLayout.addWidget(self.label_config0, 0, 0, 1, 1)

        self.lineEdit_config0 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config0.setObjectName(u"lineEdit_config0")

        self.gridLayout.addWidget(self.lineEdit_config0, 0, 1, 1, 1)

        self.lineEdit_config2 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config2.setObjectName(u"lineEdit_config2")

        self.gridLayout.addWidget(self.lineEdit_config2, 0, 3, 1, 1)

        self.label_config2 = QLabel(self.gridGroupBox_config)
        self.label_config2.setObjectName(u"label_config2")

        self.gridLayout.addWidget(self.label_config2, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_config)

        self.gridGroupBox_OK = QGroupBox(self.scrollAreaWidgetContents_2)
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

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gridGroupBox_brownout.setTitle(QCoreApplication.translate("Dialog", u"Brown-out Voltage Options", None))
        self.radioButton_bw_v_2.setText(QCoreApplication.translate("Dialog", u"3.3V", None))
        self.radioButton_bw_v_1.setText(QCoreApplication.translate("Dialog", u"3.7V", None))
        self.radioButton_bw_v_0.setText(QCoreApplication.translate("Dialog", u"4.4V", None))
        self.checkBox_bw_0.setText(QCoreApplication.translate("Dialog", u"Brown-out Detector", None))
        self.radioButton_bw_v_3.setText(QCoreApplication.translate("Dialog", u"2.3V", None))
        self.checkBox_bw_1.setText(QCoreApplication.translate("Dialog", u"Brown-out Reset", None))
        self.gridGroupBox_boot.setTitle(QCoreApplication.translate("Dialog", u"Boot Options", None))
        self.radioButton_bt_0_0.setText(QCoreApplication.translate("Dialog", u"LDROM", None))
        self.radioButton_bt_0_1.setText(QCoreApplication.translate("Dialog", u"APROM", None))
        self.gridGroupBox_mode.setTitle(QCoreApplication.translate("Dialog", u"PE.15 Mode Selection", None))
        self.radioButton_mode_0.setText(QCoreApplication.translate("Dialog", u"Reset Mode", None))
        self.radioButton_mode_1.setText(QCoreApplication.translate("Dialog", u"GPIO Mode", None))
        self.gridGroupBox_io_state.setTitle(QCoreApplication.translate("Dialog", u"I/O Initial State Options", None))
        self.radioButton_io_0.setText(QCoreApplication.translate("Dialog", u"Input Tri-state Mode", None))
        self.radioButton_io_1.setText(QCoreApplication.translate("Dialog", u"Quasi-bidirectional Mode", None))
        self.gridGroupBox_wdt.setTitle(QCoreApplication.translate("Dialog", u"Watchdog Timer Mode Selection", None))
        self.radioButton_wdt_0.setText(QCoreApplication.translate("Dialog", u"WDT is inactive.", None))
        self.radioButton_wdt_1.setText(QCoreApplication.translate("Dialog", u"WDT is active and WDT clock is always on.", None))
        self.radioButton_wdt_2.setText(QCoreApplication.translate("Dialog", u"WDT is active and WDT clock is controlled by LIRCEN in power-down.", None))
        self.checkBox_ice_lock.setText(QCoreApplication.translate("Dialog", u"ICE Lock", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Advanced Security Lock: 0x", None))
        self.checkBox_security_lock.setText(QCoreApplication.translate("Dialog", u"Security Lock", None))
        self.label_4.setText("")
        self.gridGroupBox_config.setTitle(QCoreApplication.translate("Dialog", u"Config Value", None))
        self.label_config0.setText(QCoreApplication.translate("Dialog", u"Config 0:", None))
        self.label_config2.setText(QCoreApplication.translate("Dialog", u"Config 2:", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

