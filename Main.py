import PySimpleGUI as sg
from hijri_converter import convert

#################################################################################
# Description: A date conversion system that converts Islamic date to Georgion
# date with a simple user interface.
# Bugs count: 0
# Fixes needed:
#################################################################################

#GUI
sg.theme('DarkAmber')	# Add a touch of color

# All the stuff inside your window.
layout = [  [sg.Text('Convert from Arabic Calender to Georg Calender')],
            [sg.Text('Enter Arabic date in format (YYYY/MM/DD):'), sg.InputText()],
            [sg.Text('Enter Georgion date in format (YYYY/MM/DD):'), sg.InputText()],
        #    [sg.OutputText()],
        #    [sg.OutputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Date Converter', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in(None, 'Cancel'):	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


#g = convert.Hijri(1403, 2, 17).to_gregorian()
#print(g)
# 1982-12-02

#h = convert.Gregorian(1982, 12, 2).to_hijri()
#print(h)
# 1403-02-17
