# Урок от 11.10.2022


integer = 1
float = 1.1
true, false = True, False
none = None

my_list = [integer, float, true, false, none]
my_tuple = (integer, float, true, false, none)

new_lst = [integer, my_tuple, my_list]

my_dict = {
    'Integer': integer,
    'tuple': my_tuple,
    'list': my_list
    }

my_set = set()

result = f'Это список - {my_list},\nЭто кортеж - {my_tuple},\nЭто словаь - {my_dict}'
#print(result)

from pprint import pprint

word = 'Hellow'
chars = list(word)

rainbow = ['red', 'green', 'blue']
rainbow.append('violet') # При добавлении в список переменную создавать не нужно
                                    # Списоки и словари - изменяемые объекты
rainbow.extend(['violet', 'yellow'])
#print(rainbow)

#primes.insert(0, 1) # insert(индекс, значение)

gradient = [ [4,5], [7,9]]
#print(gradient[1][0])

primes = [2, 3, 5, 7, 11, 13]
inversion = primes.copy() # Создаёт копию списка
inversion.reverse() # Разворачивает список
#print(primes,'\n',inversion)

# Показывает индекс значения (если есть в списке) .index(значение, *start, *stop)
# print(primes.index(2))

# Минимальное значнеие в списке
# print(min(primes))

# Словарь - список, где у каждого объекта есть ключ
capitals = {}
capitals['Россия'] = 'Москва'
capitals['Франция'] = 'Париж'
capitals['Италия'] = 'Рим'
# pprint(capitals)

# Словарь - изменяемый объект
cities = capitals
cities['Бразилия'] = 'Бразилиа' # Оба словаря изменились
# print(cities,'\n', capitals)

# Кортеж - неизменяемый объект
my_tuple = (20, 30, 40)
new_tuple = my_tuple
new_tuple += (50, 60) # Только новый кортеж изменился
# print(my_tuple, '\n', new_tuple)

# Замена значения в списке
lst = [1, 2, 3]
lst[0] = 4
# print(lst)