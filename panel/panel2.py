# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Panel2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Panel2(object):
    def setupUi(self, Panel2):
        Panel2.setObjectName("Panel2")
        Panel2.resize(400, 300)
        self.label = QtWidgets.QLabel(Panel2)
        self.label.setGeometry(QtCore.QRect(30, 40, 71, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Panel2)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 201, 41))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Panel2)
        QtCore.QMetaObject.connectSlotsByName(Panel2)

    def retranslateUi(self, Panel2):
        _translate = QtCore.QCoreApplication.translate
        Panel2.setWindowTitle(_translate("Panel2", "Form"))
        self.label.setText(_translate("Panel2", "TextLabel"))


