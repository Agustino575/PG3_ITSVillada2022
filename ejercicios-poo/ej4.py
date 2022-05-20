class Operaciones():
    def __init__(self, entero1, entero2):
        self.entero1 = entero1
        self.entero2 = entero2
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        self.sumar = self.entero1 + self.entero2
        print('suma: ',self.sumar)

    def resta(self):
        self.restar = self.entero1 - self.entero2
        print('resta: ',self.restar)

    def multiplicacion(self):
        self.multiplicar = self.entero1 * self.entero2
        print('multiplicacion: ',self.multiplicar)

    def division(self):
        self.dividir = self.entero1 / self.entero2
        print('division: ',self.dividir)

op = Operaciones(4,8)