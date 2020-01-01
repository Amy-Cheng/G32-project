from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from panel.panel5 import Ui_Panel5
import DataProcessing
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import twstock
import datetime
import time
import sys


class PanelFive(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelFive, self).__init__()
        self.ui = Ui_Panel5()
        self.ui.setupUi(self)
        self.ui.label.setText("股票：")
        self.ui.label_2.setText("天數(輸入數字)：")

        stocks = sorted([str(sid) for sid in DataProcessing.slist])
        stocks = [sid + " - " + DataProcessing.name_list[sid] for sid in stocks]
        self.ui.comboBox.addItems(stocks)

        self.onlyInt = QtGui.QIntValidator()
        self.ui.lineEdit.setValidator(self.onlyInt)
        self.ui.lineEdit.setText("1")

        self.ui.pushButton.setText("展示")
        self.ui.pushButton.clicked.connect(self.buttonClicked)

        self.ui.figure = plt.figure(figsize=(24, 15))
        self.ui.canvas = FigureCanvas(self.ui.figure)
        self.ui.gridLayout.addWidget(self.ui.canvas)

    def buttonClicked(self):
        sid = self.ui.comboBox.currentText().split("-")[0].strip()
        days = int(self.ui.lineEdit.text().strip())
        stockdata = twstock.realtime.get(sid)

        self.ui.label_3.setText(stockdata["info"]["name"] + "(" + sid + ")" + ":" + " 收盤價:" + \
            stockdata["realtime"]["latest_trade_price"] + " 開盤價:" + stockdata["realtime"]["open"] + \
            " 最高價:" + stockdata["realtime"]["high"] + " 最低價:" + stockdata["realtime"]["low"] + \
            " 時間:" + stockdata["info"]["time"])

        stock = twstock.Stock(sid)
        mean5 = stock.moving_average(stock.price, 5)
        mean20 = stock.moving_average(stock.price, 20)
        capacity = stock.capacity
        for j in range(len(capacity)):
            capacity[j] = int(capacity[j] / 1000)
        
        self.ui.label_4.setText("近" + str(days) + "日股價:" + str(stock.price[-days:]).strip("[]"))
        self.ui.label_5.setText("近" + str(days) + "日的五日均線" + str(mean5[-days:]).strip("[]"))
        self.ui.label_6.setText("近" + str(days) + "日的二十日均線" + str(mean20[-days:]).strip("[]"))
        self.ui.label_7.setText("近" + str(days) + "日的成交量(張)" + str(capacity[-days:]).strip("[]"))
        self.ui.label_8.setText("倒數第二天之五日均價:" + str(mean5[-2]).strip("[]") + "倒數第二天之二十日均價:" + str(mean20[-2]).strip("[]") + \
                                "最後一天之五日均價:" + str(mean5[-1]).strip("[]") + "最後一天之二十日均價:" + str(mean20[-1]).strip("[]"))
        if mean5[-2] < mean20[-2]:
            if mean5[-1]>mean20[-1]:
                self.ui.label_9.setText("五日均線突破二十日均線")
            else:
                self.ui.label_9.setText("五日均線仍然低於二十日均線")
                
        else:
            if mean5[-1] > mean20[-1]:
                self.ui.label_9.setText("五日均線仍大於二十日均線")
            else:
                self.ui.label_9.setText("五日均線跌破二十日均線")


        plt.cla()
        plt.clf()
        self.ui.figure.clf()

        ax = self.ui.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.set_title(sid)
        ax.plot(range(1, 32), stock.price)
        ax.set_xlabel("日期")
        ax.set_ylabel("日股價")

        self.ui.canvas.draw()


