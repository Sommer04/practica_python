#Escribir un programa que lea 10
# números por teclado, los almacene en una lista y muestre en pantalla
# cuál es el valor mínimo y máximo de esta lista.

#notas de aprendizaje:

while True:
    valor = list(map(int,input('ingrese los numeros (separe con espacios): ').split()))#The list class takes an iterable and returns a list object.
    print(valor)
    if len(valor) < 10 or len(valor)>10:
        print('Debe ingresar 10 numeros')  #We can't pass a map object to the len() function but we can convert it to a list and get the length of the list.
    else:
        break

print('El numero menor es:',min(valor),  'el numero mayor es: ',max(valor))