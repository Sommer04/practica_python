#Escribir un programa que pida al usuario n entradas. El usuario deberá introducir el nombre de un articulo y su precio,
#almacenar esta información en un diccionario. Luego de completar las entradas entonces el sistema le debe pedir
# al usuario n artículos y una cantidad asociada y mostrar en pantalla el sub-total por articulo y el total general.

cantidad_articulo = int(input('introduzca la cantidad de articulos que desea comprar: '))
articulo_precio = { }
cantidad_precio = { }
for i  in range(0,cantidad_articulo) :
    articulo = input('introduzca el articulo a comprar: ')
    precio = int(input('introduzca el precio: '))
    articulo_precio[articulo]= precio

print(articulo_precio)

for i in articulo_precio.keys():
    articulo_pagar = input('introduzca el nombre del articulo a pagar : ')
    if articulo_pagar in articulo_precio.keys():
        articulo_cantidad = int(input('introduzca la cantidad a llevar '))
        cantidad_precio [articulo_pagar] = articulo_cantidad
        subtotal_precio = articulo_precio.get(articulo_pagar)
        subtotal_total= subtotal_precio * articulo_cantidad
        print( cantidad_precio)
        print(cantidad_precio)
        for c, a in cantidad_precio.items():
            print(f"{c}*{a}= {subtotal_total}")
    else:
        break
    break







