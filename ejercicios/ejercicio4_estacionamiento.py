

''' 
Ejercicio 4 (reto). Estacionamiento 
Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o fracción. 
El cobro máximo es de $150. El sistema recibe el tiempo de estancia en minutos y 
muestra el importe a cobrar. 
''' 
# PROBLEMA 
# Qué se calcula, en una oración. 
# Se calcula el importe a cobrar por el tiempo de estancia en el estacionamiento. 

# ENTRADAS 
# minutos : int, minutos, [0, ∞]

# SALIDAS 
# total : float, $, [0, 150], 2 decimales

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
# Se asumó que el cobro se redondea a 2 decimales.
# Se asumó que se cobra una hora completa por cualquier fracción de hora.
# Se asumó que el cobro máximo es de $150.

# ALGORITMO
# 1. Leer minutos
# 2. Si minutos <= 60:
#       resultado = 20
# 3. En caso contrario:
#       resultado = 20 + (ceil((minutos - 60) / 60) * 15)
# 4. Mostrar resultado

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# (45) -> (20.0)
# (60) -> (20.0)
# (61) -> (35.0)
# (150) -> (150.0)
# (600) -> (150.0)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerMinutos() -> int : lee los minutos de estancia.
# calcularCobro(minutos: int) -> float : calcula el cobro a aplicar.
# mostrarCobro(cobro: float) -> None : muestra el cobro a pagar.

# Implementa el algoritmo anterior utilizando las funciones del contrato.
def leerMinutos() -> int:
    minutos = int(input("Ingrese los minutos de estancia: "))
    return minutos

def calcularCobro(minutos: int) -> float:
    if minutos <= 60:
        return 20.0
    else:
        horas_adicionales = (minutos - 60 + 59) // 60
        return min(20 + horas_adicionales * 15, 150)

def mostrarCobro(cobro: float) -> None:
    print(f"El cobro a pagar es: ${cobro:.2f}") 


