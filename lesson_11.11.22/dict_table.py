# ООП

# Создать таблицу, которая будет принимать список колонок и словари в качестве строк

class Table:
    
    def __init__(self, cols):
        self.cols = cols
        self.rows = []

    def add_rows(self, row):
        if any(col not in tuple(row) for col in self.cols):
            print('Такой колонки нет!')
        self.rows.append(row)

    def get_column(self, col):
        if col not in self.cols:
            return None
        return [row[col] for row in self.rows]


table = Table(['a', 'b'])
table.add_rows({'a': 1, 'b': 2})
table.add_rows({'a': 2, 'b': 4})
table.add_rows({'a': 3, 'b': 8})
table.add_rows({'a': 4, 'b': 16})
print(table.get_column('a'))
print(table.get_column('b'))