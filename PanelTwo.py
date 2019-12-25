from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from panel.panel2 import Ui_Panel2
import sys


class PanelTwo(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelTwo, self).__init__()
        self.ui = Ui_Panel2()
        self.ui.setupUi(self)
        # self.ui.label.setFont(QtGui.QFont("Arial", 12))
        # self.ui.label.setGeometry(QtCore.QRect(10, 10, 600, 200))
        self.ui.label.setText("股票：")

        self.setWindowTitle("Program")
        choices = ["台股"]
        self.ui.comboBox.addItems(choices)
        #
        # self.ui.pushButton.clicked.connect(self.buttonClicked)
        # self.ui.pushButton.setText("展示")
        #
        # self.view = QtWebEngineWidgets.QWebEngineView()
        # self.view.load(QtCore.QUrl().fromLocalFile("C:\\Users\Chen-Hao\Desktop\out.html"))
        # self.view.show()

    # def buttonClicked(self):
    #     # self.ui.label_2.setText("push")
    #     self.ui.label_2.setGeometry(QtCore.QRect(140, 190, 480, 480))
    #     self.ui.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\Chen-Hao\\Desktop\\python.png"))
