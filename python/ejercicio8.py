# Programación funcional
#Juan Felipe Rojas. 
#Universidad Sergio Arboleda 

numeros=[ 2, 4, 6, -8, -6, 2, 5, -7, 1, -3, 11, 16, 19,-15, -6] #defino la lista 
#Utilizo la funcion lambda. se utilixo map para la transformación de los elelemtos de la secuencia.
#Adicionalmete se utilizo la funcion abs para convertir los números. 
numeros_positivos = list(map(lambda x: abs(x) if x < 0 else x, numeros)) 

print(numeros_positivos)