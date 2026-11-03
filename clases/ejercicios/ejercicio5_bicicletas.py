class Bicicleta:
    def __init__(self):
        self.horas = 0
        self.total = 0.0

    def leerHoras(self) -> int:
        self.horas = int(input("Ingrese las horas de renta: "))
        return self.horas

    def calcularRenta(self, horas: int) -> float:
        if horas <= 1:
            return 5.0
        elif horas <= 3:
            return 5.0 + (horas - 1) * 4.0
        else:
            return 5.0 + 2 * 4.0 + (horas - 3) * 3.0

    def mostrarRenta(self, total: float) -> None:
        print(f"Total a pagar: ${total:.2f}")
