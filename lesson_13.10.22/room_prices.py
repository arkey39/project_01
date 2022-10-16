room_prices = (41, 90, 100, 9, 61, 38, 15, 8, 68)

i = -1
while i < len(room_prices) - 1:
    i += 1
    price = room_prices[i]
    print('Проверяем ', price)

    if price == min(room_prices):
        print('Найдена минимальная цена')
        break
print('До свидания!')