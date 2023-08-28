# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UC_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 545)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(16, 83, 149);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MC = QtWidgets.QComboBox(self.centralwidget)
        self.MC.setGeometry(QtCore.QRect(80, 50, 501, 61))
        self.MC.setStyleSheet("background-color: rgb(151, 247, 235);")
        self.MC.setObjectName("MC")
        self.MC.addItem("")
        self.MC.addItem("")
        self.MC.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 300, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(247, 145, 145);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 218, 171);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 440, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(145, 230, 151);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 380, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 235, 103);")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-50, -70, 771, 861))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/WhatsApp Image 2023-08-28 at 5.39.53 AM.jpeg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 110, 411, 371))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/WhatsApp Image 2023-08-28 at 5.42.51 AM.jpeg"))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.TC = QtWidgets.QComboBox(self.centralwidget)
        self.TC.setGeometry(QtCore.QRect(500, 220, 86, 41))
        self.TC.setStyleSheet("background-color: rgb(145, 230, 151);\n"
"background-color: rgb(249, 173, 213);")
        self.TC.setObjectName("TC")
        self.FC = QtWidgets.QComboBox(self.centralwidget)
        self.FC.setGeometry(QtCore.QRect(500, 140, 86, 41))
        self.FC.setStyleSheet("background-color: rgb(201, 148, 225);")
        self.FC.setObjectName("FC")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(350, 220, 151, 41))
        self.Output.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"gridline-color: rgb(0, 0, 0);")
        self.Output.setText("")
        self.Output.setObjectName("Output")
        self.Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(350, 140, 151, 41))
        self.Input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Input.setObjectName("Input")
        self.label_2.raise_()
        self.label_3.raise_()
        self.MC.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.TC.raise_()
        self.FC.raise_()
        self.Output.raise_()
        self.Input.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MC.setItemText(0, _translate("MainWindow", "    Length (\'u\')"))
        self.MC.setItemText(1, _translate("MainWindow", "    Mass (^w^)"))
        self.MC.setItemText(2, _translate("MainWindow", "    Temprature (>u<)"))
        self.label_4.setText(_translate("MainWindow", "Welcome to our"))
        self.label_5.setText(_translate("MainWindow", "FAM"))
        self.label_6.setText(_translate("MainWindow", "Unit Converter"))
        self.label_7.setText(_translate("MainWindow", "(farfa4a and mar2a3a)"))
        self.label_8.setText(_translate("MainWindow", "From:"))
        self.label_9.setText(_translate("MainWindow", "To:"))


