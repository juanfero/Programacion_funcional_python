from functools import reduce
sueldo = 1000  #sueldo base
ventas = [123, 456, 876]  #lista 

# función lambda para calcular la comisión de cada venta
comision = lambda venta: venta * 0.1

# función para calcular el total de ingresos del vendedor en el mes
#  reduce() se utiliza para sumar todas las comisiones de las ventas
def ingresos_mes(sueldo, ventas):
    comisiones = reduce(lambda x, y: x + y, map(comision, ventas))
    total = sueldo + comisiones
    return (total)
total=ingresos_mes(sueldo, ventas)
print("el sueldo total es de: ", total)






