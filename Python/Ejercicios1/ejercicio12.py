def anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2): return False

    aux = palabra2[:]
    for i in range(len(palabra1)):
        encontrada = False
        j=0
        while not encontrada and j<len(aux):
            if aux[j] == palabra1[i]:
                encontrada=True
                aux = aux[0:j]+aux[j+1:]
            else: j=j+1

        if not encontrada: return False

    return True

hola = anagrama("marta","trama")
print(hola)

hola = anagrama("a","a")
print(hola)

hola = anagrama("hola","holaa")
print(hola)