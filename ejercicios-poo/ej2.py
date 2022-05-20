 class alumno:
    def notas(self,nota):
        if int(nota)>=6:
            return("aprobado")
        else:
            return('desprobado')
    def __init__(self, nom,nota):
        self.nombre=nom
        self.nota=nota
        
    def __str__(self):
        print("Nombre: "+str(self.nombre))
        print("Nota: "+str(self.nota))
        return self.notas(self.nota)


alumno1=alumno("santiago","8")
alumno2=alumno("agustin","5")
print(alumno1)
print(alumno2)