import datetime

import pyodbc
from datetime import datetime

databaseConnector = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Bishop '
    r'Ross\PycharmProjects\CEIS400\BishopsDatabase.accdb;')


# B
# Any where you see r'Driver = .....DBQ =, update the file path for the access
# Database to the file path on your local machine to allow it to function properly and execute
# the queries successfully

def retrieve_logs():
    results = []
    conn = databaseConnector
    cursor = conn.cursor()
    cursor.execute('select * from employee')
    for row in cursor:
        results.append(list(row))
    return results


def showLogs():
    result = retrieve_logs()
    for i in result:
        print(i)


def insertRecord():
    tools = ["Hammer", "Screwdriver", "Mallet", "Axe", "Saw", "Scissors", "Chisel", "Pliers", "Drill", "Tape measure",
             "Electric drill", "Circular saw", "Soldering iron", "Electric screwdriver", "Chainsaw", "Nail gun",
             "Hammer", "Screwdriver", "Mallet", "Axe", "Saw", "Wrench", "Monkeywrench", "Chisel", "Pliers", "Hacksaw",
             "Phillips screwdriver", "Hatchet", "Stepladder", "Toolbox"]
    conn = databaseConnector
    cursor = conn.cursor()
    for i in tools:
        cursor.execute(f"INSERT INTO Inventory (CLEAR_LEVEL, ITEM_NAME, STATUS) VALUES (3,'{i}', 0)")
    conn.commit()
    print("Table was updated")
insertRecord()

def insertIntoLogsTableOut(emp_id, ser_num):
    now = datetime.now()
    dateAndTime = now.strftime('%m/%d/%Y %I:%M:%S %p')
    emp_id = emp_id
    ser_num = ser_num
    conn = databaseConnector
    cursor = conn.cursor()
    print(dateAndTime)
    cursor.execute(
        f"INSERT INTO Checkout_Logs (TIME_LOG, LOG_TYPE, EMP_ID, SERIAL_NUM) "
        f"VALUES ('{dateAndTime}','checkout', {emp_id}, {ser_num});")
    cursor.execute(f'UPDATE Inventory SET STATUS = 1 WHERE SERIAL_NUM={ser_num}')
    conn.commit()
    print("Checkout Log table was updated")


def insertIntoLogsTableIn(emp_id, ser_num):
    now = datetime.now()
    emp_id = emp_id
    ser_num = ser_num
    dateAndTime = now.strftime('%m/%d/%Y %I:%M:%S %p')
    conn = databaseConnector
    cursor = conn.cursor()
    print(dateAndTime)
    cursor.execute(
        f"INSERT INTO Checkout_Logs (TIME_LOG, LOG_TYPE, EMP_ID, SERIAL_NUM) VALUES "
        f"('{dateAndTime}','checkin', {emp_id}, {ser_num});")
    cursor.execute(f'UPDATE Inventory SET STATUS = 0 WHERE SERIAL_NUM={ser_num}')
    conn.commit()
    print("Checkout Log table was updated")


def createRecord():
    results = []
    conn = databaseConnector
    cursor = conn.cursor()
    cursor.execute('''SELECT Employee.F_NAME, Employee.L_NAME, Checkout_Logs.TIME_LOG, Checkout_Logs.LOG_TYPE, 
    Inventory.ITEM_NAME FROM (Checkout_Logs INNER JOIN Employee ON Checkout_Logs.EMP_ID = Employee.EMP_ID) INNER JOIN 
    Inventory ON Checkout_Logs.SERIAL_NUM = Inventory.SERIAL_NUM ORDER BY Checkout_Logs.TIME_LOG DESC;''')
    for row in cursor:
        results.append(list(row))
    for i in results:
        print(i)
    return (results)


def loginFunction(username, password, employee_ID):
    users_info = []
    conn = databaseConnector
    cursor = conn.cursor()
    cursor.execute(f"SELECT LOGIN_DETAILS.EMP_ID, LOGIN_DETAILS.USER, LOGIN_DETAILS.PASS FROM LOGIN_DETAILS WHERE "
                   f"EMP_ID = {employee_ID} and USER = '{username}' and PASS = '{password}'")
    for row in cursor:
        users_info.append(list(row))
    return users_info
