import sys
import os
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout
from functools import partial

currentView = 0

current_dir = os.path.dirname(os.path.abspath(__file__))


Form, Base = uic.loadUiType(os.path.join(
    current_dir, "../../ui/Screenshot/Screenshot.ui"))


class ScreenshotWidget(Base, Form):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.currentView = 0
        self.viewButton.clicked.connect(self.switchViews)

    def switchViews(self):
        if(self.currentView == 0):
            self.screenshotViews.setCurrentIndex(1)
            self.currentView = 1
            self.viewButton.setText("List View")
        elif(self.currentView == 1):
            self.screenshotViews.setCurrentIndex(0)
            self.currentView = 0
            self.viewButton.setText("Gallery View")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = ScreenshotWidget()
    w.show()
    sys.exit(app.exec_())
