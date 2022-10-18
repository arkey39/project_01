# import random as r
from random import randint, choice, choices

def print_them_all(a, b=None,*args, **kwargs):
    print('print_them_all')
    print('a и b:', a, b)
    print('тип args:', type(args))
    print(args)
    
    for i, elem in enumerate(args):
        print('Позиционный параметр:', i, elem)

    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('Именованный параметр:', key, value)



# Вывод трех случайных значений от 100 до 10000
print([choice(range(100, 10000)) for _ in range(3)])  

r_lst = choices(range(100, 10000), k = 5)
print_them_all(
    10,
    1000,
    randint(100, 1000), 
    randint(100, 1000), 
    randint(100, 1000),
    x = randint(100, 1000),
    y = randint(100, 1000)
    )