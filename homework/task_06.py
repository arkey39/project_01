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

print('Три случайные песни:', r.choices(list(my_favorite_songs.keys()), k = 3))
print('Три уникальные песни:', r.sample(list(my_favorite_songs.keys()), k = 3))
print('Три случайные песни звучат {:.2f} минут'.format(sum(r.choices(list(my_favorite_songs.values()), k =3))))
print('Три уникальные песни звучат {:.2f} минут'.format(sum(r.sample(list(my_favorite_songs.values()), k =3))))