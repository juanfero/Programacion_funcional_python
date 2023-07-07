# lista vacía para almacenar los números ingresados por el usuario
numeros = []
# Iteramos 20 veces,  usuario ingrese 20 números
for i in range(20):
    num = int(input("Ingrese el número: "))
    numeros.append(num)

# Obtenemos la posición del mayor y del menor número en la lista utilizando una expresión lambda
posicion_mayor = max(range(len(numeros)), key=lambda i: numeros[i])
posicion_menor = min(range(len(numeros)), key=lambda i: numeros[i])

# Imprimimos la posición del mayor y del menor número en la lista
print(f"El número mayor es {max(numeros)} y se encuentra en la posición {posicion_mayor}")
print(f"El número menor es {min(numeros)} y se encuentra en la posición {posicion_menor}")

