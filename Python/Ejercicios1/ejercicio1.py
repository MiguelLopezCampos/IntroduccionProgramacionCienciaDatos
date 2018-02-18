def contar_letras(palabra, letra):
	cont=0
	for i in palabra:
		if(i==letra):
			cont+=1

	return cont


hola = contar_letras("palabraaaa", "a")
print(hola)