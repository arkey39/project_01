# ООП


# Создать класс таблицы, состоящий из пустых значений.
# Таблица может: принимать новые значения, заменять существующие значения, выводить число строк и колонок.

# from pandas import DataFrame

# df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
# print(df)

from pprint import pprint

class Table:
    
    def __init__(self, rows, cols): # Инициализирует строки и столбцы
        self.rows = rows
        self.cols = cols
        self.field = [[None for i in range(rows)] for j in range(cols)]

    def get_value(self, row, col):
        try:
            return self.field[row][col]
        except IndexError: # При делении на ноль
            return None
        
        # if row in range(self.rows) and col in range(self.cols):
        #    return self.field[row][col]
        # else: # При делении на ноль
        #    return None

    def set_value(self, row, col, val): # Замена занчения в ячейке
        try:
            self.field[row][col] = val
        except IndexError:
            return None

table = Table(rows = 11, cols = 11)
print(table.rows, table.cols, table.field)
pprint(table.field)

print(table.get_value(10, 5))
table.set_value(10, 5, 1000000)
print(table.get_value(10, 5))
pprint(table.field)
