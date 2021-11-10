# GUI.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# October 01, 2021
#

# Adapted from https://github.com/PySimpleGUI/PySimpleGUI

import PySimpleGUI as sg
from Constants import *

def launch_start(onSetup):

    # Define the window's contents
    layout = [[sg.Text("What is the user's name?")],
            [sg.Input(key=GUI_INPUT_USER_NAME)],

            [sg.Text("What is the caretakers's name?")],
            [sg.Input(key=GUI_INPUT_CARETAKER_NAME)],

            [sg.Text("What is the caretakers's 10-digit US phone number?")],
            [sg.Input(key=GUI_INPUT_CARETAKE_PHONE_NUMBER)],
            
            [sg.Text(size=(60,1), key='-OUTPUT-')],
            [sg.Button(GUI_EVENT_SEND_TEST), sg.Button(GUI_EVENT_QUIT)]]

    # Create the window
    window = sg.Window('Brace for Impact Setup', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed

        if event == sg.WINDOW_CLOSED or event == GUI_EVENT_QUIT:
            break

        if event == GUI_EVENT_SEND_TEST:
            onSetup(values[GUI_INPUT_USER_NAME], values[GUI_INPUT_CARETAKER_NAME], values[GUI_INPUT_CARETAKE_PHONE_NUMBER])

            # Output a message to the window
            check_for_SMS = GUI_FORMATTED_CONFIRM_SMS.format(values[GUI_INPUT_CARETAKER_NAME])
            window['-OUTPUT-'].update(check_for_SMS)

    # Finish up by removing from the screen
    window.close()
