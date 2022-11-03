salary = float(input('Введи ЗП '))
exp = float(input('Введи расход '))
month = [1,2,3,4,5,6,7,8,9,10,11,12]
all_salary = salary
if exp >= salary:
    print('Условия не верны')
else:
    for i in month:
        if i != 1:
            exp_total = exp * i
            salary = salary * 1.05
            all_salary = all_salary + salary
    live = abs(all_salary - exp_total)
print('Сотрудник накопит ', round(live, 2))