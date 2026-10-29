from ejercicios.ejercicio1_luz import leerConsumo, calcularPago, mostrarRecibo 
from ejercicios.ejercicio2_calificacion import leerParciales, calcularFinal, determinarEstado, mostrarResultado

 
 
 
def ejecutarEjercicio1(): 
    consumo = leerConsumo()
    cobro = calcularPago(consumo)
    mostrarRecibo(cobro)


def ejecutarEjercicio2(): 
    parciales = leerParciales()
    calificacion_final = calcularFinal(parciales)
    estado = determinarEstado(calificacion_final)
    mostrarResultado(calificacion_final, estado)




def mostrarMenu(): 
    print() 
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Recibo de luz") 
    print("2. Calificación final") 
  
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
        elif opcion != "0": 

            print("Opción no válida.")