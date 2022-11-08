# Имитация вызова функции

#def foo(*args, **kwargs):
#    print(args, kwargs)


class Foo:
    def __call__(self, *args: tuple, **kwargs: dict) -> any:
        print(args, kwargs)

foo = Foo()

foo(1, 2, 3, a = 4, b = 5)