# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_type_NM1500.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(442, 419)
        Dialog.setBaseSize(QSize(600, 720))
        self.gridLayout_8 = QGridLayout(Dialog)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setBaseSize(QSize(600, 720))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 428, 405))
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
        self.radioButton_bw_v_1 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_1.setObjectName(u"radioButton_bw_v_1")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_1, 0, 1, 1, 1)

        self.radioButton_bw_v_2 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_2.setObjectName(u"radioButton_bw_v_2")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_2, 0, 2, 1, 1)

        self.radioButton_bw_v_0 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_0.setObjectName(u"radioButton_bw_v_0")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_0, 0, 0, 1, 1)

        self.radioButton_bw_v_3 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_3.setObjectName(u"radioButton_bw_v_3")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_3, 0, 3, 1, 1)

        self.checkBox_bw_0 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_0.setObjectName(u"checkBox_bw_0")

        self.gridLayout_7.addWidget(self.checkBox_bw_0, 1, 0, 1, 1)

        self.checkBox_bw_1 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_1.setObjectName(u"checkBox_bw_1")

        self.gridLayout_7.addWidget(self.checkBox_bw_1, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_brownout)

        self.gridGroupBox_boot = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_boot.setObjectName(u"gridGroupBox_boot")
        self.gridLayout_6 = QGridLayout(self.gridGroupBox_boot)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_bt_0_0 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_0.setObjectName(u"radioButton_bt_0_0")

        self.gridLayout_6.addWidget(self.radioButton_bt_0_0, 0, 0, 1, 1)

        self.radioButton_bt_1_0 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_1_0.setObjectName(u"radioButton_bt_1_0")

        self.gridLayout_6.addWidget(self.radioButton_bt_1_0, 1, 0, 1, 1)

        self.radioButton_bt_0_1 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_1.setObjectName(u"radioButton_bt_0_1")

        self.gridLayout_6.addWidget(self.radioButton_bt_0_1, 0, 1, 1, 1)

        self.radioButton_bt_1_1 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_1_1.setObjectName(u"radioButton_bt_1_1")

        self.gridLayout_6.addWidget(self.radioButton_bt_1_1, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_boot)

        self.gridGroupBox_data_flash = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_data_flash.setObjectName(u"gridGroupBox_data_flash")
        self.gridLayout_9 = QGridLayout(self.gridGroupBox_data_flash)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.doubleSpinBox_pagesize = QDoubleSpinBox(self.gridGroupBox_data_flash)
        self.doubleSpinBox_pagesize.setObjectName(u"doubleSpinBox_pagesize")

        self.gridLayout_9.addWidget(self.doubleSpinBox_pagesize, 1, 2, 1, 1)

        self.label = QLabel(self.gridGroupBox_data_flash)
        self.label.setObjectName(u"label")

        self.gridLayout_9.addWidget(self.label, 0, 1, 1, 1)

        self.lineEdit_data_address = QLineEdit(self.gridGroupBox_data_flash)
        self.lineEdit_data_address.setObjectName(u"lineEdit_data_address")

        self.gridLayout_9.addWidget(self.lineEdit_data_address, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gridGroupBox_data_flash)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_9.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridGroupBox_data_flash)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_9.addWidget(self.label_3, 1, 3, 1, 1)

        self.checkBox_dataflash = QCheckBox(self.gridGroupBox_data_flash)
        self.checkBox_dataflash.setObjectName(u"checkBox_dataflash")

        self.gridLayout_9.addWidget(self.checkBox_dataflash, 0, 0, 1, 1)

        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 1)
        self.gridLayout_9.setColumnStretch(0, 4)
        self.gridLayout_9.setColumnStretch(1, 2)
        self.gridLayout_9.setColumnStretch(2, 1)
        self.gridLayout_9.setColumnStretch(3, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_data_flash)

        self.gridGroupBox_pwm = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_pwm.setObjectName(u"gridGroupBox_pwm")
        self.gridLayout_pwm = QGridLayout(self.gridGroupBox_pwm)
        self.gridLayout_pwm.setObjectName(u"gridLayout_pwm")
        self.checkBox = QCheckBox(self.gridGroupBox_pwm)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_pwm.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridGroupBox_pwm)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_pwm.addWidget(self.checkBox_3, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridGroupBox_pwm)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_pwm.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridGroupBox_pwm)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_pwm.addWidget(self.checkBox_4, 2, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridGroupBox_pwm)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_pwm.addWidget(self.checkBox_5, 2, 1, 1, 1)

        self.gridLayout_pwm.setRowStretch(0, 1)
        self.gridLayout_pwm.setRowStretch(1, 1)
        self.gridLayout_pwm.setRowStretch(2, 1)
        self.gridLayout_pwm.setColumnStretch(0, 1)
        self.gridLayout_pwm.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_pwm)

        self.gridGroupBox_misc = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_misc.setObjectName(u"gridGroupBox_misc")
        self.gridLayout_3 = QGridLayout(self.gridGroupBox_misc)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_watchdog_pwdwn = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_watchdog_pwdwn.setObjectName(u"checkBox_watchdog_pwdwn")

        self.gridLayout_3.addWidget(self.checkBox_watchdog_pwdwn, 0, 1, 1, 1)

        self.checkBox_security_lock = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_security_lock.setObjectName(u"checkBox_security_lock")

        self.gridLayout_3.addWidget(self.checkBox_security_lock, 1, 0, 1, 1)

        self.checkBox_watchdog = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_watchdog.setObjectName(u"checkBox_watchdog")

        self.gridLayout_3.addWidget(self.checkBox_watchdog, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_misc)

        self.gridGroupBox_config = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_config.setObjectName(u"gridGroupBox_config")
        self.gridLayout = QGridLayout(self.gridGroupBox_config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_config0 = QLabel(self.gridGroupBox_config)
        self.label_config0.setObjectName(u"label_config0")

        self.gridLayout.addWidget(self.label_config0, 0, 0, 1, 1)

        self.lineEdit_config0 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config0.setObjectName(u"lineEdit_config0")

        self.gridLayout.addWidget(self.lineEdit_config0, 0, 1, 1, 1)

        self.label_config1 = QLabel(self.gridGroupBox_config)
        self.label_config1.setObjectName(u"label_config1")

        self.gridLayout.addWidget(self.label_config1, 0, 2, 1, 1)

        self.lineEdit_config1 = QLineEdit(self.gridGroupBox_config)
        self.lineEdit_config1.setObjectName(u"lineEdit_config1")

        self.gridLayout.addWidget(self.lineEdit_config1, 0, 3, 1, 1)


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
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gridGroupBox_brownout.setTitle(QCoreApplication.translate("Dialog", u"Brown-out Voltage Options", None))
        self.radioButton_bw_v_1.setText(QCoreApplication.translate("Dialog", u"3.7V", None))
        self.radioButton_bw_v_2.setText(QCoreApplication.translate("Dialog", u"2.7V", None))
        self.radioButton_bw_v_0.setText(QCoreApplication.translate("Dialog", u"4.4V", None))
        self.radioButton_bw_v_3.setText(QCoreApplication.translate("Dialog", u"2.2V", None))
        self.checkBox_bw_0.setText(QCoreApplication.translate("Dialog", u"Brown-out Detector", None))
        self.checkBox_bw_1.setText(QCoreApplication.translate("Dialog", u"Brown-out Reset", None))
        self.gridGroupBox_boot.setTitle(QCoreApplication.translate("Dialog", u"Boot Options", None))
        self.radioButton_bt_0_0.setText(QCoreApplication.translate("Dialog", u"LDROM", None))
        self.radioButton_bt_1_0.setText(QCoreApplication.translate("Dialog", u" LDROM with IAP", None))
        self.radioButton_bt_0_1.setText(QCoreApplication.translate("Dialog", u"APROM", None))
        self.radioButton_bt_1_1.setText(QCoreApplication.translate("Dialog", u"APROM with IAP", None))
        self.gridGroupBox_data_flash.setTitle(QCoreApplication.translate("Dialog", u"Data Flash Options", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Base Address: 0x", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Data Flash Size:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"K", None))
        self.checkBox_dataflash.setText(QCoreApplication.translate("Dialog", u"Data Flash", None))
        self.gridGroupBox_pwm.setTitle(QCoreApplication.translate("Dialog", u"PWM Tri-State", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Basic PWM Tri-State", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"PWM Odd0 Tri-State", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"PWM Even0 Tri-State", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"PWM Even1 Tri-State", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"PWM Odd1 Tri-State", None))
        self.checkBox_watchdog_pwdwn.setText(QCoreApplication.translate("Dialog", u"Watchdog Clock Power-down", None))
        self.checkBox_security_lock.setText(QCoreApplication.translate("Dialog", u"Security Lock", None))
        self.checkBox_watchdog.setText(QCoreApplication.translate("Dialog", u"Watchdog", None))
        self.gridGroupBox_config.setTitle(QCoreApplication.translate("Dialog", u"Config Value", None))
        self.label_config0.setText(QCoreApplication.translate("Dialog", u"Config 0:", None))
        self.label_config1.setText(QCoreApplication.translate("Dialog", u"Config 1:", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

