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

data = [('packet-121', datetime.datetime(2019, 5, 5, 0, 54)),
        ('packet-121', datetime.datetime(2019, 5, 5, 0, 54)),
        ('packet-121', datetime.datetime(2019, 5, 5, 0, 54)),
        ('packet-121', datetime.datetime(2019, 5, 5, 0, 54)),
        ('packet-121', datetime.datetime(2019, 5, 5, 0, 54)),
        ('packet-121', datetime.datetime(2019, 5, 5, 0, 54)),
        ('packet-121', datetime.datetime(2019, 5, 5, 0, 54))]


Form, Base = uic.loadUiType(os.path.join(
    current_dir, "../../ui/PacketCapture/PacketCaptureTable.ui"))


class PacketCaptureTableWidget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        model = QStandardItemModel()

        model.setHorizontalHeaderLabels(
            ['Name', 'Timestamp'])
        model.setHeaderData(0, QtCore.Qt.Horizontal,
                            QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)

        for row in range(len(data)):
            for column in range(len(data[row])):
                item = QStandardItem(str(data[row][column]))
                # item.setSelectable(True)
                # item.setCheckable(True)
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
    w = PacketCaptureTableWidget()
    w.show()
    sys.exit(app.exec_())
