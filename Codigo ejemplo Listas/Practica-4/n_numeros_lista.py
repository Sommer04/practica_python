#Escribir un programa que pida al usuario n números
# a ser introducidos por teclado y los almacene en una lista.
num_lista = int(input("Introduzca el numero de elementos a ser guardados en una lista"))
i = 1

result_lista = []
while True:
    lista_guardar = input("ingrese el numero a ser guardado: ")
    result_lista.append(lista_guardar)
    i+=1
    if i == num_lista+1:
        break
print('su lista es:\n', result_lista)