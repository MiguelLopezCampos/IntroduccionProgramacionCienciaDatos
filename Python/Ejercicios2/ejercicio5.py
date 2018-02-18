import generar_lista

def mezclar(l1,l2):
    l1.extend(l2)
    #Supongo que no puedo usar la función sort
    aux=[]
    while len(l1) != 0:
        minimo = min(l1)
        aux.extend([minimo])
        l1.remove(min(l1))
    return aux


l1=generar_lista.generar_lista(5,1,1000)
print(l1)
l2=generar_lista.generar_lista(2,1,1000)
print(l2)
l = mezclar(l1,l2)
print(l)