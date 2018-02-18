def orden_alfabetico(palabra):
	for i in range(len(palabra)-1):
		if palabra[i]>palabra[i+1]:
			return False


	return True


hola = orden_alfabetico("abcdefgh")
print(hola)

hola = orden_alfabetico("zabcd")
print(hola)