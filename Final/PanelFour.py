from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from panel.panel4 import Ui_Panel4
import DataProcessing
import pandas as pd
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sys


class PanelFour(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelFour, self).__init__()
        self.ui = Ui_Panel4()
        self.ui.setupUi(self)
        self.ui.label.setText("股票：")
        self.ui.label_2.setText("類別及計算比率：")

        stocks = sorted([str(sid) for sid in DataProcessing.slist])
        stocks = [sid + " - " + DataProcessing.name_list[sid] for sid in stocks]
        self.ui.comboBox.addItems(stocks)
        self.ui.comboBox_2.addItems(["財務結構-負債佔資產比率(%)", "財務結構-長期資金佔不動產、廠房及設備比率(%)", 
            "償債能力-流動比率(%)", "償債能力-速動比率(%)", "償債能力-利息保障倍數(%)", "經營能力-應收款項週轉率(次)",
            "經營能力-平均收現日數 經營能力-存貨週轉率(次)", "經營能力-平均售貨日數 經營能力-不動產、廠房及設備週轉率(次)",
            "經營能力-總資產週轉率(次)", "獲利能力-資產報酬率(%)", "獲利能力-權益報酬率(%)", "獲利能力-稅前純益佔實收資本比率(%)",
            "獲利能力-純益率(%)", "獲利能力-每股盈餘(元)", "現金流量-現金流量比率(%)",  "現金流量-現金流量允當比率(%)", "現金流量-現金再投資比率(%)"])


        self.ui.pushButton.setText("展示")
        self.ui.pushButton.clicked.connect(self.buttonClicked)

        self.ui.figure = plt.figure(figsize=(24, 15))
        self.ui.canvas = FigureCanvas(self.ui.figure)
        self.ui.gridLayout.addWidget(self.ui.canvas)

    def buttonClicked(self):
        plt.cla()
        plt.clf()
        self.ui.figure.clf()

        sid = self.ui.comboBox.currentText().split("-")[0].strip()
        cat_rat = self.ui.comboBox_2.currentText()

        df_ratios = DataProcessing.ratios(int(sid), cat_rat)
        
        ax = self.ui.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.set_title(sid)
        ax.plot(df_ratios["Years"], df_ratios["Ratios"])
        ax.set_xlabel("Year")
        ax.set_ylabel("Ratio")

        self.ui.canvas.draw()

        year = "  102,   103,   104,   105,   106,   107"
        ratio = [item for item in df_ratios["Ratios"]]
        self.ui.label_3.setText("年份： " + year)
        self.ui.label_4.setText("比率： " + str(ratio).strip("[]"))
