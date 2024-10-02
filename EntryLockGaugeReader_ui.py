# Form implementation generated from reading ui file 'd:\SynologyDrive_Home\programming\Git\WikiLogauge\EntryLockGaugeReader.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 650)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_serialport = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_serialport.setMaximumSize(QtCore.QSize(78, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_serialport.setFont(font)
        self.label_serialport.setObjectName("label_serialport")
        self.horizontalLayout_2.addWidget(self.label_serialport)
        self.port_list = QtWidgets.QComboBox(parent=self.centralwidget)
        self.port_list.setObjectName("port_list")
        self.horizontalLayout_2.addWidget(self.port_list)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_savepath = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.lineEdit_savepath.setFont(font)
        self.lineEdit_savepath.setObjectName("lineEdit_savepath")
        self.horizontalLayout_5.addWidget(self.lineEdit_savepath)
        self.AutoSaveLog = QtWidgets.QCheckBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.AutoSaveLog.setFont(font)
        self.AutoSaveLog.setChecked(True)
        self.AutoSaveLog.setObjectName("AutoSaveLog")
        self.horizontalLayout_5.addWidget(self.AutoSaveLog)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gaugeID = QtWidgets.QComboBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.gaugeID.setFont(font)
        self.gaugeID.setObjectName("gaugeID")
        self.gaugeID.addItem("")
        self.gaugeID.addItem("")
        self.horizontalLayout_4.addWidget(self.gaugeID)
        self.label_pressure = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_pressure.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_pressure.setObjectName("label_pressure")
        self.horizontalLayout_4.addWidget(self.label_pressure)
        self.label_time = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_4.addWidget(self.label_time)
        self.comboBox_dynamic_or_log = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_dynamic_or_log.setObjectName("comboBox_dynamic_or_log")
        self.comboBox_dynamic_or_log.addItem("")
        self.comboBox_dynamic_or_log.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_dynamic_or_log)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.setStretch(0, 70)
        self.horizontalLayout_6.setStretch(1, 30)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_mpl = QtWidgets.QVBoxLayout()
        self.verticalLayout_mpl.setObjectName("verticalLayout_mpl")
        self.verticalLayout_2.addLayout(self.verticalLayout_mpl)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(2, 100)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_serialport.setText(_translate("MainWindow", "Serial Port"))
        self.lineEdit_savepath.setText(_translate("MainWindow", "Entry Lock Pressure Log.csv"))
        self.AutoSaveLog.setText(_translate("MainWindow", "Auto Save Log"))
        self.gaugeID.setItemText(0, _translate("MainWindow", "Entry Lock"))
        self.gaugeID.setItemText(1, _translate("MainWindow", "INFINITY"))
        self.label_pressure.setText(_translate("MainWindow", "Pressure"))
        self.label_time.setText(_translate("MainWindow", "Time"))
        self.comboBox_dynamic_or_log.setItemText(0, _translate("MainWindow", "Dynamic Data"))
        self.comboBox_dynamic_or_log.setItemText(1, _translate("MainWindow", "Log Data"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
