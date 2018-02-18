def eco_palabra(palabra):
	aux=""
	for i in range(len(palabra)):
		aux=aux+palabra

	return aux


hola = eco_palabra("hola")
print(hola)

hola = eco_palabra("esternocleidomastoideo")
print(hola)