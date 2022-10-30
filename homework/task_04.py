# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

import random as r

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

len = len(my_favorite_songs)
random1 = r.randrange(0, len)
random2 = r.randrange(0, len)
random3 = r.randrange(0, len)
duration_of_three = my_favorite_songs[random1][1] + my_favorite_songs[random2][1] + my_favorite_songs[random3][1]

print('Три песни звучат {:.2f} минут'.format(duration_of_three))

# Отлично можно ещё так
# Решение 2
time = 0
for song in sample(my_favorite_songs, 3):
    print(song[0])
    time += song[1]

print(f'Три песни звучат {round(time, 2)}')
