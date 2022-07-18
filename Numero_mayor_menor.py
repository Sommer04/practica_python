# Escribir un programa que pida al usuario 3 números por teclado,
# y diga cual es el mayor y el menor de los3 números.

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))


if numero_1 > numero_2  and numero_1 > numero_3:
    print("el numero mayor es", numero_1)
    if numero_2 > numero_3 :
        print("el numero menor es ", numero_3)
    else:
        print("el numero menor es ", numero_2)
elif numero_2 > numero_1  and numero_2 > numero_3:
    print("el numero mayor es", numero_2)
    if numero_1 > numero_3 :
        print("el numero menor es ", numero_3)
    else:
        print("el numero menor es ", numero_1)

elif numero_3 > numero_1  and numero_3 > numero_2:
    print("el numero mayor es", numero_3)
    if numero_1 > numero_2 :
        print("el numero menor es ", numero_2)
    else:
        print("el numero menor es ", numero_1)
else:
    print("existen numeros iguales")

