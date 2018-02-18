import generar_lista

def traspuesta(matriz):
    traspose = []
    #Supongo que en la matriz todas las filas tienen las mismas columnas
    for j in range(len(matriz[0])):
        aux = []
        for i in range(len(matriz)):
            aux.extend([matriz[i][j]])

        traspose.append(aux)

    return traspose

matriz = []
matriz.append(generar_lista.generar_lista(3, 1, 1000))
matriz.append(generar_lista.generar_lista(3,1,1000))
matriz.append(generar_lista.generar_lista(3,1,1000))
print(matriz)

matriz = traspuesta(matriz)
print(matriz)
