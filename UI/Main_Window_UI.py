# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.Images import source_rc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(786, 654)
        Form.setStyleSheet("background-color: rgb(56, 56, 56);\n"
"border-image: url(:/plane_border/plane.png);")
        self.lbllogo = QtWidgets.QLabel(Form)
        self.lbllogo.setGeometry(QtCore.QRect(100, -20, 801, 221))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbllogo.setFont(font)
        self.lbllogo.setStyleSheet("border-image: url(:/logo/source.qrc);\n"
"")
        self.lbllogo.setObjectName("lbllogo")
        self.btnRunCrawler = QtWidgets.QPushButton(Form)
        self.btnRunCrawler.setGeometry(QtCore.QRect(350, 540, 161, 61))
        self.btnRunCrawler.setStyleSheet("border-image: url(:/logo/source.qrc);\n"
"background-color: rgb(172, 172, 172);\n"
"")
        self.btnRunCrawler.setObjectName("btnRunCrawler")
        self.btnShowData = QtWidgets.QPushButton(Form)
        self.btnShowData.setGeometry(QtCore.QRect(540, 540, 161, 61))
        self.btnShowData.setStyleSheet("border-image: url(:/logo/source.qrc);\n"
"background-color: rgb(172, 172, 172);")
        self.btnShowData.setObjectName("btnShowData")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbllogo.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#655f70;\">SkyScanner</span></p></body></html>"))
        self.btnRunCrawler.setText(_translate("Form", "Run Crawler"))
        self.btnShowData.setText(_translate("Form", "Show data"))

