#Escribir un programa que lea un número por teclado y muestre en pantalla el factorial de ese número.
num_factorial = int(input("ingrese el numero a factorial: "))
factorial = []
for i in range(1, num_factorial):
    num_factorial *= i
    factorial.append(num_factorial)
print(factorial)
