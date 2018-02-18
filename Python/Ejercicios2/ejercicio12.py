import generar_lista

def suma_primer_digito(numeros):
    suma = 0
    for i in numeros:
        aux = str(i)
        aux = aux[0]
        suma+=int(aux)

    return suma


l = generar_lista.generar_lista(5, 1, 100000)
print(l)
hola = suma_primer_digito(l)
print(hola)