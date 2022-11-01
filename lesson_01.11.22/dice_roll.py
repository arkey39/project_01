import random as r

n = 0
dice_rolls = []
while n < 4:
    d = r.randint(1, 6)
    dice_rolls.append(d)
    n += 1
print('После четырёх бросков выпало:', dice_rolls)
print('Сумма', sum(dice_rolls))