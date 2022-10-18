


def search_min_price(arr):
    for price in room_prices:
        if price == max(arr):
            continue
        if price == min(arr):
            return f'Минимальная цена: {price}'
        yield f'Текущая цена {price}'
    else:
        return f'Такой цены нет!'

room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17]

print(search_min_price(room_prices))