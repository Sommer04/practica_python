
# Escribir un programa que lea un número por teclado y determine si se trata de un número primo.

num_primo = int(input("Inserte el Numero que sea primo: "))
a = 1
b = 0
while a <= num_primo:
    if num_primo % a == 0:
        b += 1
    a += 1

if b == 2:
    print("El numero", num_primo, "Es numero primo")

elif b > 2:
    print(num_primo, "No es un numero primo")
else:
    print("Valores Incorrectos")

