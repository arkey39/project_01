def add_value(element, list_to_add=[]):
    list_to_add.append(element)
    return list_to_add

lst = [1,2,3]
lst_1 = add_value(4, lst)
print(lst_1)

lst_2 = add_value(4)
print(lst_2)

lst_3 = add_value(10000)
print(lst_3)  # Ожидаю [10000], но получаем [4, 10000]