


num_primo = float(input("Ingrese el numero: "))
a= num_primo
while a == num_primo:
    num_primo = float(input("Ingrese el numero: "))
    if num_primo % 2 != 1:
        print(num_primo, "No es un numero primo")
        continue
    print(num_primo, "es un numero primo")





