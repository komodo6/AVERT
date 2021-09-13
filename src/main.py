import sys, os
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
Form, Base = uic.loadUiType(os.path.join(current_dir, "ui/main.ui"))


class MainWidget(Base, Form):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        buttons = (self.homebutton, self.keystroke, self.mouseactions, self.packetcapture, self.screenshots, self.settings)
        for i, button in enumerate(buttons):
            button.clicked.connect(partial(self.stackedWidget.setCurrentIndex, i))


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    with open("./styles/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
        
