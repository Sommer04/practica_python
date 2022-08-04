# Escribir un programa que pida al usuario un número,
# si el número esta comprendido entre 1 y 10 que
# muestre un mensaje diciendo gracias. de lo contrario que se mantenga
# de manera indefinida pidiendo el número hasta que el usuario ingrese un número entre 1 y 10.
##

i = 0
while i < 1 or i > 10:
    i = int(input('ingrese el  numero dentro del rango 1 y 10 '))
    if i >= 1 and i <= 10:
        print('Gracias')
        break




