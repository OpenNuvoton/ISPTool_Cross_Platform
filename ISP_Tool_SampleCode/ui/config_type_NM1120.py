# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_type_NM1120.ui'
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
        Dialog.resize(442, 581)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 415, 569))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridGroupBox_brownout = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_brownout.setObjectName(u"gridGroupBox_brownout")
        self.gridLayout_7 = QGridLayout(self.gridGroupBox_brownout)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radioButton_bw_v_2 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_2.setObjectName(u"radioButton_bw_v_2")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_2, 0, 2, 1, 1)

        self.radioButton_bw_v_3 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_3.setObjectName(u"radioButton_bw_v_3")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_3, 0, 3, 1, 1)

        self.radioButton_bw_v_0 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_0.setObjectName(u"radioButton_bw_v_0")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_0, 0, 0, 1, 1)

        self.radioButton_bw_v_1 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_1.setObjectName(u"radioButton_bw_v_1")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_1, 0, 1, 1, 1)

        self.radioButton_bw_v_4 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_4.setObjectName(u"radioButton_bw_v_4")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_4, 1, 0, 1, 1)

        self.radioButton_bw_v_5 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_5.setObjectName(u"radioButton_bw_v_5")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_5, 1, 1, 1, 1)

        self.radioButton_bw_v_7 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_7.setObjectName(u"radioButton_bw_v_7")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_7, 1, 3, 1, 1)

        self.radioButton_bw_v_6 = QRadioButton(self.gridGroupBox_brownout)
        self.radioButton_bw_v_6.setObjectName(u"radioButton_bw_v_6")

        self.gridLayout_7.addWidget(self.radioButton_bw_v_6, 1, 2, 1, 1)

        self.checkBox_bw_0 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_0.setObjectName(u"checkBox_bw_0")

        self.gridLayout_7.addWidget(self.checkBox_bw_0, 2, 0, 1, 1)

        self.checkBox_bw_1 = QCheckBox(self.gridGroupBox_brownout)
        self.checkBox_bw_1.setObjectName(u"checkBox_bw_1")

        self.gridLayout_7.addWidget(self.checkBox_bw_1, 2, 2, 1, 1)

        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(1, 1)
        self.gridLayout_7.setRowStretch(2, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.gridLayout_7.setColumnStretch(2, 1)
        self.gridLayout_7.setColumnStretch(3, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_brownout)

        self.gridGroupBox_boot = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_boot.setObjectName(u"gridGroupBox_boot")
        self.gridLayout_6 = QGridLayout(self.gridGroupBox_boot)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_bt_0_1 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_1.setObjectName(u"radioButton_bt_0_1")

        self.gridLayout_6.addWidget(self.radioButton_bt_0_1, 0, 1, 1, 1)

        self.radioButton_bt_0_0 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_0_0.setObjectName(u"radioButton_bt_0_0")

        self.gridLayout_6.addWidget(self.radioButton_bt_0_0, 0, 0, 1, 1)

        self.radioButton_bt_1_1 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_1_1.setObjectName(u"radioButton_bt_1_1")

        self.gridLayout_6.addWidget(self.radioButton_bt_1_1, 1, 1, 1, 1)

        self.radioButton_bt_1_0 = QRadioButton(self.gridGroupBox_boot)
        self.radioButton_bt_1_0.setObjectName(u"radioButton_bt_1_0")

        self.gridLayout_6.addWidget(self.radioButton_bt_1_0, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.gridGroupBox_boot)

        self.gridGroupBox_io_state = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_io_state.setObjectName(u"gridGroupBox_io_state")
        self.gridLayout_5 = QGridLayout(self.gridGroupBox_io_state)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radioButton_io_0 = QRadioButton(self.gridGroupBox_io_state)
        self.radioButton_io_0.setObjectName(u"radioButton_io_0")

        self.gridLayout_5.addWidget(self.radioButton_io_0, 0, 0, 1, 1)

        self.radioButton_io_1 = QRadioButton(self.gridGroupBox_io_state)
        self.radioButton_io_1.setObjectName(u"radioButton_io_1")

        self.gridLayout_5.addWidget(self.radioButton_io_1, 0, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_io_state)

        self.gridGroupBox_resistor = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_resistor.setObjectName(u"gridGroupBox_resistor")
        self.gridLayout_4 = QGridLayout(self.gridGroupBox_resistor)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.GPA0 = QWidget(self.gridGroupBox_resistor)
        self.GPA0.setObjectName(u"GPA0")
        self.horizontalLayout = QHBoxLayout(self.GPA0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_gpa0 = QLabel(self.GPA0)
        self.label_gpa0.setObjectName(u"label_gpa0")

        self.horizontalLayout.addWidget(self.label_gpa0)

        self.radioButton_gpa0_0 = QRadioButton(self.GPA0)
        self.radioButton_gpa0_0.setObjectName(u"radioButton_gpa0_0")

        self.horizontalLayout.addWidget(self.radioButton_gpa0_0)

        self.radioButton_gpa0_1 = QRadioButton(self.GPA0)
        self.radioButton_gpa0_1.setObjectName(u"radioButton_gpa0_1")

        self.horizontalLayout.addWidget(self.radioButton_gpa0_1)

        self.radioButton_gpa0_2 = QRadioButton(self.GPA0)
        self.radioButton_gpa0_2.setObjectName(u"radioButton_gpa0_2")

        self.horizontalLayout.addWidget(self.radioButton_gpa0_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.GPA0, 5, 0, 1, 1)

        self.GPA1 = QWidget(self.gridGroupBox_resistor)
        self.GPA1.setObjectName(u"GPA1")
        self.horizontalLayout_2 = QHBoxLayout(self.GPA1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_gpa1 = QLabel(self.GPA1)
        self.label_gpa1.setObjectName(u"label_gpa1")

        self.horizontalLayout_2.addWidget(self.label_gpa1)

        self.radioButton_gpa1_0 = QRadioButton(self.GPA1)
        self.radioButton_gpa1_0.setObjectName(u"radioButton_gpa1_0")

        self.horizontalLayout_2.addWidget(self.radioButton_gpa1_0)

        self.radioButton_gpa1_1 = QRadioButton(self.GPA1)
        self.radioButton_gpa1_1.setObjectName(u"radioButton_gpa1_1")

        self.horizontalLayout_2.addWidget(self.radioButton_gpa1_1)

        self.radioButton_gpa1_2 = QRadioButton(self.GPA1)
        self.radioButton_gpa1_2.setObjectName(u"radioButton_gpa1_2")

        self.horizontalLayout_2.addWidget(self.radioButton_gpa1_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.GPA1, 6, 0, 1, 1)

        self.GPA2 = QWidget(self.gridGroupBox_resistor)
        self.GPA2.setObjectName(u"GPA2")
        self.horizontalLayout_3 = QHBoxLayout(self.GPA2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_gpa2 = QLabel(self.GPA2)
        self.label_gpa2.setObjectName(u"label_gpa2")

        self.horizontalLayout_3.addWidget(self.label_gpa2)

        self.radioButton_gpa2_0 = QRadioButton(self.GPA2)
        self.radioButton_gpa2_0.setObjectName(u"radioButton_gpa2_0")

        self.horizontalLayout_3.addWidget(self.radioButton_gpa2_0)

        self.radioButton_gpa2_1 = QRadioButton(self.GPA2)
        self.radioButton_gpa2_1.setObjectName(u"radioButton_gpa2_1")

        self.horizontalLayout_3.addWidget(self.radioButton_gpa2_1)

        self.radioButton_gpa2_2 = QRadioButton(self.GPA2)
        self.radioButton_gpa2_2.setObjectName(u"radioButton_gpa2_2")

        self.horizontalLayout_3.addWidget(self.radioButton_gpa2_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.GPA2, 7, 0, 1, 1)

        self.GPA3 = QWidget(self.gridGroupBox_resistor)
        self.GPA3.setObjectName(u"GPA3")
        self.horizontalLayout_5 = QHBoxLayout(self.GPA3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_gpa3 = QLabel(self.GPA3)
        self.label_gpa3.setObjectName(u"label_gpa3")

        self.horizontalLayout_5.addWidget(self.label_gpa3)

        self.radioButton_gpa3_0 = QRadioButton(self.GPA3)
        self.radioButton_gpa3_0.setObjectName(u"radioButton_gpa3_0")

        self.horizontalLayout_5.addWidget(self.radioButton_gpa3_0)

        self.radioButton_gpa3_1 = QRadioButton(self.GPA3)
        self.radioButton_gpa3_1.setObjectName(u"radioButton_gpa3_1")

        self.horizontalLayout_5.addWidget(self.radioButton_gpa3_1)

        self.radioButton_gpa3_2 = QRadioButton(self.GPA3)
        self.radioButton_gpa3_2.setObjectName(u"radioButton_gpa3_2")

        self.horizontalLayout_5.addWidget(self.radioButton_gpa3_2)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.GPA3, 8, 0, 1, 1)

        self.GPA4 = QWidget(self.gridGroupBox_resistor)
        self.GPA4.setObjectName(u"GPA4")
        self.horizontalLayout_6 = QHBoxLayout(self.GPA4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_gpa4 = QLabel(self.GPA4)
        self.label_gpa4.setObjectName(u"label_gpa4")

        self.horizontalLayout_6.addWidget(self.label_gpa4)

        self.radioButton_gpa4_0 = QRadioButton(self.GPA4)
        self.radioButton_gpa4_0.setObjectName(u"radioButton_gpa4_0")

        self.horizontalLayout_6.addWidget(self.radioButton_gpa4_0)

        self.radioButton_gpa4_1 = QRadioButton(self.GPA4)
        self.radioButton_gpa4_1.setObjectName(u"radioButton_gpa4_1")

        self.horizontalLayout_6.addWidget(self.radioButton_gpa4_1)

        self.radioButton_gpa4_2 = QRadioButton(self.GPA4)
        self.radioButton_gpa4_2.setObjectName(u"radioButton_gpa4_2")

        self.horizontalLayout_6.addWidget(self.radioButton_gpa4_2)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.GPA4, 9, 0, 1, 1)

        self.GPA5 = QWidget(self.gridGroupBox_resistor)
        self.GPA5.setObjectName(u"GPA5")
        self.horizontalLayout_8 = QHBoxLayout(self.GPA5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_gpa5 = QLabel(self.GPA5)
        self.label_gpa5.setObjectName(u"label_gpa5")

        self.horizontalLayout_8.addWidget(self.label_gpa5)

        self.radioButton_gpa5_0 = QRadioButton(self.GPA5)
        self.radioButton_gpa5_0.setObjectName(u"radioButton_gpa5_0")

        self.horizontalLayout_8.addWidget(self.radioButton_gpa5_0)

        self.radioButton_gpa5_1 = QRadioButton(self.GPA5)
        self.radioButton_gpa5_1.setObjectName(u"radioButton_gpa5_1")

        self.horizontalLayout_8.addWidget(self.radioButton_gpa5_1)

        self.radioButton_gpa5_2 = QRadioButton(self.GPA5)
        self.radioButton_gpa5_2.setObjectName(u"radioButton_gpa5_2")

        self.horizontalLayout_8.addWidget(self.radioButton_gpa5_2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 2)
        self.horizontalLayout_8.setStretch(3, 2)

        self.gridLayout_4.addWidget(self.GPA5, 10, 0, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 2)
        self.gridLayout_4.setRowStretch(4, 1)
        self.gridLayout_4.setRowStretch(5, 1)
        self.gridLayout_4.setRowStretch(6, 1)
        self.gridLayout_4.setRowStretch(7, 1)
        self.gridLayout_4.setRowStretch(8, 1)
        self.gridLayout_4.setRowStretch(9, 1)
        self.gridLayout_4.setRowStretch(10, 1)

        self.verticalLayout.addWidget(self.gridGroupBox_resistor)

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

        self.gridGroupBox_misc = QGroupBox(self.scrollAreaWidgetContents)
        self.gridGroupBox_misc.setObjectName(u"gridGroupBox_misc")
        self.gridLayout_3 = QGridLayout(self.gridGroupBox_misc)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_security_lock = QCheckBox(self.gridGroupBox_misc)
        self.checkBox_security_lock.setObjectName(u"checkBox_security_lock")

        self.gridLayout_3.addWidget(self.checkBox_security_lock, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setColumnStretch(0, 1)

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
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gridGroupBox_brownout.setTitle(QCoreApplication.translate("Dialog", u"Brown-out Voltage Options", None))
        self.radioButton_bw_v_2.setText(QCoreApplication.translate("Dialog", u"3.7V", None))
        self.radioButton_bw_v_3.setText(QCoreApplication.translate("Dialog", u"3.0V", None))
        self.radioButton_bw_v_0.setText(QCoreApplication.translate("Dialog", u"4.3V", None))
        self.radioButton_bw_v_1.setText(QCoreApplication.translate("Dialog", u"4.0V", None))
        self.radioButton_bw_v_4.setText(QCoreApplication.translate("Dialog", u"2.7V", None))
        self.radioButton_bw_v_5.setText(QCoreApplication.translate("Dialog", u"2.4V", None))
        self.radioButton_bw_v_7.setText(QCoreApplication.translate("Dialog", u"2.0V", None))
        self.radioButton_bw_v_6.setText(QCoreApplication.translate("Dialog", u"2.2V", None))
        self.checkBox_bw_0.setText(QCoreApplication.translate("Dialog", u"Brown-out Detector", None))
        self.checkBox_bw_1.setText(QCoreApplication.translate("Dialog", u"Brown-out Reset", None))
        self.gridGroupBox_boot.setTitle(QCoreApplication.translate("Dialog", u"Boot Options", None))
        self.radioButton_bt_0_1.setText(QCoreApplication.translate("Dialog", u"APROM", None))
        self.radioButton_bt_0_0.setText(QCoreApplication.translate("Dialog", u"LDROM", None))
        self.radioButton_bt_1_1.setText(QCoreApplication.translate("Dialog", u"APROM with IAP", None))
        self.radioButton_bt_1_0.setText(QCoreApplication.translate("Dialog", u" LDROM with IAP", None))
        self.gridGroupBox_io_state.setTitle(QCoreApplication.translate("Dialog", u"I/O Initial State Options", None))
        self.radioButton_io_0.setText(QCoreApplication.translate("Dialog", u"Input Tri-state Mode", None))
        self.radioButton_io_1.setText(QCoreApplication.translate("Dialog", u"Quasi-bidirectional Mode", None))
        self.gridGroupBox_resistor.setTitle(QCoreApplication.translate("Dialog", u"Power-on Pull Resistor Initial State Selection", None))
        self.label_gpa0.setText(QCoreApplication.translate("Dialog", u"GPA0:", None))
        self.radioButton_gpa0_0.setText(QCoreApplication.translate("Dialog", u"Pull-Low Resistor", None))
        self.radioButton_gpa0_1.setText(QCoreApplication.translate("Dialog", u"Pull-High Resistor", None))
        self.radioButton_gpa0_2.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.label_gpa1.setText(QCoreApplication.translate("Dialog", u"GPA1:", None))
        self.radioButton_gpa1_0.setText(QCoreApplication.translate("Dialog", u"Pull-Low Resistor", None))
        self.radioButton_gpa1_1.setText(QCoreApplication.translate("Dialog", u"Pull-High Resistor", None))
        self.radioButton_gpa1_2.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.label_gpa2.setText(QCoreApplication.translate("Dialog", u"GPA2:", None))
        self.radioButton_gpa2_0.setText(QCoreApplication.translate("Dialog", u"Pull-Low Resistor", None))
        self.radioButton_gpa2_1.setText(QCoreApplication.translate("Dialog", u"Pull-High Resistor", None))
        self.radioButton_gpa2_2.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.label_gpa3.setText(QCoreApplication.translate("Dialog", u"GPA3:", None))
        self.radioButton_gpa3_0.setText(QCoreApplication.translate("Dialog", u"Pull-Low Resistor", None))
        self.radioButton_gpa3_1.setText(QCoreApplication.translate("Dialog", u"Pull-High Resistor", None))
        self.radioButton_gpa3_2.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.label_gpa4.setText(QCoreApplication.translate("Dialog", u"GPA4:", None))
        self.radioButton_gpa4_0.setText(QCoreApplication.translate("Dialog", u"Pull-Low Resistor", None))
        self.radioButton_gpa4_1.setText(QCoreApplication.translate("Dialog", u"Pull-High Resistor", None))
        self.radioButton_gpa4_2.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.label_gpa5.setText(QCoreApplication.translate("Dialog", u"GPA5:", None))
        self.radioButton_gpa5_0.setText(QCoreApplication.translate("Dialog", u"Pull-Low Resistor", None))
        self.radioButton_gpa5_1.setText(QCoreApplication.translate("Dialog", u"Pull-High Resistor", None))
        self.radioButton_gpa5_2.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.gridGroupBox_data_flash.setTitle(QCoreApplication.translate("Dialog", u"Data Flash Options", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Base Address: 0x", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Data Flash Size:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"K", None))
        self.checkBox_dataflash.setText(QCoreApplication.translate("Dialog", u"Data Flash", None))
        self.checkBox_security_lock.setText(QCoreApplication.translate("Dialog", u"Security Lock", None))
        self.gridGroupBox_config.setTitle(QCoreApplication.translate("Dialog", u"Config Value", None))
        self.label_config0.setText(QCoreApplication.translate("Dialog", u"Config 0:", None))
        self.label_config1.setText(QCoreApplication.translate("Dialog", u"Config 1:", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

