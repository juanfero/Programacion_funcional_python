import random

PREMIOS = {
    1: "Bolsa Leche",
    2: "Libra de Arroz",
    3: "1 Dulce",
    4: "1 Menta",
    5: "Vuelve a Intentar",
    6: "1 Papas fritas",
    7: "10% descuento",
    8: "12% descuento",
    9: "No gana",
    10: "15% descuento"
}

def calcular_premio() -> tuple:
    #Calcula premio que ganó el usuario y retorna una tupla con el número del premio
    numero = random.randint(1, 10)
    premio = PREMIOS[numero]
    return numero, premio

def calcular_descuento(numero:int) -> float:
    #Calcula el descuento que corresponde al número del premio y lo retorna.
    #map para convertir una lista de números a una lista de descuentos.
    #filter para eliminar los elementos de la lista que son 0.
    # funcion lambda para calcular el descuento correspondiente al número del premio.
    descuentos = list(map(lambda x: 0.1 if x == 7 else (0.12 if x == 8 else (0.15 if x == 10 else 0)), PREMIOS.keys()))
    descuentos = list(filter(lambda x: x != 0, descuentos))
    return descuentos[numero-7] if descuentos else 0

def calcular_valor_a_pagar(descuento:float) -> float:
    #Calcula el valor que el usuario tiene que pagar después de aplicar el descuento y lo retorna."""
    precio_total = float(input("Ingrese el valor total de su compra: "))
    valor_a_pagar = precio_total - (precio_total * descuento)
    return valor_a_pagar

def main():

    numero, premio = calcular_premio()
    print(f"Felicitaciones! Usted ha ganado: {premio}")
    descuento = calcular_descuento(numero)
    if descuento > 0:
        print(f"Además, usted tiene un descuento del {descuento*100}% en su compra")
    valor_a_pagar = calcular_valor_a_pagar(descuento)
    print(f"El valor a pagar es: {valor_a_pagar}")

if __name__ == '__main__':
    main()