# Бинарный поиск работает по принципу «разделяй и властвуй». Он быстрее, чем линейный поиск, но требует,
# чтобы массив был отсортирован перед выполнением алгоритма.

def binary_search(arr, low, high, x):
    # Проверка середины
    if high >= low:
        mid = (high + low) // 2
        # Если элемент находится в середине
        if arr [mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

arr = [3, 5, 7, 10, 15, 17]
x = input('Введи число:')
x = int(x)

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Элемент присутствует в массиве")
else:
    print("Элемент не присутствует в массиве")