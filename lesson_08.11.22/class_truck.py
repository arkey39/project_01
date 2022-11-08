# Самосвал

class Truck:
    '''Самосвал загружает в ковш и выгружает из него в другом месте'''

    def __init__(self, *args: tuple) -> None:
        self._args = args
        print('Загружено в ковш:')
        [print(i) for i in self._args]

    def __len__(self): # Количество объектов в экземпляре
        return len(self._args)

    def __eq__(self, other: object) -> bool: # Задаёт правило обработки равенства объектов
        return isinstance(other, type(self)) and self._args == other._args

    def __hash__(self) -> int: # Создаёт уникальный хеш
        return hash(self._args)

    def __del__(self):
        print('Содержимое выгружено из ковша!')
        
transport1 = Truck('песок', 'щебень', 'земля', 'блоки')
transport2 = Truck('песок', 'щебень', 'земля', 'блоки')

hash_d = {transport1: 1, transport2: 2}
print(hash_d)
#print('Количество объектов:', len(transort))