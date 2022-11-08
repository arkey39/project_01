# Класс строки

class Row:

    def __init__(self, *args):
        self._args = args
    
    def __eq__(self, other: object) -> bool: # Задаёт правило обработки равенства объектов
        return self._args == other._args

    def __hash__(self) -> int: # Создаёт уникальный хеш
        return hash(self._args)

    def __add__(self, other):
        return self._args + other._args if isinstance(other, Row) else self._args + other

r1 = Row(1, 2, 3)
r2 = Row(4, 5, 6)

print(r1 == r2)
print(r1 + r2)
print(r1 + (1, 2, 3))