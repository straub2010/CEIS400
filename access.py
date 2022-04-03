import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\strau\OneDrive\Desktop\Inventory1.accdb;')
cursor = conn.cursor()
cursor.execute('select * from inventory')

for row in cursor.fetchall():
    print(row)