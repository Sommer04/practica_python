# Escribir un programa que defina una función que reciba 2 parámetros (una lista de valores y un valor)
# y retorne True si el valor esta en la lista y False si el valor no esta en la lista.

def listavalores(lista,valor):
    if valor in lista:
        return True
    else:
        return False

lista =  list(map(int,input('ingrese los numeros (separe con espacios): ').split()))
valor = int(input('escriba el valor a buscar en la lista: '))

print(listavalores(lista,valor))