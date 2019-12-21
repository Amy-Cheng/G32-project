from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from Panel1 import Ui_Panel1
from bokeh import plotting, embed, resources
import pandas as pd
import sys


class PanelOne(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelOne, self).__init__()
        self.ui = Ui_Panel1()
        self.ui.setupUi(self)
        self.setWindowTitle("Program")
        # self.ui.label.setFont(QtGui.QFont("Arial", 12))
        # self.ui.label.setGeometry(QtCore.QRect(10, 10, 600, 200))
        self.ui.label.setText("股票：")

        choices = ["1"]
        self.ui.comboBox.addItems(choices)

        self.ui.pushButton.setText("展示")
        self.ui.pushButton.clicked.connect(self.buttonClicked)

        self.view = QtWebEngineWidgets.QWebEngineView()

        # self.ui.verticalLayout.addWidget(self.ui.pushButton)
        self.ui.verticalLayout.addWidget(self.view)

    def buttonClicked(self):
        p = plotting.figure(plot_width=300, plot_height=300)
        data = {"Day": [1, 2, 3, 4, 5], "Num": [5, 4, 3, 2, 1]}
        df = pd.DataFrame(data)
        p.hexbin(df.Day, df.Num, size=0.5)
        html = embed.file_html(p, resources.CDN, "my plot")
        self.view.setHtml(html)
