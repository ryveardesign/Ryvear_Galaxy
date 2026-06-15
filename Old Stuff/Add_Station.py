from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import time
from datetime import datetime

import serial
from serial.tools import list_ports

ports = serial.tools.list_ports.comports()

class Addstation:

    def __init__(self, ports):
        self.ports = ports
        sys_date = datetime.strptime('%Y-%m-%d').date()
        sys_time = datetime.strptime("%H:%M:%S").time()
        print(sys_date, sys_time)

    def comport_search(self):
        comportnum = []
        for port in ports:
            try:
                ser = serial.Serial(port.device, timeout=5)
                if ser.isOpen():
                    comportnum.append(port.device)
                    comportnum.append(port.description)
                    comportnum.append(datetime.now().date())
                    comportnum.append(datetime.now().time())
                    station_comm = port.description.split()
                    if station_comm[1] == 'CH340':
                        remove_start_char = station_comm[2].replace('(', '"')
                        station_port_location = remove_start_char.replace(')', '"')
                        print(station_port_location)
            except serial.SerialException as e: # If error connecting move on to next port
                pass

    def bluetooth_search(self):
        print("Bluetooth is not installed")

    def wifi_search(self):
        print("No WiFi Connection")