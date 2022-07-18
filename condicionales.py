# Estructuras de control de flujo (selectivas y repetitivas)
# Condicionales
# indentación
# if        if-else     if-elif

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if numero1 > numero2:  # num2 > ,  ==
    print("El numero1 es mayor")
elif numero2 > numero1:
    print("Numero 2 es mayor")
else:
    print("Los numeros son iguales")


print("Bye!")