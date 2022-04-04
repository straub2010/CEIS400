import PySimpleGUI as sg
import Logs
# B Ross d
# This is the main file that houses all of the functionality for the GUI and application.
# This file also contains the formatting code for editing how the objects and functions appear on the
# GUI window
sg.Window(title="T.A.R.S", layout=[[]], margins=(850, 450)).read()


def inventory_log():
    records = Logs.showLogs()
    print(Logs)

inventory_log()