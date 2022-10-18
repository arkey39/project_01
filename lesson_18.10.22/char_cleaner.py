
def char_cleaner(string):
    '''Функция char_cleaner() принимает string
    возвращает объект str без символов'''
    new_s = ''

    for i in s:
        if i.isdigit():
            new_s += i
    
    return new_s

s = 'Дата заказа: 2022-08-12_xdasa'

print(char_cleaner(s))
print(help(char_cleaner))