# Создание таблицы

import sqlite3

connection = sqlite3.connect('teachers.db') # Подключаюсь к БД
cursor = connection.cursor() # Определяю курсор
query = """ CREATE TABLE School 
            (
            School_Id INTEGER NOT NULL PRIMARY KEY,
            School_Name TEXT NOT NULL,
            Place_Count INTEGER NOT NULL
            );
        """ # Создаю переменную с SQL запросом
cursor.execute(query) # С помощью запроса выполняю SQL запрос
connection.commit() # Закрепляю изменения в БД
connection.close() # Отключаюсь от БД