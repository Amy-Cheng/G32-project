# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlPanel.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.rightwidget = QtWidgets.QWidget(self.centralwidget)
        self.rightwidget.setGeometry(QtCore.QRect(297, 10, 1051, 801))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightwidget.sizePolicy().hasHeightForWidth())
        self.rightwidget.setSizePolicy(sizePolicy)
        self.rightwidget.setObjectName("rightwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.rightwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1051, 801))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.leftwidget = QtWidgets.QWidget(self.centralwidget)
        self.leftwidget.setGeometry(QtCore.QRect(20, 10, 271, 801))
        self.leftwidget.setObjectName("leftwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.leftwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 241, 235))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.verticalLayout_2.addWidget(self.pushButton1)
        self.pushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout_2.addWidget(self.pushButton2)
        self.pushButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton3.setObjectName("pushButton3")
        self.verticalLayout_2.addWidget(self.pushButton3)
        self.pushButton4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton4.setObjectName("pushButton4")
        self.verticalLayout_2.addWidget(self.pushButton4)
        self.pushButton5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton5.setObjectName("pushButton5")
        self.verticalLayout_2.addWidget(self.pushButton5)
        spacerItem1 = QtWidgets.QSpacerItem(236, 58, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftwidget.raise_()
        self.rightwidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "PushButton"))
        self.pushButton2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton5.setText(_translate("MainWindow", "PushButton"))


