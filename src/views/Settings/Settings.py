import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from qtwidgets import Toggle
from PyQt5.QtCore import Qt
from functools import partial
from services.mouse_action_record import MouseActionRecorder
from services.KeystrokeRecorder import KeystrokeRecorder

current_dir = os.path.dirname(os.path.abspath(__file__))


Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Settings/Settings.ui"))


class SettingsWidget(Base, Form):
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
			self.gridLayout_2.addWidget(toggle, i, 1)

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

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = SettingsWidget()
	w.show()
	sys.exit(app.exec_())