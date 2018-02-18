def eliminar_letra(cad, letra):
	aux=""
	for i in cad:#range(len(cad)):
		if i != letra:
			aux = aux+i


	return aux



hola = eliminar_letra("hola lola", 'l')
print hola