from clases.ejercicios import ejercicio1_luz
from clases.ejercicios import ejercicio2_calificacion

class menu(object):
    def __init__(self):
        self.opcion = 0

    def mostrarMenu(self):
        print("Ejemplo programa con POO")
        print("1. Luz")
        print("2. Calificación")
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
            else:
                print("Opción no válida.")
