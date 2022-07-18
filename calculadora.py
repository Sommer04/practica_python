print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")

opcion = int(input("Seleccione una opción: "))
if 1 <= opcion <= 4:  # opcion >=1 and opcion <=4
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese Otro numero: "))

if opcion == 1:
    print(numero1, " + ", numero2, " = ", numero1 + numero2)
elif opcion == 2:
    print(numero1, " - ", numero2, " = ", numero1 - numero2)
elif opcion == 3:
    print(numero1, " X ", numero2, " = ", numero1 * numero2)
elif opcion == 4:
    print(numero1, " / ", numero2, " = ", numero1 / numero2)
else:
    print("Opción incorrecta!")
