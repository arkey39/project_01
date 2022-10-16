hotel_names = list()
hotel_names.append('aloHotel')
hotel_names.append('Appart lounge')
hotel_names.append('Sleepower')
hotel_names.append('Penthouseus')
hotel_names.append('Hotel star')

print(hotel_names)

i = -1
while i < len(hotel_names) - 1:
    i += 1
    if i == 2:
        continue

    name = hotel_names[i]
    print('Проверяем', name)

    if name == 'Penthouseus':
        print('Отель найден!')
        break

print('До свидания')