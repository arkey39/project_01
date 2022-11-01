import random as r

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
user_input = input('Задайте длину пароля:' + "\n")
length = int(user_input)

try:
    print('Пароль:', ''.join(r.choices(chars, k = length)))
except ValueError:
    print('Вы ввели буквы, пожалуйста введите цифры')
