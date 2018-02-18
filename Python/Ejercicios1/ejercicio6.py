def es_inversa(palabra1, palabra2):
	if len(palabra1) != len(palabra2):
		return False
	else:
		for i,j in zip(range(len(palabra1)), reversed(range(len(palabra2)))):
			if palabra1[i] != palabra2[j]:
				return False


	return True


hola = es_inversa("Hola", "aloH")
print(hola)

hola = es_inversa("ei", "ua")
print(hola)

hola = es_inversa("asdfñasdf","a2")
print(hola)