# Урок от 13.10.22  if и else

# Отладка (Debuging)
# x = 4
#print('Здравствуйте')
#if x < 0:
#    print('Меньше нуля')
#print('До свидания')

# Сравнение списков
#if 'abc' < ('abcd'):
#    print('Успех')

#x = 4
#if x < 0:
#    print('Меньше нуля')
#else:
#    print('Больше нуля')

#x, y = 3, 4
#rez = x + y if y < x else y - x
#print(rez)

# Тройное сравнение
#x, y = True, False
#if y and not x or x:
#    print('Истина')
#else:
#    print('Ложь')

#x = 4
#if x < 0:
#    print('Меньше нуля')
#elif x == 0:
#    print('Равен нулю')
#elif x == 1:
#    print('Равен единице')
#else:
#    print('Больше нуля, но не равен единице')

# Операторы циклов while (пока что то не произойдёт) и for ()

#i = 1
#while i < 10:
#    i += 1
#    print('i =', i)

# Последовательность Фибоначи
# №   1   2   3   4   5   6   7   8   9   10 ... 14
# ЧФ  1   1   2   3   5   8   13  21  34  55      ?

#fib1, fib2 = 1, 1
#i = input("Номер элемента ряда Фибоначчи: ")
#i = int(i) - 2
#while i > 0:
#    print(fib2)
#    fib1, fib2 = fib2, fib1 + fib2
#    i -= 1
#print("Значение этого элемента:", fib2)