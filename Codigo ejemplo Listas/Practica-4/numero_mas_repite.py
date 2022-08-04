#Escribir un programa que pida al usuario 10 números por teclado y
# muestre cuál es el valor que más se repite dentro de la lista.
i = 10
num_lista = []
while i >= 1:
    print("Valor Numero",i, "°:",sep="",end=" ")
    num_repetidos = int(input())
    num_lista.append (num_repetidos)
    i -= 1

num_lista.sort()

print(num_lista)

num_max_repetedio = max(set(num_lista), key = num_lista.count)


print("El numero que mas se repite es: ",num_lista)