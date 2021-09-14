import sys, os
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont, QImage, QPixmap
from functools import partial

current_dir = os.path.dirname(os.path.abspath(__file__))

Form, Base = uic.loadUiType(os.path.join(current_dir, "../../ui/Video/VideoGrid.ui"))

class VideoGridWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
         
        # loading image
		self.pixmap = QPixmap(os.path.join(current_dir, "../../img/vid.png"))

		positions = [(i, j) for i in range(2) for j in range(4)]

		for position in positions:
			# adding image to label
			label = QLabel(self)
			label_2 = QLabel(self)
			label.setPixmap(self.pixmap)
			label_2.setText('VID_0567.MP4')
			label_2.setFont(QFont('Times', 30))
			self.layout = QVBoxLayout()
			self.layout.addWidget(label)
			self.layout.addWidget(label_2)
			self.videoGrid.addLayout(self.layout, *position)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	w = VideoGridWidget()
	w.show()
	sys.exit(app.exec_())