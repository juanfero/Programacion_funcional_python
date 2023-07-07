# Diccionario de descuentos por código de cajero
descuentos = {
    1: 2,
    2: 3,
    5: 5,
    7: 8,
    10: 10,
    11: 15
}

# Función para aplicar el descuento según el código del cajero
aplicar_descuento = lambda venta, codigo: venta * (1 - descuentos.get(codigo, 0) / 100)

# Ingresar el total de la venta y el código del cajero
venta_total = float(input("Ingrese el total de la venta: "))
codigo_cajero = int(input("Ingrese el código del cajero: "))

# Calcular el descuento aplicado
descuento = venta_total - aplicar_descuento(venta_total, codigo_cajero)

# Mostrar el total de la venta y el descuento realizado
print("Total de la venta:", venta_total)
print("Obtendrá un descuento de:", descuento)
