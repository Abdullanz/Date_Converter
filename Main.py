#################################################################################
# Description: A date conversion system that converts Islamic date to Georgion
# date with a simple user interface.
# Bugs count: 0
# TODO: I need to convert the input string into seperate entitites day, month, and year then insert these values inside the conversion API. Make sure IN/OP are linked
#################################################################################
import PySimpleGUI as sg #GUI library
from hijri_converter import convert #conversion library
import re #regex library

# GUI - Added a dark theme
sg.theme('DarkAmber')

# Layout of elements
layout = [  [sg.Text('Convert from Arabic Calender to Georg Calender: ')],
            [sg.Text('Enter Arabic date in format (DD/MM/YYYY):'), sg.InputText()],
            # [sg.Text('Enter Georg. date in format (DD/MM/YYYY):'), sg.InputText()],
            [sg.Output()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

#Regex for date: ^\d{1,2}\/\d{1,2}\/\d{4}$

# Window
window = sg.Window('Date Converter', layout)

# Event Loop to process the inputs
while True:
    event, values = window.read()
    if event in(None, 'Cancel'):
        break
    if event == 'Ok':
        g = convert.Hijri(1403, 2, 17).to_gregorian()
    print('The result in Georg. Calender: ', values[0])
    # if event == 'Ok':
    #     h = convert.Gregorian(1982, 12, 2).to_hijri()
    # print('The result in Arab Calender: ', values[g])
# g - 1982-12-02
# h - 1403-02-17

window.close()
