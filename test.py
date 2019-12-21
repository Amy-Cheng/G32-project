from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from ControlPanel import Ui_MainWindow
from PanelOne import PanelOne
from PanelTwo import PanelTwo
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("ControlPanel")

        self.layout = QtWidgets.QVBoxLayout(self.ui.leftwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        self.topwidget = QtWidgets.QWidget()
        self.layout.addWidget(self.topwidget)
        self.buttonLayout = QtWidgets.QVBoxLayout(self.topwidget)

        self.pushButton1 = QtWidgets.QPushButton()
        self.pushButton1.setText("股票價量圖")
        self.buttonLayout.addWidget(self.pushButton1)
        self.pushButton2 = QtWidgets.QPushButton()
        self.pushButton2.setText("財報資料")
        self.buttonLayout.addWidget(self.pushButton2)
        self.pushButton3 = QtWidgets.QPushButton()
        self.pushButton3.setText("本益比河流圖")
        self.buttonLayout.addWidget(self.pushButton3)
        self.pushButton4 = QtWidgets.QPushButton()
        self.pushButton4.setText("籌碼相關資料")
        self.buttonLayout.addWidget(self.pushButton4)
        self.pushButton5 = QtWidgets.QPushButton()
        self.pushButton5.setText("均線資料")
        self.buttonLayout.addWidget(self.pushButton5)


        one = PanelOne()
        two = PanelTwo()

        self.layout = QtWidgets.QVBoxLayout(self.ui.rightwidget)
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.layout.addWidget(self.stackedWidget)
        self.stackedWidget.addWidget(one)
        self.stackedWidget.addWidget(two)

        self.showMaximized()

        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)
        self.pushButton4.clicked.connect(self.on_pushButton4_clicked)
        self.pushButton5.clicked.connect(self.on_pushButton5_clicked)

    def on_pushButton1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_pushButton2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_pushButton3_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_pushButton4_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

    def on_pushButton5_clicked(self):
        self.stackedWidget.setCurrentIndex(4)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
