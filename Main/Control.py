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

root = tk.Tk()

version = 'v0.1 06/2026'

now = datetime.now()
current_time = now.strftime("%m/%d/%y %H:%M")
print(current_time)

class MainScreen(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self, root)
        datetime_label = tk.Label(root, text = current_time, font = ("Arial", 8), width = 20, height = 1)
        datetime_label.place(x = 5, y = 175)
        version_label = tk.Label(root, text = version, font = ("Arial", 8), width = 20, height = 1)
        version_label.place(x = 275, y = 175)
        self.Make_Screen()

    def Make_Screen(self):
        self.winfo_toplevel().title("Ryvear Main Page")
        system_color = root.cget('bg')
        root.configure(background=system_color)
        root.geometry("400x200+50+50")
        self.pack()

        menubar = tk.Menu(root)
        station_menu = tk.Menu(menubar, tearoff = 0)
        station_menu.add_command(label = "Add Station", command = self.AddStation)
        station_menu.add_command(label = "Remove Station", command = self.DelStation)
        station_menu.add_separator()
        station_menu.add_command(label = "Exit", command = root.quit)
        menubar.add_cascade(label = "Station", menu=station_menu)

        data_capture_menu = tk.Menu(menubar, tearoff = 0)
        data_capture_menu.add_command(label = "Select Station", command = self.DataCapture)
        data_capture_menu.add_command(label = "Select By Type", command = self.DataCapture)
        data_capture_menu.add_command(label = "Select By Location", command = self.DataCapture)
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
        root.config(menu = menubar)

        # Combobox
        sel_stationVar = tk.StringVar()
        sel_station = ttk.Combobox(root, width = 50, height = 1, textvariable = sel_stationVar)
        sel_station.place(x = 35, y = 50)
        # Adding combobox drop down list

        sel_station['values'] = (
            '',
            'Individual Stations',
            'Stations By Type',
            'Stations By Location',
        )

        refresh_button = (tk.Button(root, text = "Refresh", command = self.RefreshStationData, height = 1, width = 12))
        refresh_button.place(x = 35, y = 140)

        view_data_button = (tk.Button(root, text = "View Data", command = self.ViewStationData, height = 1, width = 12))
        view_data_button.place(x = 150, y = 140)

        exit_button = (tk.Button(root, text = "Exit", command = root.destroy, height = 1, width = 12))
        exit_button.place(x = 265, y = 140)

    def AddStation(self):
        Check_Station()

    def DelStation(self):
        print('DelStation')

    def DataCapture(self):
        print('DataCapture')

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

app = MainScreen()
root.mainloop()