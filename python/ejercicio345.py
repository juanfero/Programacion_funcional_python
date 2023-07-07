
total= 1000 #defino total de la compra 
numero_escogido = int(input('digite numero: ')) #elegir numero 

#defino la lamda con dos argumentos. Utiliza condicional para definir que descuento se le da 
descuento = lambda total, numero: total * 0.15 if numero < 74 else total * 0.20 
#se guarda en una variable la funcion 
promocion = descuento(total, numero_escogido)
#imprime 
print(promocion)







