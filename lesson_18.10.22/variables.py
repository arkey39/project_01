# Переменная глобального пространства имён
name = 'Никита'

def greeting():
    question = 'Как дела?' # ЯПеременная локального пространства имён
    print('Привет, ', name)
    print(question)

# Локальные переменные приоритетней глобальных

def add_value(param):
    [].append(param)

greeting()