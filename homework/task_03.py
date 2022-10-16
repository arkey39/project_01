# Задача 3
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

months = {1 : 31,
          2 : 28,
          3 : 31,
          4 : 30,
          5 : 31,
          6 : 30,
          7 : 31,
          8 : 31,
          9 : 30,
          10 : 31,
          11 : 30,
          12 : 31}

user_input = input("Введите номер месяца: ")
month = int(user_input)
if month in months:
    print('Количество дней в месяце -', months[month])
else:
    print('Ошибка в вводе')