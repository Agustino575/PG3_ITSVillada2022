#3) PINTAMEEEEEE
#Escriba un programa que pida ancho y alto de un rectángulo y el caracter a utilizar en el dibujo.
#Ejemplo:
#Pedido:
#Ancho: 5
#Alto: 4
#Caracter: 'A'
#Imprime:
#A A A A A
#A A A A A
#A A A A A
#A A A A A
import string


nf = int(input("coloque el numero de filas: "))
nc = int(input("coloque el numero de columnas: "))
ca = str(input("coloque con que caracter quiere hacerlo: "))


for i in range (1,nf+1):
    for j in range (1,nc+1):
        print(ca,end=" ")
    print(" ")    