import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from qtwidgets import AnimatedToggle
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))


Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Settings/Settings.ui"))


class SettingsWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		for i in range(0, 6):
			toggle = AnimatedToggle(
            	checked_color="#00FF00",
            	pulse_checked_color="#00FF00",
				pulse_unchecked_color="#FF0000"
        	)
			self.gridLayout_2.addWidget(toggle, i, 1)



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = SettingsWidget()
	w.show()
	sys.exit(app.exec_())