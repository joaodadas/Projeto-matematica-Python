from time import sleep
from cmath import sqrt
import path_01
import numpy as np
import matplotlib.pyplot



RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\u001b[34;1m"
YELLOW = "\033[1;33m"
NORMAL = "\u001b[0m"



def options(num, string):
    print(BLUE + '[' + str(num) + '] ' + NORMAL + string)


def little_color(texto, color=NORMAL):
    print(color + texto + NORMAL)


def delt(a, b, c):
    return (b ** 2) - (4 * a * c)


def complex(a, b, delta):
    x1 = ((-b) + (sqrt(delta))) - (2 * a)
    x2 = ((-b) - (sqrt(delta))) - (2 * a)
    print(f'the delta value is {delta}, a complex number')
    print(f'the x1 and x2 values are {x1} and {x2}')


def roots(a, b, delta):
    x1 = ((-b) + (delta ** (1 / 2))) / (2 * a)
    x2 = ((-b) - (delta ** (1 / 2))) / (2 * a)
    if x1 == x2:
        print(f'the delta value is {delta}, x1 = x2')
        print(f'the x1 and x2 values are {x1} and {x2}')
    else:
        print(f'the delta value is {delta}, x1 != x2')
        print(f'the x1 and x2 values are {x1} and {x2}')


def opp():
    little_color('\n======= MENU =======', GREEN)
    options(1, 'calculate roots')
    options(2, 'calculate function in X')
    options(3, 'calculate vertex')
    options(4, 'generate chart')
    options(5, 'back to start')
    while True:

        try:
            ask = int(input(BLUE + '\ntype an option: ' + GREEN))
        except ValueError:
            print(RED + 'ERROR!!')
            sleep(1)
        else:
            if ask not in [1, 2, 3, 4, 5, ]:
                print(RED + 'invalid operation')
                sleep(1)

            else:
                if ask == 1:
                    func_roots()
                    sleep(1)
                elif ask == 2:
                    FX()
                    sleep(1)
                elif ask == 3:
                    vertex()
                    sleep(1)
                elif ask == 4:
                    chart()
                    sleep(1)
                elif ask == 5:
                    path_01.show_op()


def func_roots():
    while True:
        try:
            a = float(input('enter the coefficient "A": '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    if a > 0:
        while True:
            try:
                b = float(input('enter the coefficient "B": '))
            except ValueError:
                print(RED + 'TRY AGAIN!!')
            else:
                break
        while True:
            try:
                c = float(input('enter the coefficient "C": '))
            except ValueError:
                print(RED + 'TRY AGAIN!!')
            else:
                break
        delta = delt(a, b, c)
        if delta < 0:  # complex
            complex(a, b, delta)
            sleep(1)
            return opp()
        else:
            roots(a, b, delta)
            sleep(1)
            return opp()
    else:
        print('valor de a dever ser maior q 0')


def FX():
    while True:
        try:
            a = float(input('enter the coefficient "A": '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    while True:
        try:
            b = float(input('type the coefficient "B": '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    while True:
        try:
            c = float(input('type the coefficient "C": '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    while True:
        try:
            x = float(input('type the coefficient "X": '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    print(f'f({x}) = {(a * (x ** 2)) + (b * x) + c}')
    sleep(1)
    return opp()


def vertex():
    while True:
        try:
            a = float(input('type the coefficient A: '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    while True:
        try:
            b = float(input('type the coefficient B: '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    while True:
        try:
            c = float(input('type the coefficient C: '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    print(f'XVertex has the value of : {-b / (2 * a)}')
    print(f'YVertex has the value of : {-delt(a, b, c) / (4 * a)}')


def chart():
    while True:
        try:
            a = float(input('type the coefficient A: '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    while True:
        try:
            b = float(input('type the coefficient B: '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    while True:
        try:
            c = float(input('type the coefficient C: '))
        except ValueError:
            print(RED + 'TRY AGAIN!!')
        else:
            break
    x = np.arange(-1000, 1001, 1)
    y = (a * (x * x)) + (b * x) + c
    matplotlib.pyplot.plot(x, y, 'y', label='ax ** 2 + bx c')
    matplotlib.pyplot.legend(loc='upper left')
    matplotlib.pyplot.show()


