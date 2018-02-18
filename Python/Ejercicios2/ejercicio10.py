import generar_lista

def parejas(lista):
    lista_parejas = []

    while(len(lista) != 0):
        lista_aux = lista[:]
        letra = lista[0]
        j=1
        while j < len(lista_aux):
            if letra != lista_aux[j]:
                lista_parejas.append((letra,lista_aux[j]))
                letra2 = lista_aux[j]
                while lista_aux.count(letra2) != 0:
                    lista_aux.remove(letra2)
            else: j+=1
        while lista.count(letra):
            lista.remove(letra)

    return lista_parejas


l = generar_lista.generar_lista(10, 1, 5)
print(l)
hola = parejas(l)
print(hola)