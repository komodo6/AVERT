import uuid
from posixpath import pardir
import sys
import os
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import uic, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QListWidget, QTableWidgetItem, QTableView, QCheckBox, QAbstractItemView
from functools import partial
from datetime import datetime
import datetime
current_dir = os.path.dirname(os.path.abspath(__file__))

data = [
    (datetime.datetime(2019, 5, 5, 0, 54), "Right Click",
     '150.3123, 54.0334', "cmd.exe", "00-15-E9-2B-99-3C"),
    (datetime.datetime(2019, 5, 5, 0, 54), "Right Click",
     '150.3123, 54.0334', "cmd.exe", "00-15-E9-2B-99-3C"),
    (datetime.datetime(2019, 5, 5, 0, 54), "Right Click",
     '150.3123, 54.0334', "cmd.exe", "00-15-E9-2B-99-3C"),
    (datetime.datetime(2019, 5, 5, 0, 54), "Right Click",
     '150.3123, 54.0334', "nc -l 2222", "00-15-E9-2B-99-3C"),
    (datetime.datetime(2019, 5, 5, 0, 54), "Right Click",
     '150.3123, 54.0334', "python3 spinner.py", "00-15-E9-2B-99-3C"),
    (datetime.datetime(2019, 5, 5, 0, 54), "Left Click",
     '150.3123, 54.0334', "htop", "00-15-E9-2B-99-3C"),
]


Form, Base = uic.loadUiType(os.path.join(
    current_dir, "../../ui/MouseActions/ListView.ui"))


class ListViewWidget(Base, Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        model = QStandardItemModel()

        model.setHorizontalHeaderLabels(
            ['Date/Time', 'Type', 'X,Y Coordinates', 'Process', 'MAC Address'])
        model.setHeaderData(0, QtCore.Qt.Horizontal,
                            QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)
        for row in range(len(data)):
            for column in range(len(data[row])):
                item = QStandardItem(str(data[row][column]))

                item.setEditable(False)
                model.setItem(row, column, item)

        table = QTableView()

        table.setModel(model)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        vbox = QVBoxLayout(self)
        vbox.addWidget(table)
        self.setLayout(vbox)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = ListViewWidget()
    w.show()
    sys.exit(app.exec_())
