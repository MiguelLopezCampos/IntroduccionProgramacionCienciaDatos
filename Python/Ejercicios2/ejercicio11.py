def cadena_mas_larga(cadenas):
    max = len(cadenas[0])
    mayor_cadena = cadenas[0]
    for i in cadenas[1:]:
        if len(i) > max:
            max=len(i)
            mayor_cadena = i

    return mayor_cadena


cads = []
cads.append("hola buenas tardes")
cads.append("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
cads.append("ei")
cad = cadena_mas_larga(cads)
print(cad)