#Escribir un programa que le pida al usuario introducir la cantidad de filas y columnas de una
# lista de 2 dimensiones, y a continuación le pida los datos para cada posición de la lista.

cantidad_fila = int(input('Escriba la cantidad de filas a introducir: '))
cantidad_columna = int(input('Escriba la cantidad de columnas a introducir: '))

matrizBidimencional = []

#lista = [[56,62],[56,23],[54,12]]

for i in range (1, cantidad_fila+1):
    o = []
    for j in range (1, cantidad_columna+1):
        print('introduzca el dato de la fila ',i, 'y la columna ',j , end=': ')
        o.append(int(input()))
    matrizBidimencional.append(o)

for l in range(cantidad_fila):
    for k in range(cantidad_columna):
        print(matrizBidimencional[l][k], end = " ")
    print(' ')

