import PySimpleGUI as sg
import Queries as q
from datetime import datetime

emp_id_setter = 0


# B Ross
# This is the main file that houses all of the functionality for the GUI and application.
# This file also contains the formatting code for editing how the objects and functions appear on the
# GUI window
# Final Version 1

def login():
    global emp_id_setter
    sg.theme("LightBlue2")
    layout = [[sg.Text("Log In", size=(15, 1), font=16)],
              [sg.Text("Username", size=(15, 1), font=16), sg.InputText(key='-usrnm-', font=16)],
              [sg.Text("Password", size=(15, 1), font=16), sg.InputText(key='-pwd-', password_char='*', font=16)],
              [sg.Text("Employee ID", size=(15, 1), font=16), sg.InputText(key='-emp_id-', font=16)],
              [sg.Button('Login'), sg.Button('Cancel')],
              ]

    window = sg.Window("T.A.R.S. Login", layout, enable_close_attempted_event=True)

    while True:
        event, values = window.read()
        if event == "Cancel":
            return 0
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
    global emp_id_setter
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
                if values['-empID-'] != str(emp_id_setter):
                    sg.popup("Please use your Employee ID")
                else:
                    q.insertIntoLogsTableIn(values['-empID-'], values['-serialNum-'])
                    window.close()

    window.close()


def checkoutOption():
    global emp_id_setter
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
                if values['-empID-'] != str(emp_id_setter):
                    sg.popup("Please use your Employee ID")
                else:
                    q.insertIntoLogsTableOut(values['-empID-'], values['-serialNum-'])
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
        [sg.Table(values=results, headings=heading, max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=counter,
                  key='-record-',
                  row_height=20)]
    ]
    window = sg.Window("Check-in/Check-out Record", layout, location=(0, 0))

    while True:
        event, values = window.read()

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
    window.close()


def createAdvRecordTable(results_list):
    sg.theme("Darkblue1")
    results = results_list
    heading = ['First Name', 'Last Name', 'Time', 'Status', 'Item Name']
    counter = 0
    for i in range(len(results)):
        counter += 1

    layout = [
        [sg.Table(values=results, headings=heading, max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=counter,
                  key='-record-',
                  row_height=20)]
    ]
    window = sg.Window("Check-in/Check-out Record", layout, location=(0, 0))

    while True:
        event, values = window.read()

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
    window.close()


def advancedEMPSearch():
    sg.theme("Darkblue1")
    layout = [[sg.Text("Advanced Employee Record Search", justification='center', size=(40, 2), font=16)],
              [sg.Text("Employee First Name", size=(20, 1), font=16), sg.InputText(key='-fName-', font=16)],
              [sg.Text("Employee Last Name", size=(20, 1), font=16), sg.InputText(key='-lName-', font=16)],
              [sg.Text("Start of Search Date", size=(20, 1), font=16), sg.InputText(key='-date1-', font=16)],
              [sg.Text("End of Search Date", size=(20, 1), font=16), sg.InputText(key='-date2-', font=16)],
              [sg.Button('Search', size=(17, 3), font=40)]]
    window = sg.Window("T.A.R.S. Menu - Advanced Employee Search", layout, element_justification='c')

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            try:
                if event == "Search":
                    createAdvRecordTable(q.createAdvancedRecordEmp(values['-fName-'], values['-lName-'], values['-date1-'],
                                                                   values['-date2-']))
            except:
                sg.popup("Invalid search, please enter valid search parameters")

    window.close()


def advancedToolSearch():
    sg.theme("Darkblue1")
    layout = [[sg.Text("Advanced Tool Record Search", justification='center', size=(40, 2), font=16)],
              [sg.Text("Serial Number", size=(15, 1), font=16), sg.InputText(key='-sNum-', font=16)],
              [sg.Text("Start of Search Date", size=(15, 1), font=16), sg.InputText(key='-date1-', font=16)],
              [sg.Text("End of Search Date", size=(15, 1), font=16), sg.InputText(key='-date2-', font=16)],
              [sg.Button('Search', size=(17, 3), font=40)]]
    window = sg.Window("T.A.R.S. Menu - Advanced Tool Search", layout, element_justification='c')

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            try:
                if event == "Search":
                    createAdvRecordTable(q.createAdvancedRecordTool(values['-sNum-'], values['-date1-'], values['-date2-']))
            except:
                sg.popup("Invalid search, please enter valid search parameters")
    window.close()


def advancedSearch():
    sg.theme("Darkblue2")
    layout = [[sg.Text("Advanced Record Search", justification='center', size=(40, 2), font=16)],
              [sg.Button('Advanced Employee Search', size=(17, 3), font=40)],
              [sg.Button('Advanced Tool Search', size=(17, 3), font=40)]]
    window = sg.Window("T.A.R.S. Menu - Advanced Search", layout, element_justification='c')

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Advanced Employee Search":
                advancedEMPSearch()
            elif event == "Advanced Tool Search":
                advancedToolSearch()

    window.close()


def menuOption():
    sg.theme("Darkblue1")
    layout = [[sg.Text("Main Menu", justification='center', size=(40, 2), font=16)],
              [sg.Button('Check-In Equipment', size=(20, 3), font=16)],
              [sg.Button('Check-Out Equipment', size=(20, 3), font=16)],
              [sg.Button('Create Record', size=(20, 3), font=40)],
              [sg.Button('Create Advanced Record', size=(20, 3), font=40)],
              [sg.Button('Logout', size=(20, 3), font=40)]]
    window = sg.Window("T.A.R.S. Menu Options", layout, element_justification='c')

    while True:
        global emp_id_setter
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Check-In Equipment":
                checkinOption()
            elif event == "Check-Out Equipment":
                checkoutOption()
            elif event == "Create Record":
                createRecordTable()
            elif event == "Create Advanced Record":
                advancedSearch()
            elif event == "Logout":
                emp_id_setter = 0
                window.close()

    window.close()


while True:
    if login() == 0:
        break
    menuOption()
