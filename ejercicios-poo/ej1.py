class persona:
    def inicializacion(self,nombre):
        self.nom=nombre
    

    def mostrar(self):
        print(f'Nombre {self.nom}')
persona1 = persona()
persona1.inicializacion("gringo")
print(persona1.mostrar())