import sqlite3

connection = sqlite3.connect('homework_17.11.22.db')
cursor = connection.cursor()
query = ("""  CREATE TABLE School 
              ( School_Id INTEGER NOT NULL PRIMARY KEY,
                School_Name TEXT NOT NULL,
                Place_Count INTEGER NOT NULL
              ); """)
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect('homework_17.11.22.db')
cursor = connection.cursor()
query = ("""  INSERT INTO School (School_Id , School_Name , Place_Count)
              VALUES  ('1', 'Протон', 200),
                      ('2', 'Преспектива', 300),
                      ('3', 'Спектр', 400),
                      ('4', 'Содружество', 500); """)
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect('homework_17.11.22.db')
cursor = connection.cursor()
query = """ CREATE TABLE Students
             (Student_id INTEGER NOT NULL,
              Student_Name TEXT NOT NULL,
              School_id INTEGER NOT NULL
             ); """
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect('homework_17.11.22.db')
cursor = connection.cursor()
query = """ INSERT INTO Students (Student_id, Student_Name, School_id)
             VALUES  (201, 'Иван', 1),
                     (202, 'Петр', 2),
                     (203, 'Анастасия', 3),
                     (204, 'Игорь', 4); """
cursor.execute(query)
connection.commit()
connection.close()

def get_connection():
  connection = sqlite3.connect('homework_17.11.22.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_detail(Student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """  SELECT Student_id, Student_Name, Students.School_id, School.School_Name
                        FROM Students
                        JOIN School ON Students.School_id = school.School_id
                        WHERE Student_Id = ?;

                        """
    cursor.execute(select_query, (Student_id,))
    records = cursor.fetchall()
    print ("Данные по студенту")
    for row in records:
      print ("ID студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", row[3])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по студенту ", error)


get_student_detail(201)