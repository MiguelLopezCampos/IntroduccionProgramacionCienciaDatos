def contar_letras(palabra):
    lista = []
    i=0
    while(len(palabra)!=0):
        contador_letra = 1
        letra = palabra[i]
        palabra=palabra[0:i]+palabra[i+1:]
        j = 0
        while(j < len(palabra)):
            if palabra[j] == letra:
                contador_letra+=1
                palabra=palabra[0:j]+palabra[j+1:]
            else: j+=1
        lista.append((letra, contador_letra))

    return lista


hola = "Buenaas taaaaaardesss"
x = contar_letras(hola)
print(x)
