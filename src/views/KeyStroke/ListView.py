import uuid
from posixpath import pardir
import sys
import os
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import uic, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QListWidget, QTableWidgetItem, QTableWidget, QTableView, QCheckBox, QAbstractItemView
from functools import partial
from datetime import datetime
import datetime
from PyQt5.QtCore import Qt
from db.KeystrokeDAO import KeystrokeDAO

current_dir = os.path.dirname(os.path.abspath(__file__))

data = [('image-121', datetime.datetime(2019, 5, 5, 0, 54), datetime.datetime(2019, 5, 26, 22, 51, 36), '192.2131.2131'),
        ('image-124', datetime.datetime(2019, 5, 26, 22, 51, 36),
         datetime.datetime(2019, 6, 15, 10, 22, 48), '192.2131.2131'),
        ('image-125', datetime.datetime(2019, 6, 15, 10, 22, 48),
         datetime.datetime(2019, 7, 8, 13, 33, 36), '192.2131.2131'),
        ('image-124', datetime.datetime(2019, 7, 8, 13, 33, 36),
         datetime.datetime(2019, 7, 29, 6, 18), '192.2131.2131'),
        ('image-123', datetime.datetime(2019, 7, 29, 6, 18),
         datetime.datetime(2019, 8, 6, 18, 50, 24), '192.2131.2131'),
        ('image-321', datetime.datetime(2019, 8, 6, 18, 50, 24), datetime.datetime(2019, 8, 31, 3, 14, 24), '192.2131.2131')]


Form, Base = uic.loadUiType(os.path.join(
    current_dir, "../../ui/KeyStroke/ListView.ui"))


class ListViewWidget(Base, Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi()

    def setupUi(self):

        ksDAO = KeystrokeDAO()

        KeyStrokeData = list(ksDAO.read())

        table = QTableWidget(self)
        table.setColumnCount(6)
        # Set the table headers
        table.setHorizontalHeaderLabels(
            ["Date/Time", "IP Address", "MAC Address", "Annotations", "Key", "Active Window"])
        row = 0
        table.setRowCount(len(KeyStrokeData))
        for maData in KeyStrokeData:
            timestamp = QTableWidgetItem(maData["timestamp"])
            timestamp.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 0, timestamp)

            ip = QTableWidgetItem(maData["ip_address"])
            ip.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 1, ip)

            mac = QTableWidgetItem(maData["mac_address"])
            mac.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 2, mac)

            anno = QTableWidgetItem(maData["annotations"]["note"])
            table.setItem(row, 3, anno)

            mtype = QTableWidgetItem(maData["key"])
            mtype.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 4, mtype)

            active_window = QTableWidgetItem(maData["active_window"])
            active_window.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 5, active_window)

            row = row + 1
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        #table.itemChanged.connect(self.test)

        # Display the table
        table.show()

        vbox = QVBoxLayout(self)
        vbox.addWidget(table)
        self.setLayout(vbox)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = ListViewWidget()
    w.show()
    sys.exit(app.exec_())
