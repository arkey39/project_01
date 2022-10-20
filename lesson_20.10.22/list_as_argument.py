

# 1й аргумент - список цифр, 2й - index в списке
def pick(l: list, index: int) -> int: # возвращает число в указаном индексе
    if isinstance(l, list):
        return l[index]

print(pick([1,2,3,], 1))