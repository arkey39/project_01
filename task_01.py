# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

#len = len(my_favorite_songs)
#print(len)

index = my_favorite_songs[:14] + ', ' + my_favorite_songs[64:] + ', ' + my_favorite_songs[16:30] + ', ' + my_favorite_songs[51:62]
print(index)
