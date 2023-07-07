longitud_vector = int(input("Ingrese la longitud del vector: "))
#se define la longitud del vector 

# Crear el vector utilizando programación funcional
# se transforma y crea en nuevo vector con el rango que se definio anteriormente
vector = list(map(lambda x: int(input("Ingrese el elemento: ")), range(longitud_vector)))

# Calcular el número mayor y menor utilizando programación funcional
maximo = max(vector)
minimo = min(vector)

print("El número mayor es:", maximo)
print("El número menor es:", minimo)

