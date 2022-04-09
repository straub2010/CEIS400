import PySimpleGUI as sg
import Logs
# B Ross ddd
# This is the main file that houses all of the functionality for the GUI and application.
# This file also contains the formatting code for editing how the objects and functions appear on the
# GUI window
username = 'Bishop Ross'
password = 'Password'


def inventory_log():
    records = Logs.showLogs()
    print(Logs)

inventory_log()

#PROGRESS BAR
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
    global username,password
    sg.theme("LightBlue2")
    layout = [[sg.Text("Log In", size =(15, 1), font=16)],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-usrnm-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
            [sg.Button('Ok'),sg.Button('Cancel')]]

    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok":
                if values['-usrnm-'] == username and values['-pwd-'] == password:
                    sg.popup("Welcome!")
                    break
                elif values['-usrnm-'] != username or values['-pwd-'] != password:
                    sg.popup("Invalid login. Try again")

    window.close()
# login()

def menuOption():
    sg.theme("Darkblue1")
    layout = [[sg.Text("Main Menu", size =(40, 5), font=16)],
              [sg.Button('Check-In Equipment', size=(17,3), font=16)],
              [sg.Button('Check-Out Equipment', size=(17,3), font=16)],
              [sg.Button('Create Record', size=(17,3), font=40)]]
    window = sg.Window("Menu Options", layout,element_justification='c')

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Check-In Equipment":
                print("This button works!")
            elif event == "Check-Out Equipment":
                print("This button works!")
            elif event == "Create Record":
                print("This button works!")

    window.close()

menuOption()
