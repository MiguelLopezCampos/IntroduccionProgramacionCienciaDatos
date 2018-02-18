def contar_letras(palabra, letra):
	cont=0
	for i in palabra:
		if(i==letra):
			cont+=1

	return cont

def vocales(cad):
	aux=""
	for i in range(len(cad)):
		if (cad[i]=='a' or cad[i]=='e' or cad[i]=='i' or cad[i]=='o' or cad[i]=='u') and contar_letras(aux,cad[i])==0:
			aux=aux+cad[i]

	return aux



a = vocales("holaaa")
print(a)