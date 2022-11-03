# Интерполяционный поиск - это еще один алгоритм «разделяй и властвуй», похожий на бинарный поиск.
# В отличие от бинарного поиска, он не всегда начинает поиск с середины. Интерполяционный поиск вычисляет
# вероятный индекс искомого элемента по формуле:
# index = low + [(value - arr[low])*(high-low) / arr[high] - arr[low])]

import math as m
from random import randint

def InterpolationSearch(arr, value):
    low = 0
    high = (len(arr) - 1)
    while low <= high and value >= arr[low] and value <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (value - arr[low])))
        if arr[index] == value:
            return index
        if arr[index] < value:
            low = index + 1
        else:
            high = index - 1
    return - 1

test_arr = []
for i in range(15):
    test_arr.append(randint(50, 150))
    test_arr.sort()
print(test_arr)

x = int(input('Введите число '))

if InterpolationSearch(test_arr, x) != -1:
    print('Элемент под индексом', InterpolationSearch(test_arr, x))
else:
    print('Элемент отсутствует в массиве')