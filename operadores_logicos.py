# Operadores lógicos
# and or not (conjunción, disyunción, negación)

# and (ambas deben ser verdaderas)
# or (solo sera falsa si ambas son falsas)
# not (valor opuesto)

num1 = 90
num2 = 89

print(num1 > num2 and num2 < 100 and num1 == 90 and 10 > 10)  # False
print(num1 > num2 and num2 < 100 and num1 == 90 or 10 > 10)  # True
print(not(num1 > num2 and num2 < 100 and num1 == 90 and 10 > 10))  # True

