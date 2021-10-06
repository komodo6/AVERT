from db.MouseActionsDAO import MouseActionsDAO
import uuid
from posixpath import pardir
import sys
import os
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QListWidget, QTableWidgetItem, QTableWidget, QTableView, QCheckBox, QAbstractItemView
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

        maDAO = MouseActionsDAO()
        MouseActionsData = list(maDAO.read())
        table = QTableWidget(self)
        table.setColumnCount(10)
        # Set the table headers
        table.setHorizontalHeaderLabels(
            ["Date/Time", "IP Address", "MAC Address", "Annotations", "Type", "X/Y Coordinates", "Pressed", "Button", "Scroll", "Active Window"])
        row = 0
        table.setRowCount(len(MouseActionsData))
        for maData in MouseActionsData:
            timestamp = QTableWidgetItem(maData["timestamp"])
            timestamp.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 0, timestamp)

            ip = QTableWidgetItem(maData["ip_address"])
            ip.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 1, ip)

            mac = QTableWidgetItem(maData["mac_address"])
            mac.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 2, mac)

            anno = QTableWidgetItem(maData["annotations"]['note'])
            table.setItem(row, 3, anno)

            mtype = QTableWidgetItem(maData["type"])
            mtype.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 4, mtype)

            coord = QTableWidgetItem(
                f"{maData['coords'][0]}, {maData['coords'][1]}")
            coord.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            table.setItem(row, 5, coord)

            pressed = QTableWidgetItem(maData["pressed"])
            pressed.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 6, pressed)

            button = QTableWidgetItem(maData["button"])
            button.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 7, button)

            scroll = QTableWidgetItem(maData["scroll"])
            scroll.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 8, scroll)

            active_window = QTableWidgetItem(maData["active_window"])
            active_window.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(row, 9, active_window)
            row = row + 1

        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.itemChanged.connect(self.test)

        # Display the table
        table.show()
        vbox = QVBoxLayout(self)
        vbox.addWidget(table)
        self.setLayout(vbox)

    def test(self, item):

        print(item.row(), item.column())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = ListViewWidget()
    w.show()
    sys.exit(app.exec_())
