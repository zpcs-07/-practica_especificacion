class calificacion(object):
    def  __init__(self):
        self.parcial1 = 0
        self.parcial2 = 0
        self.parcial3 = 0
        self.nota = 0

    def leerParciales(self):
        self.parcial1 = float(input("Ingrese la nota del primer parcial: "))
        self.parcial2 = float(input("Ingrese la nota del segundo parcial: "))
        self.parcial3 = float(input("Ingrese la nota del tercer parcial: "))
    
    def calcularFinal(self):
        self.nota = (self.parcial1 + self.parcial2 + self.parcial3) / 3
        return self.nota    

    def determinarEstado(self):
        if self.nota >= 6:
            return "Aprobado"
        else:
            return "Reprobado"

    def mostrarResultado(self):
        estado = self.determinarEstado()
        print(f"Nota final: {self.nota:.2f}, Estado: {estado}")