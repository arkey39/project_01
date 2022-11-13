# ООП

class User:
    '''Модель пользователя'''

    uid = 1000
    active = True
    # __token = 'очень-очень секретный ключ' # токен

    def __init__(self, name = None):
        self.name = name
        self.uid = 1000
        self.get_permisions('700')

    def __str__(self):
        return '{}, id({}), status({})'.format(
            self.__class__.__name__,
            self.uid,
            'Active' if self.active is True else 'Dead'
            )

    def get_permisions(self, args):
        self.u, self.g, self.o = args
        return self.u, self.g, self.o
    
    def check_permisions(self):
        print('Права:', self.u, self.g, self.o)

class RemoteDesktop:
    '''Удалённый рабочий стол'''

    def __str__(self):
        return f'Пользователь {self.__class__.__name__} подключен к удалённому рабочему столу'

    def connection(self, host):
        print(f'Подключение к {host}')

class Guest(User, RemoteDesktop):
    '''Гость удалённого рабочего стола'''

    def __str__(self):
        return '{}, id({}), status({})\n{}'.format(
            self.__class__.__name__,
            self.uid,
            'Active' if self.active is True else 'Dead',
            f'Пользователь {self.__class__.__name__} подключен к удалённому рабочему столу'
            )

class Admin(User):
    '''Администратор'''

    def __init__(self, name):
        super().__init__(name = name)
        self.get_permisions('764')

class Root(User):
    '''Суперпользователь'''

    active = False

acc1 = Guest(name = 'Радж')
print(acc1)
acc1.check_permisions()
acc1.connection(host = '127.0.0.1')
print()

acc2 = Admin(name = 'Сэм')
print(acc2)
acc2.check_permisions()
print()

acc0 = Root()
print(acc0)