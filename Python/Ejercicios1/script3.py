def num_vocales(cad):
	num_vocales = 0
	for i in range(len(cad)):
		if cad[i]=='a' or cad[i]=='e' or cad[i]=='i' or cad[i]=='o' or cad[i]=='u':
			num_vocales+=1

	return num_vocales



a = vocales("hola")
print(a)