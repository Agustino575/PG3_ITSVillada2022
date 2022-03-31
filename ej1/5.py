#5) PALINDROMOS
#Escribir una función que reciba como parámetro una palabra, y devuelva True si esa palabra es un
#palíndromo y False si no lo es.
#Ejemplo:
#esCapicua("neuquen") === True
#esCapicua("jovenes") === Fals

from operator import truediv


palabra = str(input("escriba una poalabra para saber si es palindrome o no: "))
if str(palabra) == str(palabra)[::-1] :
    print(palabra," es ",True)
else:
    print(palabra," es ",False)