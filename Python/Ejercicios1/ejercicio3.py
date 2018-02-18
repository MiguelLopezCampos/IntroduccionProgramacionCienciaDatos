def buscar(palabra, sub):
    for i in range(len(palabra)):
        if len(palabra)-i < len(sub): return -1

        if palabra[i] == sub[0]:
            no_coincide = False
            j = 1
            while not no_coincide and j<len(sub):
                if palabra[i+j] != sub[j]:
                    no_coincide = True

                j = j+1

            if not no_coincide: return i


    return -1


hola = buscar("hola", "la")
print(hola)

hola = buscar("hola", "las")
print(hola)

hola = buscar("hola", "hola")
print(hola)

hola = buscar("hola", "holaaa")
print(hola)

hola = buscar("hola", "ci")
print(hola)