from clases.ejemplo.calculadora import calculadora
class menu(object):
    def __init__(self):
        self.opcion = 0

    def mostrarMenu(self):
        print("Ejemplo programa con POO")
        print("1. Calculadora")
        print("0. Salir")

    def ejecutar(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrarMenu()
            self.opcion = input("Seleccione una opción: ")
            if self.opcion == "1":
                casio = calculadora()
                casio.leerNumeros()
                casio.calcularSuma()
                casio.mostrarSuma()
            else:
                print("Opción no válida.")
