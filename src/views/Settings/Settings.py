import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from qtwidgets import Toggle
from PyQt5.QtCore import Qt
from functools import partial
from services.mouse_action_record import MouseActionRecorder

current_dir = os.path.dirname(os.path.abspath(__file__))


Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Settings/Settings.ui"))


class SettingsWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		for i in range(0, 6):
			recorders = ['screen', 'keystrokes', 'screenshots', 'pcap', 'window_history', MouseActionRecorder]
			toggle = Toggle(
				bar_color=Qt.red,
            	checked_color="#00FF00",
        	)
			toggle.setFixedHeight(17)
			toggle.setFixedWidth(40)
			try:
				recorders[i].initiate()
			except:
				print('Not implemented')
			toggle.clicked.connect(partial(self.toggle_recording, toggle, recorders[i]))
			self.gridLayout_2.addWidget(toggle, i, 1)

	def toggle_recording(self, toggle, recorder):
		print("{}".format(toggle.handle_position) + ":" + recorder)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = SettingsWidget()
	w.show()
	sys.exit(app.exec_())