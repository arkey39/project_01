print("Ноль закроет калькулятор")
while True:
    s = input("Знаки (+, -, *, /): ")
    if s == '0':
        break
    elif s in ('+', '-', '*', '/'):
        a = float(input("a="))
        b = float(input("b="))
        if s == '+':
            print("%.2f" % (a+b))
        elif s == '-':
            print("%.2f" % (a-b))
        elif s == '*':
            print("%.2f" % (a*b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a/b))
            else:
                print('Деление на ноль!')
    else:
        print('Неверный знак операции!')