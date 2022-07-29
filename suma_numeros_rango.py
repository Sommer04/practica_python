#* Escribir un programa que calcule y muestre en pantalla la suma de todos los
# números comprendidos en un rango dado, debe leer por teclado el valor inicial y final de dicho rango.

num_inicial = int(input("ingrese el numero inicial: "))
num_final = int(input("ingrese el numero final: "))
sum_rango = []

for i in range(num_inicial+1, num_final+1):
    num_inicial += i
    sum_rango.append(num_inicial)
print(sum_rango)