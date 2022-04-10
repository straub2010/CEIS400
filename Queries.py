import datetime

import pyodbc
from datetime import datetime

# Any where you see r'Driver = .....DBQ =, update the file path for the access
# Database to the file path on your local machine to allow it to function properly and execute
# the queries successfully

def retrieve_logs():
    results = []
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Bishop Ross\PycharmProjects\CEIS400\BishopsDatabase.accdb;')
    cursor = conn.cursor()
    cursor.execute('select * from employee')
    for row in cursor:
        results.append(list(row))
    return results


def showLogs():
    result = retrieve_logs()
    for i in result:
        print(i)


def updateTable():
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Bishop Ross\PycharmProjects\CEIS400\BishopsDatabase.accdb;')
    cursor = conn.cursor()
    cursor.execute('UPDATE Inventory SET STATUS = 0 WHERE SERIAL_NUM=3')
    conn.commit()
    print("Table was updated")


def insertRecord():
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Bishop Ross\PycharmProjects\CEIS400\BishopsDatabase.accdb;')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Inventory (CLEAR_LEVEL, ITEM_NAME, STATUS)
     VALUES (3,'Buzzsaw', 1)''')
    conn.commit()
    print("Table was updated")


def insertIntoLogsTable():
    now = datetime.now()
    dateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Bishop Ross\PycharmProjects\CEIS400\BishopsDatabase.accdb;')
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO Checkout_Logs (TIME_LOG, LOG_TYPE, EMP_ID, SERIAL_NUM)'
                   f'')


