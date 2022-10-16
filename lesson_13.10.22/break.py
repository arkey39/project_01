while True:
    user_input = input('Введите “Перерыв” >> ')
    result = str(user_input)
    if result == "Перерыв":
        print('Урааа!')
        break
    else:
        print('А когда перерыв?( Попробуйте еще раз...')