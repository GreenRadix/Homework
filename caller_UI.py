# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modems.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SIMCaller(object):
    def setupUi(self, SIMCaller):
        SIMCaller.setObjectName("SIMCaller")
        SIMCaller.resize(699, 828)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SIMCaller.sizePolicy().
                                                        hasHeightForWidth())
        SIMCaller.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(SIMCaller)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setEnabled(True)
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
# вікно ModemBox 1 ------------------------------------------------------------
        self.ModemBox_1 = QtWidgets.QGroupBox(self.tab_1)
        self.ModemBox_1.setToolTipDuration(-4)
        self.ModemBox_1.setObjectName("ModemBox_1")
        self.ConSetBoxMod_1 = QtWidgets.QGroupBox(self.ModemBox_1)
        self.ConSetBoxMod_1.setGeometry(QtCore.QRect(11, 17, 309, 142))
        self.ConSetBoxMod_1.setFlat(False)
        self.ConSetBoxMod_1.setCheckable(False)
        self.ConSetBoxMod_1.setChecked(False)
        self.ConSetBoxMod_1.setObjectName("ConSetBoxMod_1")
        self.BoudlabelMod_1 = QtWidgets.QLabel(self.ConSetBoxMod_1)
        self.BoudlabelMod_1.setGeometry(QtCore.QRect(20, 63, 47, 13))
        self.BoudlabelMod_1.setObjectName("BoudlabelMod_1")
        self.PortlabelMod_1 = QtWidgets.QLabel(self.ConSetBoxMod_1)
        self.PortlabelMod_1.setGeometry(QtCore.QRect(21, 27, 25, 16))
        self.PortlabelMod_1.setObjectName("PortlabelMod_1")
        self.FindPortButtMod_1 = QtWidgets.QPushButton(self.ConSetBoxMod_1)
        self.FindPortButtMod_1.setGeometry(QtCore.QRect(180, 26, 76, 21))
        self.FindPortButtMod_1.setObjectName("FindPortButtMod_1")
        self.layoutWidget = QtWidgets.QWidget(self.ConSetBoxMod_1)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 25, 71, 57))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.portComboBoxMod_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.portComboBoxMod_1.setEditable(False)
        self.portComboBoxMod_1.setCurrentText("")
        self.portComboBoxMod_1.setObjectName("portComboBoxMod_1")
        self.verticalLayout_3.addWidget(self.portComboBoxMod_1)
        self.boudrateComboBoxMod_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.boudrateComboBoxMod_1.setEditable(False)
        self.boudrateComboBoxMod_1.setObjectName("boudrateComboBoxMod_1")
        self.boudrateComboBoxMod_1.addItem("")
        self.boudrateComboBoxMod_1.addItem("")
        self.boudrateComboBoxMod_1.addItem("")
        self.boudrateComboBoxMod_1.addItem("")
        self.boudrateComboBoxMod_1.addItem("")
        self.boudrateComboBoxMod_1.addItem("")
        self.boudrateComboBoxMod_1.addItem("")
        self.verticalLayout_3.addWidget(self.boudrateComboBoxMod_1)
        self.layoutWidget1 = QtWidgets.QWidget(self.ConSetBoxMod_1)
        self.layoutWidget1.setGeometry(QtCore.QRect(17, 90, 221, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ConnButtMod_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.ConnButtMod_1.setObjectName("ConnButtMod_1")
        self.horizontalLayout_5.addWidget(self.ConnButtMod_1)
        self.DisconnButtMod_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.DisconnButtMod_1.setObjectName("DisconnButtMod_1")
        self.horizontalLayout_5.addWidget(self.DisconnButtMod_1)
        self.TaskBoxMod_1 = QtWidgets.QGroupBox(self.ModemBox_1)
        self.TaskBoxMod_1.setGeometry(QtCore.QRect(11, 173, 309, 141))
        self.TaskBoxMod_1.setObjectName("TaskBoxMod_1")
        self.layoutWidget2 = QtWidgets.QWidget(self.TaskBoxMod_1)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 79, 42))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ActivationCBMod_1 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.ActivationCBMod_1.setObjectName("ActivationCBMod_1")
        self.verticalLayout_4.addWidget(self.ActivationCBMod_1)
        self.CallingCBMod_1 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.CallingCBMod_1.setObjectName("CallingCBMod_1")
        self.verticalLayout_4.addWidget(self.CallingCBMod_1)
        self.layoutWidget3 = QtWidgets.QWidget(self.TaskBoxMod_1)
        self.layoutWidget3.setGeometry(QtCore.QRect(115, 32, 134, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ProvlabelMod_1 = QtWidgets.QLabel(self.layoutWidget3)
        self.ProvlabelMod_1.setObjectName("ProvlabelMod_1")
        self.horizontalLayout_6.addWidget(self.ProvlabelMod_1)
        self.ProvComboBoxMod_1 = QtWidgets.QComboBox(self.layoutWidget3)
        self.ProvComboBoxMod_1.setObjectName("ProvComboBoxMod_1")
        self.ProvComboBoxMod_1.addItem("")
        self.ProvComboBoxMod_1.addItem("")
        self.ProvComboBoxMod_1.addItem("")
        self.horizontalLayout_6.addWidget(self.ProvComboBoxMod_1)
        self.layoutWidget4 = QtWidgets.QWidget(self.TaskBoxMod_1)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 100, 155, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CallTimeSBMod_1 = QtWidgets.QSpinBox(self.layoutWidget4)
        self.CallTimeSBMod_1.setMinimum(10)
        self.CallTimeSBMod_1.setMaximum(1000)
        self.CallTimeSBMod_1.setObjectName("CallTimeSBMod_1")
        self.horizontalLayout_3.addWidget(self.CallTimeSBMod_1)

        self.CallTimelabelMod_1 = QtWidgets.QLabel(self.layoutWidget4)
        self.CallTimelabelMod_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CallTimelabelMod_1.setObjectName("CallTimelabelMod_1")

        self.horizontalLayout_3.addWidget(self.CallTimelabelMod_1)

        self.scrollArea = QtWidgets.QScrollArea(self.ModemBox_1)
        self.scrollArea.setGeometry(QtCore.QRect(329, 23, 300, 291))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # Вікно виводу тексту модема 1
        self.textBrowserMod_1 = QtWidgets.QTextBrowser(self.
                                                    scrollAreaWidgetContents)
        self.textBrowserMod_1.setGeometry(QtCore.QRect(-1, -1, 300, 291))
        self.textBrowserMod_1.setObjectName("textBrowserMod_1")
        # -------------------------------------------------------------------
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.ModemBox_1)
# вікно ModemBox 2 ------------------------------------------------------------
        self.ModemBox_2 = QtWidgets.QGroupBox(self.tab_1)
        self.ModemBox_2.setObjectName("ModemBox_2")
        self.ConSetBoxMod_2 = QtWidgets.QGroupBox(self.ModemBox_2)
        self.ConSetBoxMod_2.setGeometry(QtCore.QRect(10, 20, 309, 142))
        self.ConSetBoxMod_2.setFlat(False)
        self.ConSetBoxMod_2.setCheckable(False)
        self.ConSetBoxMod_2.setChecked(False)
        self.ConSetBoxMod_2.setObjectName("ConSetBoxMod_2")
        self.BoudlabelMod_2 = QtWidgets.QLabel(self.ConSetBoxMod_2)
        self.BoudlabelMod_2.setGeometry(QtCore.QRect(20, 63, 47, 13))
        self.BoudlabelMod_2.setObjectName("BoudlabelMod_2")
        self.PortlabelMod_2 = QtWidgets.QLabel(self.ConSetBoxMod_2)
        self.PortlabelMod_2.setGeometry(QtCore.QRect(21, 27, 25, 16))
        self.PortlabelMod_2.setObjectName("PortlabelMod_2")
        self.FindPortButtMod_2 = QtWidgets.QPushButton(self.ConSetBoxMod_2)
        self.FindPortButtMod_2.setGeometry(QtCore.QRect(180, 26, 76, 21))
        self.FindPortButtMod_2.setObjectName("FindPortButtMod_2")
        self.layoutWidget_8 = QtWidgets.QWidget(self.ConSetBoxMod_2)
        self.layoutWidget_8.setGeometry(QtCore.QRect(17, 90, 221, 25))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ConnButtMod_2 = QtWidgets.QPushButton(self.layoutWidget_8)
        self.ConnButtMod_2.setObjectName("ConnButtMod_2")
        self.horizontalLayout_10.addWidget(self.ConnButtMod_2)
        self.DisconnButtMod_2 = QtWidgets.QPushButton(self.layoutWidget_8)
        self.DisconnButtMod_2.setObjectName("DisconnButtMod_2")
        self.horizontalLayout_10.addWidget(self.DisconnButtMod_2)
        self.portComboBoxMod_2 = QtWidgets.QComboBox(self.ConSetBoxMod_2)
        self.portComboBoxMod_2.setEnabled(True)
        self.portComboBoxMod_2.setGeometry(QtCore.QRect(91, 27, 69, 20))
        self.portComboBoxMod_2.setEditable(False)
        self.portComboBoxMod_2.setCurrentText("")
        self.portComboBoxMod_2.setObjectName("portComboBoxMod_2")
        self.boudrateComboBoxMod_2 = QtWidgets.QComboBox(self.ConSetBoxMod_2)
        self.boudrateComboBoxMod_2.setGeometry(QtCore.QRect(91, 58, 62, 20))
        self.boudrateComboBoxMod_2.setEditable(False)
        self.boudrateComboBoxMod_2.setObjectName("boudrateComboBoxMod_2")
        self.boudrateComboBoxMod_2.addItem("")
        self.boudrateComboBoxMod_2.addItem("")
        self.boudrateComboBoxMod_2.addItem("")
        self.boudrateComboBoxMod_2.addItem("")
        self.boudrateComboBoxMod_2.addItem("")
        self.boudrateComboBoxMod_2.addItem("")
        self.boudrateComboBoxMod_2.addItem("")
        # Вікно виводу тексту модема 2
        self.textBrowserMod_2 = QtWidgets.QTextBrowser(self.ModemBox_2)
        self.textBrowserMod_2.setGeometry(QtCore.QRect(330, 27, 300, 291))
        self.textBrowserMod_2.setObjectName("textBrowserMod_2")
        # --------------------------------------------------------------
        self.TaskBoxMod_2 = QtWidgets.QGroupBox(self.ModemBox_2)
        self.TaskBoxMod_2.setGeometry(QtCore.QRect(10, 176, 309, 141))
        self.TaskBoxMod_2.setObjectName("TaskBoxMod_2")
        self.layoutWidget_9 = QtWidgets.QWidget(self.TaskBoxMod_2)
        self.layoutWidget_9.setGeometry(QtCore.QRect(10, 30, 79, 42))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ActivationCBMod_2 = QtWidgets.QCheckBox(self.layoutWidget_9)
        self.ActivationCBMod_2.setObjectName("ActivationCBMod_2")
        self.verticalLayout_8.addWidget(self.ActivationCBMod_2)
        self.CallingCBMod_2 = QtWidgets.QCheckBox(self.layoutWidget_9)
        self.CallingCBMod_2.setObjectName("CallingCBMod_2")
        self.verticalLayout_8.addWidget(self.CallingCBMod_2)
        self.layoutWidget_10 = QtWidgets.QWidget(self.TaskBoxMod_2)
        self.layoutWidget_10.setGeometry(QtCore.QRect(115, 32, 134, 22))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_10)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.ProvComboBoxMod_2 = QtWidgets.QComboBox(self.layoutWidget_10)
        self.ProvComboBoxMod_2.setObjectName("ProvComboBoxMod_2")
        self.ProvComboBoxMod_2.addItem("")
        self.ProvComboBoxMod_2.addItem("")
        self.ProvComboBoxMod_2.addItem("")
        self.horizontalLayout_11.addWidget(self.ProvComboBoxMod_2)
        self.layoutWidget_11 = QtWidgets.QWidget(self.TaskBoxMod_2)
        self.layoutWidget_11.setGeometry(QtCore.QRect(10, 100, 155, 22))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.CallTimeSBMod_2 = QtWidgets.QSpinBox(self.layoutWidget_11)
        self.CallTimeSBMod_2.setMinimum(10)
        self.CallTimeSBMod_2.setMaximum(1000)
        self.CallTimeSBMod_2.setObjectName("CallTimeSBMod_2")
        self.horizontalLayout_12.addWidget(self.CallTimeSBMod_2)
        self.CallTimelabelMod_2 = QtWidgets.QLabel(self.layoutWidget_11)
        self.CallTimelabelMod_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CallTimelabelMod_2.setObjectName("CallTimelabelMod_2")
        self.horizontalLayout_12.addWidget(self.CallTimelabelMod_2)
        self.verticalLayout.addWidget(self.ModemBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
# опис tabWidget -------------------------------------------------------------
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setEnabled(True)
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setEnabled(True)
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StartAllButt = QtWidgets.QPushButton(self.centralwidget)
# Кнопка "StartAllButt" -------------------------------------------------------
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartAllButt.sizePolicy().
                                                        hasHeightForWidth())
        self.StartAllButt.setSizePolicy(sizePolicy)
        self.StartAllButt.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.StartAllButt.setShortcut("")
        self.StartAllButt.setFlat(False)
        self.StartAllButt.setObjectName("StartAllButt")
        self.horizontalLayout_2.addWidget(self.StartAllButt)
