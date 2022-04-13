import PySimpleGUI as sg
import Logs
import Queries as q
from datetime import datetime

emp_id_setter = 0

# B Ross ddd
# This is the main file that houses all of the functionality for the GUI and application.
# This file also contains the formatting code for editing how the objects and functions appear on the
# GUI window
# Final Version 1

# PROGRESS BAR
def progress_bar():
    sg.theme('LightBlue2')
    layout = [[sg.Text('Creating your account...')],
              [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
              [sg.Cancel()]]

    window = sg.Window('Working...', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


def login():
    global emp_id_setter
    sg.theme("LightBlue2")
    layout = [[sg.Text("Log In", size=(15, 1), font=16)],
              [sg.Text("Username", size=(15, 1), font=16), sg.InputText(key='-usrnm-', font=16)],
              [sg.Text("Password", size=(15, 1), font=16), sg.InputText(key='-pwd-', password_char='*', font=16)],
              [sg.Text("Employee ID", size=(15, 1), font=16), sg.InputText(key='-emp_id-', font=16)],
              [sg.Button('Login')]]

    window = sg.Window("T.A.R.S. Login", layout, enable_close_attempted_event=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            try:
                if event == "Login":
                    check = q.loginFunction(values['-usrnm-'], values['-pwd-'], values['-emp_id-'])
                    username = check[0][1]
                    password = check[0][2]
                    emp_id_setter = check[0][0]
                    if values['-usrnm-'] == username and values['-pwd-'] == password:
                        sg.popup("Welcome!")
                        break
                    elif values['-usrnm-'] != username or values['-pwd-'] != password:
                        sg.popup("Invalid login. Try again")
            except:
                sg.popup("Invalid login. Try again")

    window.close()


def checkinOption():
    sg.theme("Darkblue1")
    layout = [[sg.Text("Equipment Check-in", justification='center', size=(40, 2), font=16)],
              [sg.Text("Serial Number", size=(15, 1), font=16), sg.InputText(key='-serialNum-', font=16)],
              [sg.Text("Employee ID", size=(15, 1), font=16), sg.InputText(key='-empID-', font=16)],
              [sg.Button('Complete Check-in', size=(17, 3), font=40)]]
    window = sg.Window("T.A.R.S. Menu - Equipment Check-in", layout, element_justification='c')
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Complete Check-in":
                q.insertIntoLogsTableIn(values['-empID-'], values['-serialNum-'])
                print("This button in the checkin option works! ")
                window.close()

    window.close()


def checkoutOption():
    sg.theme("Darkblue1")
    layout = [[sg.Text("Equipment Check-out", justification='center', size=(40, 2), font=16)],
              [sg.Text("Serial Number", size=(15, 1), font=16), sg.InputText(key='-serialNum-', font=16)],
              [sg.Text("Employee ID", size=(15, 1), font=16), sg.InputText(key='-empID-', font=16)],
              [sg.Button('Complete Check-out', size=(17, 3), font=40)]]
    window = sg.Window("T.A.R.S. Menu - Equipment Check-out", layout, element_justification='c')

    while True:
        event, values = window.read()

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Complete Check-out":
                q.insertIntoLogsTableOut(values['-empID-'], values['-serialNum-'] )
                print("This button in the checkout option works! ")
                window.close()

    window.close()

def createRecordTable():
    sg.theme("Darkblue1")
    results = q.createRecord()
    heading = ['First Name', 'Last Name', 'Time', 'Status', 'Item Name']
    counter = 0
    for i in range(len(results)):
        counter += 1
    print(counter)

    layout = [
        [sg.Table(values=results, headings=heading,max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=counter,
                  key='-record-',
                  row_height=35)]
    ]
    window = sg.Window("Check-in/Check-out Record", layout)

    while True:
        event, values = window.read()

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
    window.close()


def menuOption():
    sg.theme("Darkblue1")
    layout = [[sg.Text("Main Menu", justification='center', size=(40, 2), font=16)],
              [sg.Button('Check-In Equipment', size=(17, 3), font=16)],
              [sg.Button('Check-Out Equipment', size=(17, 3), font=16)],
              [sg.Button('Create Record', size=(17, 3), font=40)]]
    window = sg.Window("T.A.R.S. Menu Options", layout, element_justification='c')

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Check-In Equipment":
                print("This button works!")
                checkinOption()
            elif event == "Check-Out Equipment":
                print("This button works!")
                checkoutOption()
            elif event == "Create Record":
                createRecordTable()
                print("This button works!")

    window.close()


login()
menuOption()
