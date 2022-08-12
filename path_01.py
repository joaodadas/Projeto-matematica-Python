RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\u001b[34;1m"
YELLOW = "\033[1;33m"
NORMAL = "\u001b[0m"


from time import sleep
import high_school_functions
import exponencial
import matriz


def little_color(texto, color=NORMAL):
    print(color + texto + NORMAL)


# menu
def beginning():
    little_color('===================', GREEN)
    little_color('GRUPO: os caras das bolsinhas', RED)
    little_color('Alunos: ', GREEN)
    print('   RAVI MUGHAL,\n   GUILHERME VILELA,\n   jOÃO VITOR DADAS')
    little_color('CALCULADORA RMC', YELLOW)
    little_color('===================', GREEN)


def options(num, string):
    print(BLUE + '[' + str(num) + '] ' + NORMAL + string)


def show_op():
    little_color('\n======= MENU =======', GREEN)
    options(1, 'HIGH SCHOOL FUNCTIONS')
    options(2, 'EXPONENTIAL FUNCTIONS')
    options(3, 'MATRICES')
    options(4, 'CLOSE PROGRAM')
    while True:
        try:
            op = int(input(RED + '==>'))
        except ValueError:
            print(RED + 'ERROR!')
        else:
            if op not in [1, 2, 3, 4]:
                print(RED + 'Please, enter valid action!!' + NORMAL)
                sleep(1)
            else:
                if op == 1:
                    high_school_functions.opp()
                elif op == 2:
                    exponencial.menu_functions_two()
                elif op == 3:
                    matriz.rodar()
                elif op == 4:
                    break

if __name__ == '__main__':

    beginning()
    show_op()





