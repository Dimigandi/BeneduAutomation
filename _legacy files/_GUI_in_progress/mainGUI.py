# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(341, 329)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(10, 230, 93, 41))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        self.button_start.setFont(font)
        self.button_start.setObjectName("button_start")
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(110, 230, 91, 41))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        self.button_stop.setFont(font)
        self.button_stop.setObjectName("button_stop")
        self.mainLogo = QtWidgets.QLabel(self.centralwidget)
        self.mainLogo.setGeometry(QtCore.QRect(10, 10, 481, 31))
        font = QtGui.QFont()
        font.setFamily("EBS주시경 Medium")
        font.setPointSize(22)
        self.mainLogo.setFont(font)
        self.mainLogo.setMouseTracking(False)
        self.mainLogo.setObjectName("mainLogo")
        self.settingBox = QtWidgets.QGroupBox(self.centralwidget)
        self.settingBox.setGeometry(QtCore.QRect(10, 60, 321, 151))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        self.settingBox.setFont(font)
        self.settingBox.setObjectName("settingBox")
        self.lineEdit_email = QtWidgets.QLineEdit(self.settingBox)
        self.lineEdit_email.setGeometry(QtCore.QRect(110, 30, 201, 21))
        self.lineEdit_email.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_email.setAutoFillBackground(False)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_Email = QtWidgets.QLabel(self.settingBox)
        self.label_Email.setGeometry(QtCore.QRect(13, 30, 91, 20))
        self.label_Email.setObjectName("label_Email")
        self.lineEdit_password = QtWidgets.QLineEdit(self.settingBox)
        self.lineEdit_password.setGeometry(QtCore.QRect(110, 70, 201, 21))
        self.lineEdit_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_password.setAutoFillBackground(False)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_Password = QtWidgets.QLabel(self.settingBox)
        self.label_Password.setGeometry(QtCore.QRect(13, 70, 91, 20))
        self.label_Password.setObjectName("label_Password")
        self.label_Delay = QtWidgets.QLabel(self.settingBox)
        self.label_Delay.setGeometry(QtCore.QRect(13, 110, 91, 20))
        self.label_Delay.setObjectName("label_Delay")
        self.spinBox_delay = QtWidgets.QSpinBox(self.settingBox)
        self.spinBox_delay.setGeometry(QtCore.QRect(110, 110, 201, 22))
        self.spinBox_delay.setMaximum(3600)
        self.spinBox_delay.setProperty("value", 320)
        self.spinBox_delay.setObjectName("spinBox_delay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BeneduAutomated"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.mainLogo.setText(_translate("MainWindow", "BeneduAutomated"))
        self.settingBox.setTitle(_translate("MainWindow", "Settings"))
        self.label_Email.setText(_translate("MainWindow", "Email"))
        self.label_Password.setText(_translate("MainWindow", "Password"))
        self.label_Delay.setText(_translate("MainWindow", "Delay (sec)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

