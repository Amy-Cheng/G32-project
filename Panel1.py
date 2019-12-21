# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Panel1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Panel1(object):
    def setupUi(self, Panel1):
        Panel1.setObjectName("Panel1")
        Panel1.resize(400, 300)
        self.comboBox = QtWidgets.QComboBox(Panel1)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 211, 41))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Panel1)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Panel1)
        self.pushButton.setGeometry(QtCore.QRect(310, 30, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(Panel1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 780, 460))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(Panel1)
        QtCore.QMetaObject.connectSlotsByName(Panel1)

    def retranslateUi(self, Panel1):
        _translate = QtCore.QCoreApplication.translate
        Panel1.setWindowTitle(_translate("Panel1", "Form"))
        self.label.setText(_translate("Panel1", "TextLabel"))
        self.pushButton.setText(_translate("Panel1", "PushButton"))


