#BUSCAR ADENTRO!!!
#Generar un programa, que le permita al usuario buscar un valor dentro de una lista pre-construido y que nos
#devuelva el lugar que ocupa.
##Para ello se deberá utilizar una función que a partir de dos parámetros (la lista. y el elemento buscado) nos
#devuelva el índice.
#Por ejemplo, se busca el número 12 dentro del vector [8,12,9,45], la función devolverá el número 1, que es
#el índice donde se encuentra el elemento buscado.
lista = [1,2,3,4,5,6,7]
variable = int(input("ponga un numero"))
print(lista.index(variable))
