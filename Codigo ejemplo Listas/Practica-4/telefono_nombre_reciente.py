#Escribir un programa que pida al usuario 10 nombres (o teléfonos) y los almacene en una lista (llamadas recientes).
# Esa lista debe estar ordenada con los nombres/teléfonos más recientes
# primero así como se ordenan las llamadas recientes en tu celular de la más reciente a la más antigua


desicion= input('Desea guardad Nombres o Telefonos?: ')

while True:
    if desicion=='nombre' or desicion == 'nombres':
        valor_nombre = list(input('ingrese los nombres (separe con espacios): ').split() ) # The list class takes an iterable and returns a list object.
        print(valor_nombre)
        if len(valor_nombre) < 10 or len(valor_nombre) > 10:
            print('Debe ingresar 10 nombres')  # We can't pass a map object to the len() function but we can convert it to a list and get the length of the list.
        if len(valor_nombre) == 10:
            break

    if desicion=='telefono' or desicion == 'telefonos':
        valor = list(map(int, input( 'ingrese los telefonos sin guiones (separe con espacios): ').split()))  # The list class takes an iterable and returns a list object.
        print(valor)
        if len(valor) < 10 or len(valor) > 10:
            print('Debe ingresar 10 telefonos')  # We can't pass a map object to the len() function but we can convert it to a list and get the length of the list.
        if len(valor) == 10:
            break
if desicion == 'nombre' or desicion == 'nombres':
    valor_nombre.reverse()
    print('los nombres mas recientes fueron: ', valor_nombre)
elif desicion == 'telefono' or desicion == 'telefonos':
    valor.reverse()
    print('los telefonos mas recientes fueron: ',valor)
