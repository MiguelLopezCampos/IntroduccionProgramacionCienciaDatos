import generar_lista

def suma_acumulada(numeros):
    lista = []
    for i in range(len(numeros)):
        sum_acum = 0
        for j in range(0,i+1):
            sum_acum+=numeros[j]

        lista.append(sum_acum)

    return lista


l = generar_lista.generar_lista(4,1,10)
print(l)
hola = suma_acumulada(l)
print(hola)