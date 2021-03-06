#################################################################################
# Author: Abdullah Najjar
# Description: A date conversion system that converts Islamic date to Georgion
# date with a simple user interface
# Version: 1.0
# Bugs count: 0
#################################################################################
import PySimpleGUI as sg #GUI library
from hijri_converter import convert #conversion library

# GUI - Added a dark theme
sg.theme('DarkAmber')

# Layout of elements
layout = [  [sg.Text('Convert from Arabic Calender to Georg Calender: ')],
            [sg.Text('Enter Arabic date in format (DD-MM-YYYY):'), sg.InputText(key='arabic',size=(3,15)),sg.InputText(key='arabic2',size=(3,15)),sg.InputText(key='arabic3',size=(5,15))],
            [sg.Text('Enter Georg. date in format (DD-MM-YYYY):'), sg.InputText(key='georg',size=(3,15)),sg.InputText(key='georg2',size=(3,15)),sg.InputText(key='georg3',size=(5,15))],
            [sg.Output(size=(40,20))],
            [sg.Button('Arabic to Georg'),sg.Button('Georg to Arabic'), sg.Button('Cancel')]]

# Window
window = sg.Window('Date Converter', layout)

# Event Loop to process the inputs
while True:
    event, values = window.read()
    if event in(None, 'Cancel'):
        break
    if event == 'Arabic to Georg':
        arabicDay = int(values['arabic'])
        arabicMonth = int(values['arabic2'])
        arabicYear = int(values['arabic3'])
        g = convert.Hijri(arabicYear, arabicMonth, arabicDay).to_gregorian()
        n =g.day_name()
        print('The result in Georg. Calender: ', g)
        print('Day: ',n)
    if event == 'Georg to Arabic':
        georgDay = int(values['georg'])
        georgMonth = int(values['georg2'])
        georgYear = int(values['georg3'])
        h = convert.Gregorian(georgYear, georgMonth, georgDay).to_hijri()
        m = h.day_name()
        print('The result in Arabic Calender: ', h)
        print('Day: ',m)


window.close()
