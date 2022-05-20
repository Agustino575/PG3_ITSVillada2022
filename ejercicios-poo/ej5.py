class Persona:
    def __init__(self,):
        self.name = 'gringo'
        self.edad = 18

    def myfunc(self):
        print("nombre ", self.name + " ,edad", self.edad)

class Empleado(Persona):
    def __init__(self, sueldo):
        Persona.__init__(self)
        self.sueldo = sueldo

        Persona.myfunc(self)
        self.pagarImpuestos()

    def pagarImpuestos(self,):
        if self.sueldo > 3000:
            print('debe pagar impuestos, su sueldo es: ', self.sueldo)
        if self.sueldo <= 3000:
            print('no debe pagar impuestos, su sueldo es: ', self.sueldo)

e1 = Empleado(4000)
