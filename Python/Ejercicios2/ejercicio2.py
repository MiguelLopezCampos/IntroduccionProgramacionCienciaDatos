import generar_lista

def contar_numeros_impares(numeros):
    impares=0
    for i in numeros:
        if i%2 != 0:
            impares+=1


    return impares


lista = generar_lista.generar_lista(1000, 1, 1000)
hola = contar_numeros_impares(lista)
print(hola)