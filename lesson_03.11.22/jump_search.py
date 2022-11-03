# Jump Search похож на бинарный поиск тем, что он также работает с отсортированным массивом и
# использует аналогичный подход «разделяй и властвуй» для поиска по нему.
# Его можно классифицировать как усовершенствованный алгоритм линейного поиска, поскольку он
# зависит от линейного поиска для выполнения фактического сравнения при поиске значения.

import math as m
from random import randint

def JumpSearch (arr, value):
    length = len(arr)
    jump = int(m.sqrt(length))
    left = 0
    right = 0
    while left < length and arr[left] <= value:
        right = min(length - 1, left + jump)
        if arr[left] <= value and arr[right] >= value:
            break
        left += jump
    if left >= length or arr[left] > value:
        return -1
    right = min(length - 1, right)
    i = left
    while i < right and arr[i] <= value:
        if arr[i] == value:
            return i
        i += 1
    return -1

test_arr = []
for i in range(15):
    test_arr.append(randint(50, 150))
    test_arr.sort()
print(test_arr)

x = int(input('Введите число '))

if JumpSearch(test_arr, x) != -1:
    print('Элемент под индексом', JumpSearch(test_arr, x))
else:
    print('Элемент отсутствует в массиве')