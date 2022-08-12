import determinante as dtt
import multiplicar as mlt
import transposta as trp
import path_01 as pt


def rodar():
    def nQuad(l,c):
        if l != c:
            print("matriz não quadrada")


    linhas = int(input("Numero de linhas: "))
    colunas = int(input("Numero de colunas: "))
    matriz = []
    matriz_reserva = []
    m_final = []


    elementos = linhas * colunas

    for i in range(elementos):
        valor = int(input(f"valor {i}: "))
        matriz.append(valor)
            


    j = 0
    for i in matriz:
        if j == 0:
            print("| ", end='')    
        print(i, end=' ')
        j += 1
        if j == colunas:
            print("| \r")
            j = 0

    for i in range(elementos):
        matriz_reserva.append(matriz[i])
        if len(matriz_reserva) == colunas:
            m_final.append(matriz_reserva)
            matriz_reserva = []

    while True:
        print("1. Determinante")
        print("2. Multiplicar")
        print("3. Transposta")
        print("4. Sair")


        select = input("Digite a opção: ")
        try:
            select = int(select)

            if select == 1:
                nQuad(linhas,colunas)
                dtt.dett(m_final)
            if select == 2:
                mlt.mult(m_final, matriz ,linhas, colunas, elementos)
            if select == 3:
                trp.transposta(m_final)
            if select == 4:
                pt.show_op()

        except:
            if type(select) == str:
                print("Digite um inteiro \r")
