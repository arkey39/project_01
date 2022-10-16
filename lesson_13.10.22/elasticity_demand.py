elasticity_dem = 1

if elasticity_dem == 0:
    print('Товары первой необходимости')
    result = 0.0

elif 0 < elasticity_dem < 1:
    print('Нормальные блага')
    result = 0.5

elif elasticity_dem > 1:
    print('Роскошь')
    result = 3.0

else:
    if elasticity_dem == 1:
        print ('Единичная эластичность')
        result = 1.0

    print ('Товары низкого качества')
    result = -1.0

        
print('значение =',result)