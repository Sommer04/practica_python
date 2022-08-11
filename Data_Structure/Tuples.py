nombres= tuple('juan, maria, pedro')
apellidos = ['peo', 5, 'mercedes']
a, b, c = tuple(apellidos)
print(a)
print(nombres)
print(type(nombres))

nombre2 = tuple(input('ingrese '))
print(nombre2)

print(nombre2[:2])
print(nombre2[2:])
print(nombre2[2::])
print(nombre2[2:6])
#deleting a tuple
del apellidos
print(apellidos)



