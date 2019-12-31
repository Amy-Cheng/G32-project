from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from panel.panel3 import Ui_Panel3
import requests
import pandas as pd
from bokeh import embed, resources
from bokeh.plotting import figure, output_file, show
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
import DataProcessing
import sys


class PanelThree(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelThree, self).__init__()
        self.ui = Ui_Panel3()
        self.ui.setupUi(self)
        self.ui.label.setText("股票：")
        self.ui.label_2.setText("選擇日期：")

        stocks = sorted([str(sid) for sid in DataProcessing.slist])
        stocks = [sid + " - " + DataProcessing.name_list[sid] for sid in stocks]
        self.ui.comboBox.addItems(stocks)

        self.ui.pushButton.setText("展示")
        self.ui.pushButton.clicked.connect(self.buttonClicked)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.ui.gridLayout.addWidget(self.view)

    def buttonClicked(self):
        date = self.ui.calendarWidget.selectedDate().toString("yyyyMMdd")
        sid = self.ui.comboBox.currentText().split("-")[0].strip()

        x_axis, foreign_investors, foreign_dealers, investment_trust, local_dealers = DataProcessing.chip_data(date, sid)

        p = figure(title="各方買賣超股數", plot_width=1350, plot_height=900)
        # 畫出4條綫代表各自的資料
        p.line(x_axis, foreign_investors, legend="外陸資買賣超股數", line_color="red")
        p.line(x_axis, foreign_dealers, legend="外資自營商買賣超股數", line_color="blue")
        p.line(x_axis, investment_trust, legend="投信買賣超股數", line_color="green")
        p.line(x_axis, local_dealers, legend="自營商買賣超股數", line_color="#9B870C")
        # 標上軸名
        p.legend.location = "top_left"
        p.xaxis.axis_label = '日期'
        p.yaxis.axis_label = '股數'

        html = embed.file_html(p, resources.CDN, "my plot")

        self.view.setHtml(html)
