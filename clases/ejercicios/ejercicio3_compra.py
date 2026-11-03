
class Compra:   
    def __init__(self):
        self.subtotal = 0.0
        self.descuento = 0.0
        self.iva = 0.0
        self.total = 0.0

    def leerSubtotal(self) -> float:
        self.subtotal = float(input("Ingrese el subtotal de la compra: "))
        return self.subtotal

    def calcularDescuento(self) -> float:
        if self.subtotal >= 5000:
            self.descuento = self.subtotal * 0.2
        elif self.subtotal >= 1000:
            self.descuento = self.subtotal * 0.1
        else:
            self.descuento = 0.0

    def calcularIVA(self) -> float:
        return (self.subtotal - self.descuento) * 0.16

    def calcularTotal(self) -> float:
        self.total = round(self.subtotal - self.descuento + self.iva, 2)
        return self.total   

    def mostrarTicket(self) -> None:
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Descuento: ${self.descuento:.2f}")
        print(f"IVA: ${self.iva:.2f}")
        print(f"Total: ${self.total:.2f}")