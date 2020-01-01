from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from ControlPanel import Ui_MainWindow
from PanelOne import PanelOne
from PanelTwo import PanelTwo
from PanelThree import PanelThree
from PanelFour import PanelFour
from PanelFive import PanelFive
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("G32")
        app_icon = QtGui.QIcon()
        app_icon.addFile('G32.png', QtCore.QSize(16,8))
        self.setWindowIcon(app_icon)

        # 設定控制板切換按鈕名稱
        self.ui.pushButton1.setText("股票SMA")
        self.ui.pushButton2.setText("財報資料")
        self.ui.pushButton3.setText("籌碼相關資料")
        self.ui.pushButton4.setText("財務比率分析")
        self.ui.pushButton5.setText("均線資料")


        # 控制板設定
        one = PanelOne()
        two = PanelTwo()
        three = PanelThree()
        four = PanelFour()
        five = PanelFive()

        self.stackedWidget = QtWidgets.QStackedWidget()
        self.ui.verticalLayout_2.addWidget(self.stackedWidget)
        self.stackedWidget.addWidget(one)
        self.stackedWidget.addWidget(two)
        self.stackedWidget.addWidget(three)
        self.stackedWidget.addWidget(four)
        self.stackedWidget.addWidget(five)

        self.showMaximized()


        # 連結控制板及按鍵
        self.ui.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.ui.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.ui.pushButton3.clicked.connect(self.on_pushButton3_clicked)
        self.ui.pushButton4.clicked.connect(self.on_pushButton4_clicked)
        self.ui.pushButton5.clicked.connect(self.on_pushButton5_clicked)

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
