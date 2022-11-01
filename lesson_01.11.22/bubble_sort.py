# Сортировка пузырьком - это метод сортировки массивов и списков путем последовательного сравнения и обмена
# соседних элементов, если предшествующий оказывается больше последующего.

from random import randint

n = 15
arr = []
for i in range(n):
    arr.append(randint(10, 150))
print(arr)

for k in range(n-1):
    for j in range(n-k-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# Или с помощью while

k = 0
while k < n - 1:
    j = 0
    while j < n - 1 - k:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        j += 1
    k += 1
print(arr)