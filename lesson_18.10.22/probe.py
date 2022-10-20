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
def greeting(parameter1):
    print('Привет,', parameter1)
hello_lst = ['Мир', 'Земля', 'Космос']
for elem in hello_lst:
    greeting(elem)