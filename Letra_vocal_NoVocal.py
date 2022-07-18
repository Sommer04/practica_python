#4 - Escribir un programa que pida al usuario una letra, y si es vocal
# muestre el mensaje "Es vocal", de lo contrario que muestre "No es vocal"
letra_vocal = input("Digite la Vocal: ")

if letra_vocal == "a" or  letra_vocal == "e" or letra_vocal == "i" or letra_vocal == "o" or letra_vocal == "u" :
    print("La vocal es: ", letra_vocal)
elif letra_vocal == "A" or  letra_vocal == "E" or letra_vocal == "I" or letra_vocal == "O" or letra_vocal == "U" :
    print("La vocal es: ", letra_vocal)
else:
    print("La letra introducida no es una vocal")
