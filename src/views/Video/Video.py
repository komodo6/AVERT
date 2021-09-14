import sys, os
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel
from PyQt5.QtGui import QImage, QPixmap
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))

Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Video/VideoGrid.ui"))

class VideoWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
         
        # loading image
		self.pixmap = QPixmap(os.path.join(current_dir, "../../img/vid.png"))

		positions = [(i, j) for i in range(2) for j in range(4)]

		for position in positions:
			# adding image to label
			label = QLabel(self)
			label.setPixmap(self.pixmap)
			self.videoGrid.addWidget(label, *position)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = VideoWidget()
	w.show()
	sys.exit(app.exec_())