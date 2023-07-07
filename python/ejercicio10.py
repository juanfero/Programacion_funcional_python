# Programación funcional
#Juan Felipe Rojas. 
#Universidad Sergio Arboleda 


# Función que calcula el precio a pagar por un cliente
def calcular_precio(kilos):
    precio_kilo = 50 # Precio por kilo
    descuento = 0.15 # Descuento del 15%
    if kilos > 10:
        precio_sin_descuento = kilos * precio_kilo
        precio_con_descuento = precio_sin_descuento * (1 - descuento)
        return precio_con_descuento
    else:
        return kilos * precio_kilo

# Función que calcula el precio a pagar por cada cliente y el total percibido por la tienda
def calcular_precios(kilos_clientes):
    precios_clientes = list(map(calcular_precio, kilos_clientes))
    total_pagado = sum(precios_clientes)
    total_descuento = sum(list(filter(lambda precio: precio > 500, precios_clientes))) * 0.15
    return precios_clientes, total_pagado - total_descuento

# Ejemplo de uso
kilos_clientes = [12, 8, 15, 6, 11, 7, 10, 13, 9, 14, 10, 11, 12, 8, 15]
precios_clientes, total_percibido = calcular_precios(kilos_clientes)
for i, precio in enumerate(precios_clientes):
    print("El cliente", i+1, "pagará:", precio)
print("La tienda percibirá:", total_percibido)



