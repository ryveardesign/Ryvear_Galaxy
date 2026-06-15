import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Add_Station import *
from Check_Stations import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ryvear Design") # setting window title
        self.resize(600,400)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        menu = self.menuBar()

        station_menu = menu.addMenu("&Stations")

        add_station_action = QAction("Install New", self)
        add_station_action.setStatusTip("Install a station")
        add_station_action.triggered.connect(self.add_station_button_clicked)
        add_station_action.setCheckable(False)
        station_menu.addAction(add_station_action)
        station_menu.addSeparator()

        chk_station_action = QAction("Get Information", self)
        chk_station_action.setStatusTip("Check a station")
        chk_station_action.triggered.connect(self.chk_station_button_clicked)
        station_menu.addAction(chk_station_action)
        station_menu.addSeparator()

        del_station_action = QAction("Remove Station", self)
        del_station_action.setStatusTip("Remove a station")
        del_station_action.triggered.connect(self.del_station_button_clicked)
        station_menu.addAction(del_station_action)
        station_menu.addSeparator()

        data_menu = menu.addMenu("&Data")

        datastore_action = QAction("Store Data", self)
        datastore_action.setStatusTip("Store Realtime Data")
        datastore_action.triggered.connect(self.data_store_button_clicked)
        datastore_action.setCheckable(False)
        data_menu.addAction(datastore_action)
        data_menu.addSeparator()

        capstore_action = QAction("Capture Data", self)
        capstore_action.setStatusTip("Screenshot Existing Data")
        capstore_action.triggered.connect(self.capture_data_button_clicked)
        data_menu.addAction(capstore_action)
        data_menu.addSeparator()

        datagraph_action = QAction("Graph Data", self)
        datagraph_action.setStatusTip("Graph Historical Data")
        datagraph_action.triggered.connect(self.graph_data_button_clicked)
        data_menu.addAction(datagraph_action)
        data_menu.addSeparator()

        help_menu = menu.addMenu("&Help")
        exit_menu = menu.addMenu("&Exit")

    def add_station_button_clicked(self, s):
        print("Install New Station")

    def chk_station_button_clicked(self, s):
        print("Checking Stations")
        Checkstation.comport_search(self)
        Checkstation.bluetooth_search(self)
        Checkstation.wifi_search(self)

    def del_station_button_clicked(self, s):
        print("Remove Station")

    def data_store_button_clicked(self, s):
        print("Store Realtime Data")

    def capture_data_button_clicked(self, s):
        print("Capture Snapshot Of Data")

    def graph_data_button_clicked(self, s):
        print("Graph Existing Data")

App = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(App.exec()) # start the app