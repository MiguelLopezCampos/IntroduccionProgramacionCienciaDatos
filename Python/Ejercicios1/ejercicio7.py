def contar_letras(palabra, letra):
	cont=0
	for i in palabra:
		if(i==letra):
			cont+=1

	return cont

def comunes(palabra1, palabra2):
	aux=""
	for i in palabra1:
		for j in palabra2:
			if i==j and contar_letras(aux,i)==0:
				aux=aux+i

	return aux



hola = comunes("hola", "buenas")
print(hola)

hola = comunes("barceelona", "meexico")
print(hola)