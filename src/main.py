import sys, os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow, QHBoxLayout, QFrame, QPushButton, QStackedWidget

class ExportData(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/ExportData.ui", self)

class AnnotateData(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/AnnotateData.ui", self)

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/Search.ui", self)


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
        self.Delete_Btn.clicked.connect()
        self.Search_Left_Frame_Btn.clicked.connect()
        self.Keystroke_Btn.clicked.connect()
        self.Video_Btn.clicked.connect()
        self.ScreenShot_Btn.clicked.connect()
        self.Mouse_Action_Btn.clicked.connect()
        self.NetworkData_Btn.clicked.connect()
        '''
        self.Export_Btn.clicked.connect(self.exportDataClickHandler)
        self.Annotate_Btn.clicked.connect(self.annotateDataClickHandler)
        self.Search_Left_Frame_Btn.clicked.connect(self.searchClickHandler)

        # The Code Below is to setup the various pages for changing the content pages

        # the layout to hold the QStackedWidget
        layout = QHBoxLayout()

        # Stacked Widget to Contain the content to be changed based on the coresponding button presses
        self.contentStackedWidget = QStackedWidget()

        # Adding The Export Widget
        self.ExportDataWidget = ExportData()
        self.contentStackedWidget.addWidget(self.ExportDataWidget) # index 0

        # Adding The Annotate Widget
        self.AnnotateDataWidget = AnnotateData()
        self.contentStackedWidget.addWidget(self.AnnotateDataWidget) # index 1

        # Adding The Search Widget
        self.SearchWidget = SearchWidget()
        self.contentStackedWidget.addWidget(self.SearchWidget) # index 2

        layout.addWidget(self.contentStackedWidget)
        self.Content_Container.setLayout(layout)

    def exportDataClickHandler(self):  # index 0
        self.contentStackedWidget.setCurrentIndex(0)
        print("data")

    def annotateDataClickHandler(self):  # index 1
        self.contentStackedWidget.setCurrentIndex(1)

    def searchClickHandler(self):  # index 2
        self.contentStackedWidget.setCurrentIndex(2)
        print("Search")

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