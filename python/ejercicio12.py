# Almacenar 15 valores ingresados por el usuario. utiilizando la funcion lambda 
valores = list(map(lambda _: int(input("Ingrese un valor: ")), range(15)))

# Ordenar los valores con la funcion sorted 
valores_ordenados = sorted(valores, reverse=True)

print("Valores en orden inverso:", valores_ordenados)

