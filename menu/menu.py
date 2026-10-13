from ejercicios.ejercicio1_luz import leerConsumo, calcularPago, mostrarRecibo 
from ejercicios.ejercicio2_calificacion import leerParciales, calcularFinal, determinarEstado, mostrarResultado
from ejercicios.ejercicio3_compra import leerSubtotal, calcularDescuento, calcularIVA, calcularTotal, mostrarTicket
from ejercicios.ejercicio4_estacionamiento import leerMinutos, calcularCobro, mostrarCobro 
from ejercicios.ejercicio5_bicicletas import leerHoras, calcularRenta, mostrarRenta
from ejercicios.ejercicio6_cine import leerEdad, calcularPrecio, mostrarPrecio
from ejercicios.ejercicio7_multa import leerVelocidad, calcularMulta, mostrarMulta
 
 
 
def ejecutarEjercicio1(): 
    consumo = leerConsumo()
    cobro = calcularPago(consumo)
    mostrarRecibo(cobro)


def ejecutarEjercicio2(): 
    parciales = leerParciales()
    calificacion_final = calcularFinal(parciales)
    estado = determinarEstado(calificacion_final)
    mostrarResultado(calificacion_final, estado)


def ejecutarEjercicio3(): 
    subtotal = leerSubtotal()
    descuento = calcularDescuento(subtotal)
    iva = calcularIVA(subtotal, descuento)
    total = calcularTotal(subtotal, descuento, iva)
    mostrarTicket(subtotal, descuento, iva, total)


def ejecutarEjercicio4(): 
    minutos = leerMinutos()
    cobro = calcularCobro(minutos)
    mostrarCobro(cobro)


def ejecutarEjercicio5(): 
    horas = leerHoras()
    renta = calcularRenta(horas)
    mostrarRenta(renta)


def ejecutarEjercicio6(): 
    edad = leerEdad()
    precio = calcularPrecio(edad)
    mostrarPrecio(precio)


def ejecutarEjercicio7(): 
    velocidad = leerVelocidad()
    multa = calcularMulta(velocidad)
    mostrarMulta(multa)


def mostrarMenu(): 
    print() 
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Recibo de luz") 
    print("2. Calificación final") 
    print("3. Total de compra") 
    print("4. Estacionamiento") 
    print("5. Renta de bicicletas") 
    print("6. Precio de boleto de cine")
    print("7. Multa por velocidad")
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
        elif opcion == "5": 
            ejecutarEjercicio5() 
        elif opcion == "6": 
            ejecutarEjercicio6() 
        elif opcion == "7": 
            ejecutarEjercicio7() 
        elif opcion != "0": 

            print("Opción no válida.")