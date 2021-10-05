import sys
import os
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout
from services.mouse_action_record import MouseActionRecorder
from services.KeystrokeRecorder import KeystrokeRecorder
from qtwidgets import Toggle
from PyQt5.QtCore import Qt
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))

Form, Base = uic.loadUiType(os.path.join(
    current_dir, "../../ui/AvertMini/floating.ui"))


class AvertMiniWindow(Base, Form):
    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        
        for i in range(0, 6):
            recorders = ['screen', KeystrokeRecorder(), 'screenshots', 'pcap', 'window_history', MouseActionRecorder()]
            toggle = Toggle(
                bar_color=Qt.red,
                checked_color="#00FF00",
            )
            toggle.setFixedHeight(17)
            toggle.setFixedWidth(40)
            toggle.clicked.connect(partial(self.toggle_recording, toggle, recorders[i]))
            self.formLayout.replaceWidget(self.checkBox, toggle)

    def toggle_recording(self, toggle, recorder):
        if toggle:
            try:
                recorder.start()
            except Exception as e:
                raise e
        elif not toggle:
            try:
                recorder.stop()
            except Exception as e:
                raise e

    def closeEvent(self, event):
        self.closed.emit()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = AvertMiniWindow()
    w.show()
    sys.exit(app.exec_())
