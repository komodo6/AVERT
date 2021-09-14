import sys, os
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))


Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Settings/Timeline.ui"))


class TimelineWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)

		# loading image
		self.pixmap = QPixmap(os.path.join(current_dir, "../../img/timeline.png"))

		self.timelinePic.setPixmap(self.pixmap)


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = TimelineWidget()
	w.show()
	sys.exit(app.exec_())