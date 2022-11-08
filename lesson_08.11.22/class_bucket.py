# Здесь создадим класс хранилища

class Bucket:
    '''Хранилище объектов для статического скайта'''
    
    def __init__(self):
        self.content = []

    def get_var_name(self):
        for key, val in globals().items():
            if val is self:
                return key

    def __str__(self): # Преобразование в строку
        return f'Содержимое: {self.get_var_name()}' + ', '.join(self.content)

    def __bool__(self): # Вызывается для получения "истинности" объекта с помощью функции bool()
        return self.content != []

    def add(self, obj):
        '''Поместить объект в бакет'''
        self.content.append(obj)
        print('Добавлен', obj)

    def inspect(self):
        '''Проверить содержимое'''
        print('Текущее содержимое бакета:')
        for item in self.content:
            print('    ', item)

website = Bucket()

print(bool(website))
website.add(obj='index.html')  # вызов метода
website.add('main.css')
#website.inspect()

print(website)
print(bool(website))
#Bucket.add(self = website, obj = 'index.html')  # на самом деле происходит вот это
#print(website.content)