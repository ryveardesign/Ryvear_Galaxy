import os
import sys
import time
from datetime import datetime

import tkinter as tk
from tkinter import ttk

import openpyxl
from openpyxl import *
from openpyxl.styles import *

from Check_Stations import *
from Del_Station import *
from Add_Station import *
from Data_Capture import *
from Main import station_directory

root = tk.Tk()

version = 'v0.1 06/2026'

now = datetime.now()
current_time = now.strftime("%m/%d/%y %H:%M")
print(current_time)

class MainScreen(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self, root)
        datetime_label = tk.Label(root, text = current_time, font = ("Arial", 8), width = 20, height = 1)
        datetime_label.place(x = 175, y = 10)
        version_label = tk.Label(root, text = version, font = ("Arial", 8), width = 20, height = 1)
        version_label.place(x = 0, y = 10)
        self.Make_Screen()

    def Make_Screen(self):
        self.winfo_toplevel().title("Ryvear Main Page")
        system_color = root.cget('bg')
        root.configure(background=system_color)
        root.geometry("300x50+50+50")
        self.pack()

        menubar = tk.Menu(root)
        station_menu = tk.Menu(menubar, tearoff = 0)
        station_menu.add_command(label = "Add Station", command = self.AddStation)
        station_menu.add_command(label = "Remove Station", command = self.DelStation)
        menubar.add_cascade(label = "Station", menu=station_menu)

        data_capture_menu = tk.Menu(menubar, tearoff = 0)
        data_capture_menu.add_command(label = "Select Station", command = lambda:self.DataCapture(1))
        data_capture_menu.add_command(label = "Select By Type", command = lambda:self.DataCapture(2))
        data_capture_menu.add_command(label = "Select By Location", command = lambda:self.DataCapture(3))
        menubar.add_cascade(label = "Data Capture", menu=data_capture_menu)

        data_review_menu = tk.Menu(menubar, tearoff = 0)
        data_review_menu.add_command(label = "Station History", command = self.DataStore)
        data_review_menu.add_command(label = "History By Type", command = self.DataStore)
        data_review_menu.add_command(label = "History By Location", command = self.DataStore)
        menubar.add_cascade(label = "Data Review", menu = data_review_menu)

        help_menu = tk.Menu(menubar, tearoff = 0)
        help_menu.add_command(label = "Local Help Document", command = self.HelpLocal)
        help_menu.add_command(label = "Online Help Document", command = self.HelpOnline)
        help_menu.add_command(label = "Tech Support", command = self.TechSupport)
        help_menu.add_command(label = "Version Information", command = self.Version)
        help_menu.add_command(label = "Contact Information", command = self.Contact)
        menubar.add_cascade(label = "Help", menu = help_menu)

        quit_menu = tk.Menu(menubar, tearoff=0)
        quit_menu.add_command(label = "Quit", command = self.Exit)
        menubar.add_cascade(label = "Quit", menu = quit_menu)

        root.config(menu = menubar)

    def AddStation(self):
        Add_Station()

    def DelStation(self):
        Del_Station()

    def DataCapture(self, data_type):
        if data_type == 1:
            Single_View()
        elif data_type == 2:
            Type_View()
        else:
            Location_View()

    def DataStore(self):
        print('DataStore')

    def HelpLocal(self):
        print('HelpLocal')

    def HelpOnline(self):
        print('HelpOnline')

    def TechSupport(self):
        print('TechSupport')

    def Version(self):
        print('Version')

    def Contact(self):
        print('Contact')

    def RefreshStationData(self):
        print('RefreshStationData')

    def ViewStationData(self):
        print('ViewStationData')

    def Exit(self):
        print('Exit')

app = MainScreen()
root.mainloop()