# Кнопка "StopAllButt" -------------------------------------------------------
        self.StopAllButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopAllButt.sizePolicy().
                                                        hasHeightForWidth())
        self.StopAllButt.setSizePolicy(sizePolicy)
        self.StopAllButt.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.StopAllButt.setObjectName("StopAllButt")
        self.horizontalLayout_2.addWidget(self.StopAllButt)
# Кнопка "ResetAllButt" -------------------------------------------------------
        self.ResetAllButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetAllButt.sizePolicy().
                                                        hasHeightForWidth())
        self.ResetAllButt.setSizePolicy(sizePolicy)
        self.ResetAllButt.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.ResetAllButt.setObjectName("ResetAllButt")
        self.horizontalLayout_2.addWidget(self.ResetAllButt)
# -----------------------------------------------------------------------------
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        SIMCaller.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SIMCaller)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 21))
        self.menubar.setObjectName("menubar")
        SIMCaller.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SIMCaller)
        self.statusbar.setObjectName("statusbar")
        SIMCaller.setStatusBar(self.statusbar)

        self.retranslateUi(SIMCaller)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SIMCaller)
# ----------------------------------------------------------------------------


    def retranslateUi(self, SIMCaller):
        _translate = QtCore.QCoreApplication.translate
        SIMCaller.setWindowTitle(_translate("SIMCaller", "SIMCaller"))
        self.ModemBox_1.setTitle(_translate("SIMCaller", "Modem 1"))
        self.ConSetBoxMod_1.setTitle(_translate("SIMCaller",
                                                "Налаштування з\'єднання"))
        self.BoudlabelMod_1.setText(_translate("SIMCaller", "Boudrate"))
        self.PortlabelMod_1.setText(_translate("SIMCaller", "Порт"))
        self.FindPortButtMod_1.setText(_translate("SIMCaller", "Пошук портів"))
        self.boudrateComboBoxMod_1.setCurrentText(_translate
                                                  ("SIMCaller", "2400"))
        self.boudrateComboBoxMod_1.setItemText(0, _translate
                                                    ("SIMCaller", "2400"))
        self.boudrateComboBoxMod_1.setItemText(1, _translate
                                                    ("SIMCaller", "4800"))
        self.boudrateComboBoxMod_1.setItemText(2, _translate
                                                    ("SIMCaller", "9600"))
        self.boudrateComboBoxMod_1.setItemText(3, _translate
                                                    ("SIMCaller", "19200"))
        self.boudrateComboBoxMod_1.setItemText(4, _translate
                                                    ("SIMCaller", "38400"))
        self.boudrateComboBoxMod_1.setItemText(5, _translate
                                                    ("SIMCaller", "57600"))
        self.boudrateComboBoxMod_1.setItemText(6, _translate
                                                    ("SIMCaller", "115200"))
        self.ConnButtMod_1.setText(_translate("SIMCaller", "З\'єднання"))
        self.DisconnButtMod_1.setText(_translate("SIMCaller", "Роз\'єднання"))
        self.TaskBoxMod_1.setTitle(_translate
                                   ("SIMCaller", "Налаштування задач"))
        self.ActivationCBMod_1.setText(_translate("SIMCaller", "Активація"))
        self.CallingCBMod_1.setText(_translate("SIMCaller", "Прозвонка"))
        self.ProvlabelMod_1.setText(_translate("SIMCaller", "Оператор:"))
        self.ProvComboBoxMod_1.setItemText(0, _translate
                                                    ("SIMCaller", "Vodafone"))
        self.ProvComboBoxMod_1.setItemText(1, _translate
                                                    ("SIMCaller", "Kyivstar"))
        self.ProvComboBoxMod_1.setItemText(2, _translate
                                                    ("SIMCaller", "LifeCell"))
        self.CallTimelabelMod_1.setText(_translate
                                        ("SIMCaller", "Час прозвонки, сек"))
        self.ModemBox_2.setTitle(_translate("SIMCaller", "Modem 2"))
        self.ConSetBoxMod_2.setTitle(_translate
                                     ("SIMCaller", "Налаштування з\'єднання"))
        self.BoudlabelMod_2.setText(_translate("SIMCaller", "Boudrate"))
        self.PortlabelMod_2.setText(_translate("SIMCaller", "Порт"))
        self.FindPortButtMod_2.setText(_translate("SIMCaller", "Пошук портів"))
        self.ConnButtMod_2.setText(_translate("SIMCaller", "З\'єднання"))
        self.DisconnButtMod_2.setText(_translate("SIMCaller", "Роз\'єднання"))
        self.boudrateComboBoxMod_2.setCurrentText(_translate
                                                    ("SIMCaller", "2400"))
        self.boudrateComboBoxMod_2.setItemText(0, _translate
                                                    ("SIMCaller", "2400"))
        self.boudrateComboBoxMod_2.setItemText(1, _translate
                                                    ("SIMCaller", "4800"))
        self.boudrateComboBoxMod_2.setItemText(2, _translate
                                                    ("SIMCaller", "9600"))
        self.boudrateComboBoxMod_2.setItemText(3, _translate
                                                    ("SIMCaller", "19200"))
        self.boudrateComboBoxMod_2.setItemText(4, _translate
                                                    ("SIMCaller", "38400"))
        self.boudrateComboBoxMod_2.setItemText(5, _translate
                                                    ("SIMCaller", "57600"))
        self.boudrateComboBoxMod_2.setItemText(6, _translate
                                                    ("SIMCaller", "115200"))
        self.TaskBoxMod_2.setTitle(_translate
                                   ("SIMCaller", "Налаштування задач"))
        self.ActivationCBMod_2.setText(_translate("SIMCaller", "Активація"))
        self.CallingCBMod_2.setText(_translate("SIMCaller", "Прозвонка"))
        self.label_6.setText(_translate("SIMCaller", "Оператор:"))
        self.ProvComboBoxMod_2.setItemText(0, _translate
                                                    ("SIMCaller", "Vodafone"))
        self.ProvComboBoxMod_2.setItemText(1, _translate
                                                    ("SIMCaller", "Kyivstar"))
        self.ProvComboBoxMod_2.setItemText(2, _translate
                                                    ("SIMCaller", "LifeCell"))
        self.CallTimelabelMod_2.setText(_translate
                                        ("SIMCaller", "Час прозвонки, сек"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1),
                                            _translate("SIMCaller", "Pair 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                            _translate("SIMCaller", "Pair 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                            _translate("SIMCaller", "Pair 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                            _translate("SIMCaller", "Pair 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                            _translate("SIMCaller", "Pair 5"))
        self.StartAllButt.setText(_translate("SIMCaller", "СТАРТ всі слоти"))
        self.StopAllButt.setText(_translate("SIMCaller", "СТОП всі слоти"))
        self.ResetAllButt.setText(_translate
                                        ("SIMCaller", "СКИДАННЯ всі слоти"))

