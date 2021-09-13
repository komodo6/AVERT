
import sys, os
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))


Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/MouseActions/MouseActions.ui"))


class MouseActionsWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = MouseActionsWidget()
	w.show()
	sys.exit(app.exec_())