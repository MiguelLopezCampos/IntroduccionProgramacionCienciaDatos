def trocear(palabra,num):
    resultado=[]

    if num>len(palabra):
        print("El número es mayor que el tamaño de la palabra. Se devuelve lista vacía")
        return resultado

    cont = 0
    aux=""
    for i in range(len(palabra)):


        if cont<num:
            aux=aux+palabra[i]
            cont=cont+1
        else:
            cont=1
            resultado.extend([aux])
            aux=""+palabra[i]

    resultado.extend([aux])
    return resultado


hola = trocear("holaa", 2)
print(hola)

hola = trocear("holaa", 10)
print(hola)

hola = trocear("buenastardes", 5)
print(hola)
