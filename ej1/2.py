#2) ES BISIESTO??
#Escriba un programa que pregunte un año y que escriba si es bisiesto o no.
#Se debe pasar por parámetro el año a una función.
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los
#múltiplos de 400 sí.
#Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto,
#1900 no es bisiesto.
año = int(input(("escriba un año ")))
if año % 4 == 0:
    print (" es un año bisiesto: ", año)
else:
    print(" no es bisiesto {}".format(año)) 
