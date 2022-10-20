## Модули

# Модуль - файл, определения и выражения которого можно использовать 
# в других файлах

# my_module - наш модуль
import my_module    # - самый простой способ получить доступ к модулю

# import my_module as md - сокращение названия
# import folder_name.my_module - если модуль находится в папке
# from my_module import foo - импортирование функции из модуля
# from my_module import foo as f - сокращение названия функции

print(my_module.var_1)  # ссылка на переменную var_1
my_module.foo()         # ссылка на функцию foo()

# print('Название модуля', __name__)