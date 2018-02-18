import generar_lista

def numeros_pares(numeros):
    pares = []
    for i in numeros:
        if i%2==0:
            pares.append(i)

    return pares

hola = generar_lista.generar_lista(1000, 1, 1000)
pares = numeros_pares(hola)
print(pares)