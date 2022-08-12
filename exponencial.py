from cProfile import label
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import path_01

def menu_functions_two():
    ops = ('[1] - Verificar se é crescente ou decrescente',
    '[2] - Calcular Função em "X" pedido',
    '[3] - Gerar Gráfico de Função',
    '[4] - Sair do Submenu')
    while True:
        print('-=-' * 10)
        print('FUNÇÕES EXPONENCIAIS'.center(30))
        print('-=-' * 10)
        for op in ops:
            print(op)
        print('-=-' * 10)
        try:
            ask = int(input('Digite uma Opção Válida: '))
        except ValueError:
            print('\033[31mERRO!\033[m')
            sleep(1)
        else:
            if ask not in [1, 2, 3, 4]:
                print('\033[31mOpção Inválida\033[m')
                sleep(1)
            else:
                if ask == 1:
                    option_one()
                elif ask == 2:
                    option_two()
                elif ask == 3:
                    option_three()
                elif ask == 4:
                    print('-=-' * 10)
                    sleep(1)
                    path_01.show_op()

def option_one():
    while True:
        try:
            a = float(input('Digite o Coeficiente "A": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    while True:
        try:
            b = float(input('Digite o Coeficiente "B": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            if b < 0 or b == 1:
                print('\033[31mO Valor de "B" deve ser maior que "0" e diferente de "1"\033[m')
            else:
                break
    if b > 1:
        print('A função é Crescente')
        sleep(1)
    if 0 < b < 1:
        print('A função e Decrescente')
        sleep(1)


def option_two():
    while True:
        try:
            a = float(input('Digite o Coeficiente "A": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    while True:
        try:
            b = float(input('Digite o Coeficiente "B": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            if b < 0 or b == 1:
                print('\033[31mO Valor de "B" deve ser maior que "0" e diferente de "1"\033[m')
            else:
                break
    while True:
        try:
            x = float(input('Digite o Valor de "X": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    print(f'f({x}) = {a * (b ** x)}')
    sleep(1)


def option_three():
    while True:
        try:
            a = float(input('Digite o Coeficiente "A": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    while True:
        try:
            b = float(input('Digite o Coeficiente "B": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            if b < 0 or b == 1:
                print('\033[31mO Valor de "B" deve ser maior que "0" e diferente de "1"\033[m')
            else:
                break
    x = np.linspace(-2, 2, 100)
    y = a * (b ** x)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, y, 'y', label='a * b ** x')
    plt.legend(loc='upper left')
    plt.show()
    sleep(1)

