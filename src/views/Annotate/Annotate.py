import sys, os
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))

Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Annotate/AnnotateWidget.ui"))


class AnnotateWidget(Base, Form):
    closed = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        self.closed.emit()


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = AnnotateWidget()
	w.show()
	sys.exit(app.exec_())
        
