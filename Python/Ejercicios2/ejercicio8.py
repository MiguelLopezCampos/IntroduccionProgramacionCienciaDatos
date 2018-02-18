def eliminar(l1,l2):
    lista = []
    for i in l1:
        encontrado = False
        j=0
        while not encontrado and j < len(l2):
            if i == l2[j]:
                encontrado=True
            j+=1
        if not encontrado:
            lista.append(i)

    return lista

l1 = [1,2,3,4,5]
print(l1)
l2 = [2,4,8,0]
print(l2)
l3 = eliminar(l1,l2)
print(l3)