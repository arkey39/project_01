# Поиск самых высокооплачиваемых работников с помощью спискового включения

# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}

# Вариант 1
#top_mgrs = []
#for name, salary in employees.items():
#    if salary >= 100000:
#        top_mgrs.append(name)

#print(top_mgrs)

# Вариант 2
top_mgrs = [name for name, salary in employees.items() if salary >= 100000]
print(top_mgrs)