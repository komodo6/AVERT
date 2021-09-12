
import sys, os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow, QHBoxLayout, QFrame, QPushButton, QStackedWidget

class SyncWidget(QWidget): # index 0
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/SyncWidget.ui", self)

class SettingsWidget(QWidget): # index 1
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/SettingsWidget.ui", self)

class VisualizationWidget(QWidget): # index 2
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/VisualizationWidget.ui", self)

class TransactionWidget(QWidget): # index 3
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/TransactionWidget.ui", self)


class ExportWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/ExportWidget.ui", self)

class DeleteWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/DeleteWidget.ui", self)

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/SearchWidget.ui", self)

class AnnotateData(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/AnnotateWidget.ui", self)

class TimelineWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/TimelineWidget.ui", self)

class BarGraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/BarGraphWidget.ui", self)

class PieChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/PieChartWidget.ui", self)

class CpuUsageWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/CpuUsageWidget.ui", self)

class VideoListWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/VideoListWidget.ui", self)

class VideoGraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd() + "/views/VideoGridWidget.ui", self)

class OuterFrame(QMainWindow):#would not work as a QDialog for some reason had to be a QMainWindow to load
    def __init__(self):
        super(OuterFrame, self).__init__()
        loadUi(os.getcwd()+"/views/OuterFrameMainWindow.ui", self)#our .ui files should be in views folder

        #Button Actions
        ''' The following lines are commented so that it compiles normally, uncomment lines or move them out of this commented area to work on the feature
        self.Min_Recording_Btn.clicked.connect()# link to function that will have resulting action in paranthesis ...connect(self.changeUi(parameter a)) and make that function in this class
        self.Hide_Left_Frame_Btn.clicked.connect()#As of now the only action that should be implemented are ones that would be changing the UI
        self.Delete_Btn.clicked.connect()
        self.Search_Left_Frame_Btn.clicked.connect()
        self.Keystroke_Btn.clicked.connect()
        self.ScreenShot_Btn.clicked.connect()
        self.Mouse_Action_Btn.clicked.connect()
        self.NetworkData_Btn.clicked.connect()
        '''

        # The Code Below is to setup the various pages for changing the content pages

        # the layout to hold the QStackedWidget
        layout = QHBoxLayout()

        # Stacked Widget to Contain the content to be changed based on the coresponding button presses
        self.contentStackedWidget = QStackedWidget()

        # Adding the Sync Widget - Index 0
        self.SyncWidget = SyncWidget()
        self.contentStackedWidget.addWidget(self.SyncWidget)
        self.Sync_Btn.clicked.connect(self.syncWidgetClickHandler)

        # Adding the Settings Widget - Index 1
        self.SettingsWidget = SettingsWidget()
        self.contentStackedWidget.addWidget(self.SettingsWidget)
        self.Settings_Btn.clicked.connect(self.settingsWidgetClickHandler)

        # Adding the Visualization Widget - Index 2
        self.VisualizationWidget = VisualizationWidget()
        self.contentStackedWidget.addWidget(self.VisualizationWidget)
        self.Visualize_Btn.clicked.connect(self.visualizationWidgetClickHandler)

        # Adding the Transaction Widget - Index 3
        self.TransactionWidget = TransactionWidget()
        self.contentStackedWidget.addWidget(self.TransactionWidget)
        self.Transactions_Btn.clicked.connect(self.transactionWidgetClickHandler)

        # Adding The Export Widget - Index 4
        self.ExportDataWidget = ExportWidget()
        self.contentStackedWidget.addWidget(self.ExportDataWidget)
        self.Export_Btn.clicked.connect(self.exportWidgetClickHandler)
        #

        # Adding The Delete Widget - Index 5
        self.DeleteWidget = DeleteWidget()
        self.contentStackedWidget.addWidget(self.DeleteWidget)
        self.Delete_Btn.clicked.connect(self.deleteClickHandler)

        # Adding The Search Widget - Index 6
        self.SearchWidget = SearchWidget()
        self.contentStackedWidget.addWidget(self.SearchWidget)
        self.Search_Left_Frame_Btn.clicked.connect(self.searchClickHandler)

        # Adding The Annotate Widget - Index 7
        self.AnnotateDataWidget = AnnotateData()
        self.contentStackedWidget.addWidget(self.AnnotateDataWidget)
        self.Annotate_Btn.clicked.connect(self.annotateDataClickHandler)

        # The Code Below is to setup the various pages for changing the visualization page
        # Adding the Timeline Widget - Index 8
        self.TimelineWidget = TimelineWidget()
        self.contentStackedWidget.addWidget(self.TimelineWidget)
        self.VisualizationWidget.Timeline.clicked.connect(self.timelineClickHandler)

        # Adding the Timeline Widget - Index 9
        self.BarGraphWidget = BarGraphWidget()
        self.contentStackedWidget.addWidget(self.BarGraphWidget)
        self.VisualizationWidget.Bar_Graph.clicked.connect(self.barGarphClickHandler)

        # Adding the Pie Chart Widget - Index 10
        self.PieChartWidget = PieChartWidget()
        self.contentStackedWidget.addWidget(self.PieChartWidget)
        self.VisualizationWidget.Pie_Chart.clicked.connect(self.pieChartClickHandler)

        # Adding the Pie Chart Widget - Index 11
        self.CpuUsageWidget = CpuUsageWidget()
        self.contentStackedWidget.addWidget(self.CpuUsageWidget)
        self.VisualizationWidget.CPU_Usage.clicked.connect(self.cpuUsageClickHandler)

        # Below are for the Video Widgets 12 and 13
        self.VideoListWidget = VideoListWidget()
        self.contentStackedWidget.addWidget(self.VideoListWidget)
        self.Video_Btn.clicked.connect(self.videoListWidgetClickHandler)

        self.VideoGridWidget = VideoGraphWidget()
        self.contentStackedWidget.addWidget(self.VideoGridWidget)
        self.VideoListWidget.Grid_View.clicked.connect(self.videoGridWidgetClickHandler)

        self.VideoGridWidget.List_View.clicked.connect(self.videoListWidgetClickHandler)




        layout.addWidget(self.contentStackedWidget)
        self.Content_Container.setLayout(layout)

    def syncWidgetClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(0)

    def settingsWidgetClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(1)

    def visualizationWidgetClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(2)

    def transactionWidgetClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(3)


    def exportWidgetClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(4)

    def deleteClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(5)

    def searchClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(6)
        print("Search")

    def annotateDataClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(7)

    def timelineClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(8)

    def barGarphClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(9)

    def pieChartClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(10)

    def cpuUsageClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(11)

    def videoListWidgetClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(12)

    def videoGridWidgetClickHandler(self):
        self.contentStackedWidget.setCurrentIndex(13)



#main
app = QApplication(sys.argv)
MyFrame = OuterFrame()
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