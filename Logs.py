import pyodbc


# This file contains the function to retrieve information from our access database while utilizing the GUI
# B Ross

# This is Straub's directory path for the access file: C:\Users\strau\OneDrive\Desktop\Inventory1.accdb
# This is Bishop's directory path for the access file: C:\Users\Bishop Ross\PycharmProjects\CEIS400\Inventory1.accdb
def retrieve_logs():
    results = []
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Bishop Ross\PycharmProjects\CEIS400\Inventory1.accdb;')
    cursor = conn.cursor()
    cursor.execute('select * from inventory')
    for row in cursor:
        results.append(list(row))
    return results

def showLogs():
    result = retrieve_logs()
    for i in result:
        print(i)


showLogs()