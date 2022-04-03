import PySimpleGUI as sg
import pyodbc
import Logs

sg.Window(title="T.A.R.S", layout=[[]], margins=(850, 450)).read()




def inventory_log():
    records = Logs.retrieve_logs()
    print(Logs)
