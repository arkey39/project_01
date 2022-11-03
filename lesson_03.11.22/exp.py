salary = float(input('Введи ЗП'))
exp = float(input('Введи расход'))
month = [1,2,3,4,5,6,7,8,9,10,11,12]
exp_total = exp
if salary >= exp:
    print('Условия не верны')
else:
    for i in month:
        if i != 1:
            all_sallary = salary * i
            exp = exp * 1.03
            exp_total = exp_total + exp
    live = abs(all_sallary - exp_total)
print('Необходимо занять ', round(live, 2))