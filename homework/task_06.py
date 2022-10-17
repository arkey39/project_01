# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

import random as r

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

len = len(my_favorite_songs)
random1 = r.choice(list(my_favorite_songs.keys()))
random2 = r.choice(list(my_favorite_songs.keys()))
random3 = r.choice(list(my_favorite_songs.keys()))
duration_of_three = my_favorite_songs[random1] + my_favorite_songs[random2] + my_favorite_songs[random3]

print('Три песни звучат {:.2f} минут'.format(duration_of_three))