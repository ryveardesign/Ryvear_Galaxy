import os
import sys

import tkinter as tk
from tkinter import ttk

import openpyxl
from openpyxl import *
from openpyxl.styles import *

from Main import station_directory, current_time, version

root = tk.Tk()

wb = openpyxl.load_workbook(station_directory)  # open file
ws = wb.active  # Set Active Sheet

def initialize_capture_window():
    def __init__(self):
        ttk.Frame.__init__(self, root)
        datetime_label = tk.Label(root, text = current_time, font = ("Arial", 8), width = 20, height = 1)
        datetime_label.place(x = 5, y = 175)
        version_label = tk.Label(root, text = version, font = ("Arial", 8), width = 20, height = 1)
        version_label.place(x = 275, y = 175)

        root.winfo_toplevel().title("Ryvear Main Page")
        system_color = root.cget('bg')
        root.configure(background=system_color)
        root.geometry("600x50+50+50")

def Single_View():
    pass
def Type_View():
    pass
def Location_View():
    pass