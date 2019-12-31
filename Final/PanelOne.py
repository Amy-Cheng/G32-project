from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as pdr
import sys
import numpy as np
import mpl_finance as mpf
import datetime as datetime
from panel.panel1 import Ui_Panel1
import DataProcessing

class PanelOne(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelOne, self).__init__()
        self.ui = Ui_Panel1()
        self.ui.setupUi(self)
        self.ui.label.setText("股票：")

        # 設定下拉選單選項
        stocks = sorted([str(item) for item in DataProcessing.slist])
        stocks = [sid + " - " + DataProcessing.name_list[sid] for sid in stocks]
        self.ui.comboBox.addItems(stocks)

        self.ui.pushButton.setText("展示")
        self.ui.pushButton.clicked.connect(self.buttonClicked)

        # 設定股票圖呈現
        self.ui.figure = plt.figure(figsize=(24, 15))
        self.ui.canvas = FigureCanvas(self.ui.figure)
        self.ui.gridLayout.addWidget(self.ui.canvas)

    def buttonClicked(self):
        sid = self.ui.comboBox.currentText().split("-")[0].strip()

        self.ui.figure.clf()
        plt.cla()
        plt.clf()

        sma_20, sma_60, sma_120, sma_240, df = DataProcessing.stock_sma(sid)
        
        #用add_axes創建副圖框
        ax = self.ui.figure.add_axes([0.03,0.4,0.95,0.5]) #左下角座標 (0.03,0.4)，右上角座標 (0.95,0.5)
        plt.title(sid, fontsize='x-large')    
        ax2 = self.ui.figure.add_axes([0.03,0.15,0.95,0.2]) #左下角座標 (0.03,0.15)，右上角座標 (0.95,0.2)
        
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
        self.ui.canvas.draw()
