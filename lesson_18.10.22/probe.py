# Урок от 18.10.2022

# Функции

#def greeting():
#    print('Привет, мир!')

# 10 раз выполнить "Привет, мир!"
#for _ in range(10):
#    greeting()

# Функция суммирования, пока i не дойдёт до 10
#i = 0
#while i < 10:
#    i += 1
#    pass

# DRY – Dont repeat yourself
#def greeting(parameter1):
#    print('Привет,', parameter1)
#hello_lst = ['Мир', 'Земля', 'Космос']
#for elem in hello_lst:
#    greeting(elem)



def make_coffee(size, sugar_dose = 2): # "= 2" - базовое количество переменной. Функция будет работать, даже если не указать переменную.
    if sugar_dose > 5:
        return 'Слишком много сахара!'
    else:
        return f'Ваш кофе объёмом {size} мл с {sugar_dose} кусочками сахара готов!'
# Результат функции нужно сохранят в переменную (при наличии return в функции)
text = make_coffee(300)
print(text)