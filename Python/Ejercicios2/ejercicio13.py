def dispersa(v):
    lista = []
    for i in range(len(v)):
        if v[i] != 0:
            lista.append((i, v[i]))

    lista = (lista, len(v))

    return lista



l = [0,0,0,0,1,2,3,0,0,0,0,10,1,0,0,0,0]
print(l)
l = dispersa(l)
print(l)