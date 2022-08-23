#Escribir un programa que le pida al usuario llenar dos listas de dos dimensiones (3 filas y 4 columnas)
# y sume ambas listas almacenando el resultado en una tercera lista. Utilizar una función para imprimir las matrices durante el proceso

import numpy

fila = 3
columna = 4
matriz_1 = numpy.array([],dtype= int)
matriz_2 = numpy.array([],dtype= int)

for i in range(1, fila + 1):
    for j in range(1, columna + 1):
        print('introduzca el dato de la fila ', i, 'y la columna de la primera matriz', j, end=': ')
        valor_1 = int(input())
        matriz_1 = numpy.append(matriz_1,[valor_1])



for k in range(1, fila + 1):
    for l in range(1, columna + 1):
        print('introduzca el dato de la fila ', k, 'y la columna de la segunda matriz', l, end=': ')
        valor_2 = int(input())
        matriz_2 = numpy.append(matriz_2,[valor_2])

matriz_3 = matriz_1.reshape(fila,columna)
matriz_4 = matriz_2.reshape(fila,columna)

resultado_matriz = numpy.add(matriz_3,matriz_4)
print('')


def suma_matriz (matriz):
    print(matriz)

suma_matriz(matriz_3)
suma_matriz(matriz_4)
suma_matriz(resultado_matriz)