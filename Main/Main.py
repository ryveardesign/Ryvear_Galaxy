import os
from pathlib import Path
import platform

from datetime import datetime

import openpyxl
import pytz

from openpyxl import *
from openpyxl.styles import *

from Control import MainScreen

global file_directories # create Global variable for other code to use when writing to associated data files

#### Check OS being used and change storage directory accordingly (Future use)
os_name = platform.system()

#### Create Filename
now = datetime.now()
current_time = now.strftime("%m-%d-%y-%H-%M")
file = f'StationDatabase-Rev-{current_time}.xlsx'

#### Set path to Home directory
home_path = Path.home()

#### Create Directories for Station Info and the Data Reports
station_info_directory = f'{home_path}\\Ryvear_Galaxy\\Station\\'
report_file_directory = f'{home_path}\\Ryvear_Galaxy\\Report\\'

#### Join Directory and Filename
station_directory = os.path.join(station_info_directory, file)
print(station_directory)

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
    ws['A1'] = 'Controller Type'
    ws['B1'] = 'Controller Version'
    ws['C1'] = 'Controller Address'
    ws['D1'] = 'Controller Location'
    ws['E1'] = 'Controller Data #1'
    ws['F1'] = 'Controller Data #2'
    ws['G1'] = 'Controller Data #3'
    ws['H1'] = 'Controller Data #4'
    ws['I1'] = 'Controller Data #5'
    ws['J1'] = 'Controller Data #6'
    ws['K1'] = 'Controller Data #7'
    ws['L1'] = 'Controller Data #8'
    ws['M1'] = 'Controller Data #9'
    ws['N1'] = 'Controller Data #10'

#### Set row 1 titles alignment, font, and style, borders
for letter in ['A','B','C','D','E','F','G','H','J','I','K','L','M','N']:
    max_width = 24
    for i in letter:
        ws[f'{i}1'].alignment = Alignment(horizontal='center', vertical='center')
        ws[f'{i}1'].font = Font(name = 'Arial', bold = True, italic = False, size = 12, color = "000000") # Change font and color
        ws[f'{i}1'].border = Border(Side('thin'), Side('thin'), Side('thin'), Side('thin')) # Top, Left, Right, Bottom, Thick, thin, dotted, dashed
        ws.column_dimensions[f'{letter}'].width = 28

wb.save(station_directory) # Save data to file

if __name__ == '__main__':
    app = MainScreen()
    app.mainloop()