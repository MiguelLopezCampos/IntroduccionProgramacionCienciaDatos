import random
import time

def generar_lista(n, lim1=1, lim2=-1):
    if (lim2 == -1):
        lim2 = n
    l = []
    for i in range(n):
        l.append(random.randint(lim1, lim2))

    return l