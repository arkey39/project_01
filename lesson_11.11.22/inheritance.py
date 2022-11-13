# ООП

class User:
    '''Модель пользователя'''

    uid = 1000
    active = True
    # __token = 'очень-очень секретный ключ' # токен

    def __init__(self, name = None):
        self.name = name

    def __str__(self):
        return '{}, id({}), status({})'.format(
            self.__class__.__name__,
            self.uid,
            'Active' if self.active is True else 'Dead'
            )

class Guest(User):
    '''Гость'''

    def check_prmisions(self):
        print('Чтение')

class Admin(User):
    '''Администратор'''

    def check_prmisions(self):
        print('Чтение', 'Исполнение')

class Root(User):
    '''Суперпользователь'''
    
    uid = 0
    __token = 'очень-очень секретный ключ' # токен
    def get_token(self):
        print(self.__token)

acc1 = Guest(name = 'Радж')
acc2 = Admin(name = 'Сэм')

print(acc1)
print(acc2)

acc1.check_prmisions()
acc2.check_prmisions()

acc0 = Root()