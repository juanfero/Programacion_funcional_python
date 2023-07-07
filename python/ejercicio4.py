# Programación funcional
#Juan Felipe Rojas. 
#Universidad Sergio Arboleda 


convertir_romano = lambda numero_romano: (lambda romanos: romanos[numero_romano])({
    1: 'I', 
    2: 'II', 
    3: 'III', 
    4: 'IV', 
    5: 'V', 
    6: 'VI', 
    7: 'VII', 
    8: 'VIII', 
    9: 'IX', 
    10: 'X'
})

numero_elegido = int(input('Ingrese un número entre 1-10: '))

numero_romano = convertir_romano(numero_elegido)
print("El número en romano es:", numero_romano)
