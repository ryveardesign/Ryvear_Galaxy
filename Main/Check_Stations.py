import os
import sys

import tkinter as tk
from tkinter import ttk

import openpyxl
from openpyxl import *
from openpyxl.styles import *

import time
from datetime import datetime

import serial
from serial.tools import list_ports

ports = serial.tools.list_ports.comports()

class Check_Station:
    def __init__(self):
        self.Comport_Search()

    def Comport_Search(self):
        print('Looking For New Stations On Serial Ports')
        '''
        comportnum = []
        for port in ports: # uncomment
            ser = serial.Serial('com7', baudrate = 115200, timeout = 2)
            try:
                if ser.isOpen():
                    comportnum.append(port.device)
                    comportnum.append(port.description)
                    comportnum.append(datetime.now().date())
                    comportnum.append(datetime.now().time())
                    station_comm = port.description.split() # uncomment
                    if station_comm[1] == 'CH340':
                        ser.write(b'Send Station Status')
                        ser.flush()
                        time.sleep(1) # indent for if()
                        rcvd_data = ser.read(5) # indent for if()
                        print(rcvd_data)
                        xfer_size = int(rcvd_data, 16)
                        print(xfer_size)
                        ser.flush()
                        for i in range (xfer_size):
                            rcvd_data = ser.read(2048)  # indent for if()
                            print(rcvd_data)
                            char_data_size = int.from_bytes(rcvd_data, "big")
                            print(char_data_size)
                            time.sleep(1)  # indent for if()
                            response_data = ser.read(char_data_size)  # indent for if()
                            print(response_data) # indent for if()
                            ser.flush()
            except serial.SerialException as e: # If error connecting move on to next port
            '''
        self.Bluetooth_Search()

    def Bluetooth_Search(self):
        print('Looking For New Stations On Bluetooth')
        self.Wifi_Search()

    def Wifi_Search(self):
        print('Looking For New Stations On Wifi')
        self.USB_Search()

    def USB_Search(self):
        print('Looking For New Stations On USB')