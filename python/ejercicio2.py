#se definen las notas 
parciales = 4.5
examen = 4.2
trabajo = 5

# Función para calcular la calificación final
calificacion_final = lambda parciales, examen, trabajo: 0.55 * parciales + 0.3 * examen + 0.15 * trabajo

# Calcular la calificación final utilizando la función lambda e imprimo rsultado
print('la calificacion final es de: ' ,calificacion_final(parciales, examen, trabajo)) 

