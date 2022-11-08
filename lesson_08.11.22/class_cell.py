# Для класса выделяют:
#   методы - функции внутри класса
#   атрибуты - переменные внутри класса

class Cell:
    '''Ячейка'''
    content = 1
    content_type = int()

    def set_value(self, val):
        self.content = val
        self.content_type = type(val)

# Создаем экземпляр-объекта класса
a1 = Cell()
b1 = Cell()

a1.set_value('Hello')
print(a1.content_type)
print(a1.content)

#print(
#    'Имена класса Cell:', Cell().__dict__,
#    'Имена ячейка a1:', a1.__dict__,
#    'Имена ячейка b1:', b1.__dict__,
#    sep='\n'
#    )

#a1.content=100

#print(
#    'Имена класса Cell:', Cell().__dict__,
#    'Имена ячейка a1:', a1.__dict__,
#    'Имена ячейка b1:', b1.__dict__,
#    sep='\n'
#    )