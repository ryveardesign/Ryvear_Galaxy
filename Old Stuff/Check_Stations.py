from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import time
from datetime import datetime

import serial
from serial.tools import list_ports

ports = serial.tools.list_ports.comports()

class Checkstation:

    def __init__(self, ports):
        self.ports = ports
        sys_date = datetime.strptime('%Y-%m-%d').date()
        sys_time = datetime.strptime("%H:%M:%S").time()
        print(sys_date, sys_time)

    def comport_search(self):
        comportnum = []
        #for port in ports: # uncomment
        ser = serial.Serial('com7', baudrate = 115200, timeout = 2)
        try:
            if ser.isOpen():
                #comportnum.append(port.device)
                #comportnum.append(port.description)
                #comportnum.append(datetime.now().date())
                #comportnum.append(datetime.now().time())
                # station_comm = port.descrition.split() # uncomment
                #if station_comm[1] == 'CH340':
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
                    '''
                    char_data_size = int.from_bytes(rcvd_data, "big")
                    print(char_data_size)
                    time.sleep(1)  # indent for if()
                    response_data = ser.read(char_data_size)  # indent for if()
                    print(response_data) # indent for if()
                    '''
                    ser.flush()
        except serial.SerialException as e: # If error connecting move on to next port
            pass

    def bluetooth_search(self):
        print("Bluetooth is not installed")

    def wifi_search(self):
        print("No WiFi Connection")