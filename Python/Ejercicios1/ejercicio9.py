def palindromo(frase):
	i=0
	j=len(frase)-1
	while i < len(frase) and j>i:
		if frase[i]==' ':
			i=i+1
		elif frase[j]==' ':
			j=j-1
		elif frase[j] != frase[i]:
			return False
		else:
			i=i+1
			j=j-1

	return True



hola = palindromo("buenassaneub")
print(hola)
hola = palindromo("buenassane  ub")
print(hola)
hola = palindromo("bu enassaneub")
print(hola)
hola = palindromo("buenaseasaneub")
print(hola)
hola = palindromo("buenasea saneub")
print(hola)