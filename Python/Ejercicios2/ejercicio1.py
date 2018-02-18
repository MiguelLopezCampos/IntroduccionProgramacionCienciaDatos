import random
import time

def generar_lista(n, lim1=1, lim2=-1):
    if (lim2 == -1):
        lim2 = n
    l = []
    for i in range(n):
        l.append(random.randint(lim1, lim2))

    return l

lista = generar_lista(1000000, 0, 100)

tiempo0 = time.time()
sum=0
for i in range(len(lista)):
    sum+=lista[i]

tiempo1 = time.time()-tiempo0
print("La suma es "+str(sum)+". Con range el tiempo de ejecución ha sido de "+str(tiempo1))

tiempo0=time.time()
sum=0
for i in lista:
    sum+=i

tiempo1 = time.time()-tiempo0
print("La suma es "+str(sum)+". Sin range el tiempo de ejecución ha sido de "+str(tiempo1))
#En los tiempos se observa cómo usar range relentiza mucho la ejecución