import uuid
from posixpath import pardir
import sys
import os
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QImage, QPixmap, QFont, QColor, QIcon, QBrush
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, QVariant, QSize
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QListWidget, QTableWidgetItem, QTableView, QCheckBox, QAbstractItemView, QLabel
from functools import partial
from datetime import datetime
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))


Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Home/Home.ui"))


data = [
    ('image-121', datetime.datetime(2019, 5, 5, 0, 54),
     datetime.datetime(2019, 5, 26, 22, 51, 36), '192.2131.2131'),
    ('image-124', datetime.datetime(2019, 5, 26, 22, 51, 36),
     datetime.datetime(2019, 6, 15, 10, 22, 48), '192.2131.2131'),
    ('image-125', datetime.datetime(2019, 6, 15, 10, 22, 48),
     datetime.datetime(2019, 7, 8, 13, 33, 36), '192.2131.2131'),
    ('image-124', datetime.datetime(2019, 7, 8, 13, 33, 36),
     datetime.datetime(2019, 7, 29, 6, 18), '192.2131.2131'),
    ('image-123', datetime.datetime(2019, 7, 29, 6, 18),
     datetime.datetime(2019, 8, 6, 18, 50, 24), '192.2131.2131'),
    ('image-321', datetime.datetime(2019, 8, 6, 18, 50, 24), datetime.datetime(2019, 8, 31, 3, 14, 24), '192.2131.2131')]


class HomeWidget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        # model = QStandardItemModel()
        # model.setHeaderData(0, Qt.Horizontal, "d")

        # # self.homeTable.setHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # model.setHorizontalHeaderLabels(
        #     ['Name', 'Timestamp', 'MAC Address', 'IP Address'])
        # model.setHeaderData(0, Qt.Horizontal,
        #                     Qt.AlignLeft, Qt.TextAlignmentRole)
        # for row in range(len(data)):
        #     for column in range(len(data[row])):
        #         item = QStandardItem(str(data[row][column]))

        #         item.setEditable(False)
        #         model.setItem(row, column, item)

        # # self.homeTable.header().setStretchLastSection(True)

        # self.homeTable.setModel(model)
        # # self.homeTable.setHeaderHidden(False)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = HomeWidget()
    w.show()
    sys.exit(app.exec_())
