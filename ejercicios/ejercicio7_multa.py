

''' 
Ejercicio 7. Multa por velocidad 
En una avenida el límite es de 60 km/h. Si se excede hasta por 20 km/h, la multa es de $500. Si se excede 
por más de 20 km/h, la multa es de $1,000. Se necesita mostrar la multa a partir de la velocidad del 
vehículo. 
''' 
# PROBLEMA 
# Se calcula la multa por exceso de velocidad. 

# ENTRADAS
# velocidad : float, km/h, [0, ∞]

# SALIDAS
# multa : float, $, [0, ∞], 2 decimales

# REGLAS Y SUPUESTOS
# - Valores fijos del problema (tarifas, porcentajes, topes).
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
#   Se asumió que la multa se calcula sobre el exceso de velocidad.
 
# ALGORITMO 
# 1. Leer velocidad
# 2. Si velocidad <= 60: 
#       resultado = 0
# 3. En caso contrario: 
#       resultado = 500 si velocidad <= 80
#       resultado = 1000 si velocidad > 80
# 4. Mostrar multa

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# (50) -> (0)
# (60) -> (0)
# (61) -> (1000)
# (80) -> (500)
# (81) -> (1000)

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerVelocidad() -> float : lee la velocidad del vehículo.
# calcularMulta(velocidad: float) -> float : calcula la multa por exceso de velocidad.
# mostrarMulta(multa: float) -> None : muestra la multa.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerVelocidad() -> float:
    velocidad = float(input("Ingrese la velocidad del vehículo: "))
    return velocidad

def calcularMulta(velocidad: float) -> float:
    if velocidad <= 60:
        return 0.0
    elif velocidad <= 80:
        return 500.0
    else:
        return 1000.0

def mostrarMulta(multa: float) -> None:
    print(f"Multa: ${multa:.2f}")

