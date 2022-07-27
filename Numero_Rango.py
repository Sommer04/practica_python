#* Escribir un programa que pida al usuario 2 números
# y muestre todos los números comprendidos en ese rango.

num_primero = int (input("ingrese el primer numero: "))
num_segundo = int (input("ingrese el segundo numero: "))
lista_rango = []
for i in range(num_primero, num_segundo+ 1):
    lista_rango.append(i)
print("El rango comprendido entre los dos numeros es: ",lista_rango)

