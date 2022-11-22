import sqlite3

connection = sqlite3.connect('teatcherss.db')
cursor = connection.cursor()

cursor.execute("""  SELECT * FROM Students  """)
columnname = cursor.description     # Описание таблицы
# print(columnname)

for i in columnname:
    print(i[0])