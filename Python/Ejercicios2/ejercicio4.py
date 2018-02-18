import generar_lista

def combinar_listas(l1,l2):
    l1.extend(l2)
    return l1


l1 = generar_lista.generar_lista(5, 1, 1000)
l2 = generar_lista.generar_lista(2, 1, 1000)
l = combinar_listas(l1,l2)
print(l)