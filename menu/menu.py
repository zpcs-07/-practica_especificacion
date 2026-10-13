from ejercicios import ejercicio1_luz as ej1 
from ejercicios import ejercicio2_calificacion as ej2 
from ejercicios import ejercicio3_compra as ej3 
from ejercicios import ejercicio4_estacionamiento as ej4 
 
 
def ejecutarEjercicio1(): 
    minutos = ej1.leerMinutos()
    cobro = ej1.calcularCobro(minutos)
    ej1.mostrarCobro(cobro)


def ejecutarEjercicio2(): 
    minutos = ej2.leerMinutos()
    calificacion = ej2.calcularCalificacion(minutos)
    ej2.mostrarCalificacion(calificacion)


def ejecutarEjercicio3(): 
    minutos = ej3.leerMinutos()
    total = ej3.calcularTotal(minutos)
    ej3.mostrarTotal(total)


def ejecutarEjercicio4(): 
    minutos = ej4.leerMinutos()
    cobro = ej4.calcularCobro(minutos)
    ej4.mostrarCobro(cobro)


def mostrarMenu(): 
    print() 
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Recibo de luz") 
    print("2. Calificación final") 
    print("3. Total de compra") 
    print("4. Estacionamiento") 
    print("0. Salir") 
 
 
def menus(): 
    opcion = "" 
    while opcion != "0": 
        mostrarMenu() 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            ejecutarEjercicio1() 
        elif opcion == "2": 
            ejecutarEjercicio2() 
        elif opcion == "3": 
            ejecutarEjercicio3() 
        elif opcion == "4": 
            ejecutarEjercicio4() 
        elif opcion != "0": 
            print("Opción no válida.")