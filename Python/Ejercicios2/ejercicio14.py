import random
import generar_lista

def sacar_carta(baraja):
    baraja_aleatoria = []

    while(len(baraja)!= 0):
        r = random.randint(0, len(baraja)-1)
        baraja_aleatoria.append(baraja[r])
        del baraja[r]

    return baraja_aleatoria


baraja = generar_lista.generar_lista(10, 1, 30)
print(baraja)
ei = sacar_carta(baraja)
print(ei)

