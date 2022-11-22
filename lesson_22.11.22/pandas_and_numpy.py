import pandas as pd 
import numpy as np 

# Series - список с индексами
x = pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'] )
# print(x)
# print(round(x['a'], 2))


# DataFrame - таблица
df = pd.DataFrame(  np.random.randn(5, 3),
                    index = pd.date_range('22/11/2022', periods = 5),   # строки
                    columns = ['A', 'B', 'C'])                          # колонки
# print(df)

# Открытие файлов Excel
x1 = pd.read_excel("data.xlsx", sheet_name = 'Sheet1')
# print(x1)
# x1.describe(include = [object]) # Описание таблицы, включая: 
                                # самое часто встречающееся значение, уникальные значения

# Замена значений в Серии
s = pd.Series([1, 2, 3, 4, 5])  # Если не указать индексы, то они назначатся автоматически
s = s.replace(1, 'test')
# print(s)

# Замена значений в таблице
df1 = pd.DataFrame({ 'A': [0, 1, 2, 3, 4],
                    'B': [5, 6, 7, 8, 9],
                    'C': ['a', 'b', 'c', 'd', 'e']})        
df1 = df1.replace(5, 10) # Находит значение, и меняет на указанное
# print(df1)

# Поиск значений
#print(df1[df1['A'] == 2])

# Запись датафрейма в файл
df1.to_excel('test.xlsx')
df1.to_csv('test.csv')

