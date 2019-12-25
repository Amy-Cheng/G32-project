from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from bokeh import plotting, embed, resources
import pandas as pd
import sys

from panel.panel1 import Ui_Panel1
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import mpl_finance as mpf
import datetime as datetime
import talib

slist = [2330,2317,2454,3008,1301,2412,2891,1303,1216,2882,2886,1326,2881,3711,2884,
2308,2002,2892,1101,2207,2885,5880,2303,3045,5876,2912,2382,2880,5871,2357,
2890,2887,4938,2801,2883,3034,6505,4904,2888,2395,2301,1102,2408,1402,
9904,2409,2345,3231,2105,2324,1476,4958,2633,6239,3481,2823,2834,2049,9910,9921,
2354,2492,2377,2344,3702,2356,2353,1590,2385,2347,8464,2371,2542,2618,2603,
1227,1434,2915,9945,3105,5347,8299]

def plot_graph(sid, figure):
    plt.cla()

    start = datetime.datetime(2017,1,1)

    # 取得股票資料
    if sid in [str(slist[i]) for i in range(79, 82)]:
        df = pdr.DataReader(sid + '.TWO', 'yahoo', start=start)
    else:
        df = pdr.DataReader(sid + '.TW', 'yahoo', start=start)

    df.index = df.index.format(formatter=lambda x: x.strftime('%Y-%m-%d')) 

    sma_20 = talib.SMA(np.array(df['Close']), 20)
    sma_60 = talib.SMA(np.array(df['Close']), 60)
    sma_120 = talib.SMA(np.array(df['Close']), 120)
    sma_240 = talib.SMA(np.array(df['Close']), 240)

    # self.ui.figure = plt.figure(figsize=(24, 15))
    
    #用add_axes創建副圖框
    ax = figure.add_axes([0.03,0.4,0.95,0.5]) #左下角座標 (0.03,0.4)，右上角座標 (0.95,0.5)
    plt.title(sid, fontsize='x-large')    
    ax2 = figure.add_axes([0.03,0.15,0.95,0.2]) #左下角座標 (0.03,0.15)，右上角座標 (0.95,0.2)
    
    mpf.candlestick2_ochl(ax, df['Open'], df['Close'], df['High'],
    df['Low'], width=0.6, colorup='r', colordown='g', alpha=0.75)

    ax.plot(sma_20, label='20MA')
    ax.plot(sma_60, label='60MA')
    ax.plot(sma_120, label='120MA')
    ax.plot(sma_240, label='240MA')

    mpf.volume_overlay(ax2, df['Open'], df['Close'], df['Volume'], colorup='r', colordown= 'g', width=0.5, alpha=0.8)    
    ax2.set_xticks(range(0, len(df.index), 10))
    ax2.set_xticklabels(df.index[::10], rotation = 45)    
    
    ax.legend(loc='best', shadow=True, fontsize='x-large')

    # plt.show()



class PanelOne(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelOne, self).__init__()
        self.ui = Ui_Panel1()
        self.ui.setupUi(self)
        self.ui.label.setText("股票：")

        # 設定下拉選單選項
        stocks = [str(item) for item in slist]
        self.ui.comboBox.addItems(stocks)

        self.ui.pushButton.setText("展示")
        self.ui.pushButton.clicked.connect(self.buttonClicked)

        # 設定股票圖呈現
        self.ui.figure = plt.figure(figsize=(24, 15))
        self.ui.canvas = FigureCanvas(self.ui.figure)
        self.ui.gridLayout.addWidget(self.ui.canvas)

    def buttonClicked(self):
        sid = self.ui.comboBox.currentText()
        plot_graph(sid, self.ui.figure)
        self.ui.canvas.draw()
