class luz(object):
    def  __init__(self):
        self.consumo = 0
        self.importe = 0

    def leerConsumo(self):
        self.consumo = float(input("Ingrese el consumo en kWh: "))
        self.importe = float(input("Ingrese el importe por kWh: "))

    def calcularPago(self):
        return self.consumo * self.importe

    def mostrarRecibo(self):
        total = self.calcularPago()
        print(f"El total a pagar es: {total}")