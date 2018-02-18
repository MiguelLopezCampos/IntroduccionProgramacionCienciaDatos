def buscar(cad, sub):
	encontrado = False
	i = 0

	while not encontrado and i < len(cad) :
		if cad[i] == sub[0] :
			salir = False
			j = 0
			k = i
			while j < len(sub) and not salir and k < len(cad):
				if cad[i] != sub[j]:
					salir = True
					k+=1
					j+=1
			if not salir:
				encontrado = True
		i+=1
	if encontrado:
		return i
	else:
		return -1




ei = buscar("hola buenas", "l")
ei

