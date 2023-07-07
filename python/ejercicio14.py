# Programación funcional
#Juan Felipe Rojas. 
#Universidad Sergio Arboleda 

# Crear un vector de 16 posiciones y llenarlo con la funcion lambda creada, este tiene un rango de 16
#
vector = list(map(lambda x: x+1, range(16)))

# Partir el vector en dos de 8 posiciones cada uno
vector_1 = vector[:8]
vector_2 = vector[8:]

# Imprimir los vectores resultantes
print("Vector 1:", vector_1)
print("Vector 2:", vector_2)


