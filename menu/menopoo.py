from clases.ejercicios import ejercicio1_luz
from clases.ejercicios import ejercicio2_calificacion
from clases.ejercicios import ejercicio3_compra
from clases.ejercicios import ejercicio4_estacionamiento
from clases.ejercicios import ejercicio5_bicicletas

class menu(object):
    def __init__(self):
        self.opcion = 0

    def mostrarMenu(self):
        print("Ejemplo programa con POO")
        print("1. Luz")
        print("2. Calificación")
        print("3. Compra")
        print("4. Estacionamiento")
        print("5. Bicicleta")
        print("0. Salir")

    def ejecutar(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrarMenu()
            self.opcion = input("Seleccione una opción: ")
            if self.opcion == "1":
                luz = ejercicio1_luz.luz()
                luz.leerConsumo()
                luz.mostrarRecibo()
            elif self.opcion == "2":
                calif = ejercicio2_calificacion.calificacion()
                calif.leerParciales()
                calif.calcularFinal()
                calif.mostrarResultado()
            elif self.opcion == "3":
                compra = ejercicio3_compra.Compra()
                compra.leerSubtotal()
                compra.calcularDescuento()
                compra.iva = compra.calcularIVA()
                compra.calcularTotal()
                compra.mostrarTicket()
            elif self.opcion == "4":
                estacionamiento = ejercicio4_estacionamiento.Estacionamiento()
                estacionamiento.leerMinutos()
                estacionamiento.mostrarCobro()
            elif self.opcion == "5":
                bicicleta = ejercicio5_bicicletas.Bicicleta()
                bicicleta.leerHoras()
                bicicleta.total = bicicleta.calcularRenta(bicicleta.horas)
                bicicleta.mostrarRenta(bicicleta.total)
            else:
                print("Opción no válida.")
