import sys, os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow, QHBoxLayout, QFrame,QPushButton

class OuterFrame(QMainWindow):#would not work as a QDialog for some reason had to be a QMainWindow to load
    def __init__(self):
        super(OuterFrame, self).__init__()
        loadUi(os.getcwd()+"/views/OuterFrame.ui", self)#our .ui files should be in views folder

        #Button Actions
        ''' The following lines are commented so that it compiles normally, uncomment lines or move them out of this commented area to work on the feature
        self.Min_Recording_Btn.clicked.connect()# link to function that will have resulting action in paranthesis ...connect(self.changeUi(parameter a)) and make that function in this class
        self.Hide_Left_Frame_Btn.clicked.connect()#As of now the only action that should be implemented are ones that would be changing the UI
        self.Sync_Btn.clicked.connect()
        self.Settings_Btn.clicked.connect()
        self.Visualize_Btn.clicked.connect()
        self.Transactions_Btn.clicked.connect()
        self.Export_Btn.clicked.connect()
        self.Delete_Btn.clicked.connect()
        self.Search_Left_Frame_Btn.clicked.connect()
        self.Annotate_Btn.clicked.connect()
        self.Keystroke_Btn.clicked.connect()
        self.Video_Btn.clicked.connect()
        self.ScreenShot_Btn.clicked.connect()
        self.Mouse_Action_Btn.clicked.connect()
        self.NetworkData_Btn.clicked.connect()
        '''

        # Used to add other ui elements to the other frames
        # self.Content_Container
        self.Content_Container.setStyleSheet('background: red ;')
        btn = QPushButton("Oh please god press me ")
        layout = QHBoxLayout()
        layout.addWidget(btn)

        self.Content_Container.setLayout(layout)



#main
app = QApplication(sys.argv)
MyFrame= OuterFrame()
MyFrame.show()

# Adding my test widget here

# widget = QtWidgets.QStackedWidget() # What it this
# widget.addWidget(MyFrame)
# widget.resize(1400,900)
# widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")