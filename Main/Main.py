import os
from pathlib import Path
import platform

from datetime import datetime

import openpyxl

from openpyxl import *
from openpyxl.styles import *

import Control

version = 'v0.1 06/2026'

now = datetime.now()
current_time = now.strftime("%m/%d/%y %H:%M")
print(current_time)

#### Check OS being used and change storage directory accordingly (Future use)
os_name = platform.system()

#### Create Filename
file = f'Station_Database.xlsx'

#### Set path to Home directory
home_path = Path.home()

#### Create Directories for Station Info and the Data Reports
station_info_directory = f'{home_path}\\Ryvear_Galaxy\\Station\\'
report_file_directory = f'{home_path}\\Ryvear_Galaxy\\Report\\'

#### Join Directory and Filename
station_directory = os.path.join(station_info_directory, file)
station_data = station_directory

#### Verify storage directories exist and if not create
if os.path.exists(station_info_directory): # if station information directory exists do nothing
    pass
else:
    os.makedirs(station_info_directory) # if directory does not exist create it

#### If file already exists open it. If ot create it
if os.path.isfile(station_directory):
    wb = openpyxl.load_workbook(station_directory) # open file if exists
else:
    wb = Workbook() # create file
    ws = wb.active  # Set Active Sheet
    # Creating a workbook titles
    ws['A1'] = 'Controller Type' # ESP32 type, STM32 type, or Microchip type
    ws['B1'] = 'Controller Version' # station firmware version
    ws['C1'] = 'Controller Address' # Comport, wifi, ble, or usb
    ws['D1'] = 'Controller Location' # Where is station located in the system
    ws['E1'] = 'Controller Type' # Station Version (Analog, Digital, Camera, Sensors)
    ws['F1'] = 'Station Added' # Date station added
    ws['G1'] = 'Station Removed' # Date removed maintained for history

    #### Set row 1 titles alignment, font, and style, borders
    for letter in ['A','B','C','D','E','F','G']:
        max_width = 24
        for i in letter:
            ws[f'{i}1'].alignment = Alignment(horizontal='center', vertical='center')
            ws[f'{i}1'].font = Font(name = 'Arial', bold = True, italic = False, size = 12, color = "000000") # Change font and color
            ws[f'{i}1'].border = Border(Side('thin'), Side('thin'), Side('thin'), Side('thin')) # Top, Left, Right, Bottom, Thick, thin, dotted, dashed
            ws.column_dimensions[f'{letter}'].width = 28
        for row in range(ws.max_row):
            ws[f'{i}1'].alignment = Alignment(horizontal='center', vertical='center')
            ws[f'{i}1'].font = Font(name = 'Arial', bold = True, italic = False, size = 8, color = "000000") # Change font and color
            ws[f'{i}1'].border = Border(Side('thin'), Side('thin'), Side('thin'), Side('thin')) # Top, Left, Right, Bottom, Thick, thin, dotted, dashed

wb.save(station_directory) # Save data to file

if __name__ == '__main__':
    app = Control.MainScreen()
    app.mainloop()