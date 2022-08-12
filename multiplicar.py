import numpy

def mult(m_final, matriz ,linhas, colunas, elementos):
    linhas_2 = int(input("Digite o numero de linhas"))
    colunas_2 = int(input("Digite o numero de colunas"))

    if linhas == colunas_2 or colunas == linhas_2:
        print("é Possivel calcular")
    else:
        print("Não é possivel multiplicar")
        return None
    
    matriz_2 = []
    m_final_2 = []
    matriz_reserva_2 = []

    for i in range(elementos):
        valor = int(input(f"valor {i}: "))
        matriz_2.append(valor)
        
    for i in range(elementos):
        matriz_reserva_2.append(matriz_2[i])
        if len(matriz_reserva_2) == colunas:
            m_final_2.append(matriz_reserva_2)
            matriz_reserva_2 = []
    j = 0

    j = 0
    for i in matriz:
        if j == 0:
            print("| ", end='')    
        print(i, end=' ')
        j += 1
        if j == colunas:
            print("| \r")
            j = 0

    print("x")

    for i in matriz_2:
        if j == 0:
            print("| ", end='')    
        print(i, end=' ')
        j += 1
        if j == colunas:
            print("| \r")
            j = 0
    
    print("-" * colunas)
    
    result = numpy.dot(m_final, m_final_2)
    print(result)