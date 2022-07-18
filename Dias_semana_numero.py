#2 - Escribir un programa que pida al usuario el dia de la semana en numeros
# y lo muestre en letras (ej: 1 - Domingo, 2 - Lunes, 3 - Martes, etc).

Dia_numero = int(input("Digite el numero del dia de la semana: "))

if Dia_numero==1:
    print("Es Domingo")
elif Dia_numero==2:
    print("Es Lunes")
elif Dia_numero == 3:
    print("Es Martes")
elif Dia_numero==4:
    print("Es Miercoles")
elif Dia_numero==5:
    print("Es Jueves")
elif Dia_numero==6:
    print("Es Viernes")
elif Dia_numero==7:
    print("Es Sabado")
else:
    print("Numero invalido")