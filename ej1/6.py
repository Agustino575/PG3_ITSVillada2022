#6) A CONTAR VOCALES!
#Escribir una función que reciba como parámetro una frase y devuelva la cantidad de vocales que ésta tiene.
def cont_v(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

cadena = str(input("escriba una frase: "))
cantidad = cont_v(cadena)
print(f"En la cadena '{cadena}'' hay {cantidad} vocales")