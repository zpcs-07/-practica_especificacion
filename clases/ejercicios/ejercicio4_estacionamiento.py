class Estacionamiento:
    def __init__(self):
        self.minutos = 0

    def leerMinutos(self) -> int:
        self.minutos = int(input("Ingrese los minutos de estancia: "))
        return self.minutos

    def calcularCobro(self) -> float:
        if self.minutos <= 60:
            return 20.0
        else:
            horas_adicionales = (self.minutos - 60 + 59) // 60
            return min(20 + horas_adicionales * 15, 150)

    def mostrarCobro(self) -> None:
        cobro = self.calcularCobro()
        print(f"El cobro a pagar es: ${cobro:.2f}") 