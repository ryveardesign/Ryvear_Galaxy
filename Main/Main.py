import os
from os import path

from datetime import datetime

import openpyxl
import pytz

from openpyxl import *
from openpyxl.styles import *

from Control import MainScreen

now = datetime.now()
current_time = now.strftime("%m-%d-%y-%H%M")

file = f'StationDatabase-Rev-{current_time}.xlsx'
file_location = f'E:/OneDrive/Ryvear/Ryvear_Galaxy/Data/{file}' # set where workbook is to be created or stored or read

if os.path.isfile(file_location):
    print('file exists')
    wb = openpyxl.load_workbook(file_location) # open file if exists
else:
    wb = Workbook() # create file
    print('create file')
    ws = wb.active  # Set Active Sheet
    # Creating a workbook
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

for letter in ['A','B','C','D','E','F','G','H','J','I','K','L','M','N']:
    max_width = 24
    for i in letter:
        ws[f'{i}1'].alignment = Alignment(horizontal='center', vertical='center')
        ws[f'{i}1'].font = Font(name = 'Arial', bold = True, italic = False, size = 12, color = "000000") # Change font and color
        ws[f'{i}1'].border = Border(Side('thin'), Side('thin'), Side('thin'), Side('thin')) # Top, Left, Right, Bottom, Thick, thin, dotted, dashed
        ws.column_dimensions[f'{letter}'].width = 28

wb.save(file_location) # Save data to file

if __name__ == '__main__':
    app = MainScreen()
    app.mainloop()