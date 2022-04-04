import pyodbc
# B Ross dd
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Bishop Ross\PycharmProjects\CEIS400\Inventory1.accdb;')
cursor = conn.cursor()
cursor.execute('select * from inventory')

for row in cursor.fetchall():
    print(row)