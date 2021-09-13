import uuid
from posixpath import pardir
import sys
import os
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import uic, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QListWidget, QTableWidgetItem, QTableView
from functools import partial
from datetime import datetime
import datetime
current_dir = os.path.dirname(os.path.abspath(__file__))

Form, Base = uic.loadUiType(os.path.join(
    current_dir, "../../ui/Screenshot/GalleryView.ui"))


data = [('imageasdasdas-121', datetime.datetime(2019, 5, 5, 0, 54), datetime.datetime(2019, 5, 26, 22, 51, 36), '192.2131.2131'),
        ('image-124', datetime.datetime(2019, 5, 26, 22, 51, 36),
         datetime.datetime(2019, 6, 15, 10, 22, 48), '192.2131.2131'),
        ('image-125', datetime.datetime(2019, 6, 15, 10, 22, 48),
         datetime.datetime(2019, 7, 8, 13, 33, 36), '192.2131.2131'),
        ('image-124', datetime.datetime(2019, 7, 8, 13, 33, 36),
         datetime.datetime(2019, 7, 29, 6, 18), '192.2131.2131'),
        ('image-123', datetime.datetime(2019, 7, 29, 6, 18),
         datetime.datetime(2019, 8, 6, 18, 50, 24), '192.2131.2131'),
        ('image-321', datetime.datetime(2019, 8, 6, 18, 50, 24), datetime.datetime(2019, 8, 31, 3, 14, 24), '192.2131.2131')]


class GalView(Base, Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        model = QStandardItemModel()

        model.setHorizontalHeaderLabels(
            ['Name', 'Timestamp', 'MAC Address', 'IP Address'])
        model.setHeaderData(0, QtCore.Qt.Horizontal,
                            QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)
        for row in range(len(data)):
            for column in range(len(data[row])):
                model.setItem(row, column, QStandardItem(
                    str(data[row][column])))

        table = QTableView()
        table.setModel(model)
        vbox = QVBoxLayout(self)
        vbox.addWidget(table)
        self.setLayout(vbox)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = GalView()
    w.show()
    sys.exit(app.exec_())