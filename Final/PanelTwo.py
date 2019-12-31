from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from panel.panel2 import Ui_Panel2
import DataProcessing
import sys


class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df, parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


class PanelTwo(QtWidgets.QMainWindow):
    def __init__(self):
        super(PanelTwo, self).__init__()
        self.ui = Ui_Panel2()
        self.ui.setupUi(self)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)

        self.ui.label.setText("股票：")
        self.ui.label_2.setText("年份：")
        self.ui.label_3.setText("季：")

        # 加入各下拉選單選項
        stocks = sorted([str(sid) for sid in DataProcessing.slist])
        stocks = [sid + " - " + DataProcessing.name_list[sid] for sid in stocks]
        self.ui.comboBox.addItems(stocks)
        self.ui.comboBox_2.addItems([str(year) for year in range(108, 101, -1)])
        self.ui.comboBox_3.addItems([str(season) for season in range(1,5)])

        self.ui.pushButton.clicked.connect(self.buttonClicked)
        self.ui.pushButton.setText("選取")

    def buttonClicked(self):
        sid = int(self.ui.comboBox.currentText().split("-")[0].strip())
        year = int(self.ui.comboBox_2.currentText())
        season = int(self.ui.comboBox_3.currentText())

        self.df = DataProcessing.crwal_financial_report(sid, year, season)

        model = PandasModel(self.df)
        self.ui.tableView.setModel(model)
