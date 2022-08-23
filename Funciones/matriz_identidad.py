#Escribir un programa que le pida al usuario introducir la cantidad de filas y columnas de una lista de 2 dimensiones
# y genere la matríz identidad. (Validar que la cantidad de filas y columnas deben ser iguales).

import numpy

print('\n Creacion de Matriz Identidad \n')

while True:
    cantidad_fila = int(input('Escriba la cantidad de filas a introducir: '))
    cantidad_columna = int(input('Escriba la cantidad de columnas a introducir: '))
    print('')
    if cantidad_fila != cantidad_columna:
        print('la fila y la columna deben ser de igual cantidad \n')
        cantidad_fila = 0
        cantidad_columna = 0
    else:
        break

matrizBidimencional = []
matrizIdentidad = []

#lista = [[56,62],[56,23],[54,12]]

def Bidimensional (cantidad_fila, cantidad_columna,):
    for i in range (1, cantidad_fila+1):
        o = []
        for j in range (1, cantidad_columna+1):
          #  print('introduzca el dato de la fila ',i, 'y la columna ',j , end=': ')
            o.append(0)
        matrizBidimencional.append(o)
   # print('\n')
    for l in range(cantidad_fila):
        for k in range(cantidad_columna):
            print(matrizBidimencional[l][k], end = " ")
        print(' ')
    print('\n la matriz identidad es:\n' )

    n = 0
    for a in range (len(matrizBidimencional)):
        matrizBidimencional[n][n]=1 #solamente sera uno cuando la fila sea igual que la columna ejemplo: fila 1 * columna 1 pero no fila 1 * columna 2
        print(matrizBidimencional[n])
        n+=1


Bidimensional(cantidad_fila,cantidad_columna)