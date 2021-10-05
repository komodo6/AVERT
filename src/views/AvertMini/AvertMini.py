import sys, os
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from src.services.mouse_action_record import MouseActionRecorder
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))

Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/AvertMini/floating.ui"))


class AvertMiniWindow(Base, Form):
    closed = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.mouse_action_recorder = MouseActionRecorder()
        self.mouse_action_recorder.initiate()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.start_stop_handler('record'))  # this is the record button
        self.pushButton_3.clicked.connect(lambda: self.start_stop_handler('stop'))  # this is the stop button

    def closeEvent(self, event):
        self.closed.emit()

    def start_stop_handler(self,type):
        if type == 'record':
            print("recording")
            self.mouse_action_recorder.start()
        if type == 'stop':
            print('stop recording')
            self.mouse_action_recorder.stop()


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = AvertMiniWindow()
	w.show()
	sys.exit(app.exec_())
        
