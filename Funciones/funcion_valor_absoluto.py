#Escribir un programa que defina una función que reciba como parámetro un
# numero entero y devuelva el valor absoluto de ese número.



def valorabsoluto (numero):
    if numero < 0:
        numero *= -1
    else:
        numero
    return numero

numero = int(input('Escriba el numero a convertir: '))
resultado = valorabsoluto(numero)
print('el valor absoluto es: ',resultado)