#4 - Escribir un programa que pida al usuario una letra, y si es vocal
# muestre el mensaje "Es vocal", de lo contrario que muestre "No es vocal"
letra_vocal = str(input("Digite la Vocal: "))

if letra_vocal == "a" or "e" or "i" or "o" or "u":
    print("La vocal es: ", letra_vocal)

else:
    print("La letra introducida no es una vocal")

