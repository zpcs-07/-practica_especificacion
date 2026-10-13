Ejercicio 5. Renta de bicicletas 
Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más, se aplica un 15% de descuento. Se 
necesita mostrar el importe a pagar según las horas de renta. 
• Archivo: ejercicios/ejercicio5_renta.py 
• Funciones: leerHoras, calcularRenta, mostrarRenta 
• Entradas de prueba: 1, 2, 3 y 4 horas

''' 
Enunciado del problema, tal como lo entregó el cliente. 
''' 
# PROBLEMA 
# Se calcula el importe a pagar por la renta de bicicletas. 
 
# ENTRADAS 
# horas : int, horas, [1, ∞] 

# SALIDAS 
# total : float, $, [0, ∞], 2 decimales

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
#   Se asumió que el descuento se aplica sobre el total a pagar.
 
# ALGORITMO 
# 1. Leer horas
# 2. Si horas < 3: 
#       resultado = horas * 30
# 3. En caso contrario: 
#       resultado = horas * 30 * 0.85
# 4. Mostrar total

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# (1) -> (30.00)
# (2) -> (60.00)
# (3) -> (76.50)
# (4) -> (102.00)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.    

# CONTRATO DE FUNCIONES
# leerHoras() -> int : lee las horas de renta.
# calcularRenta(horas: int) -> float : calcula el importe a pagar por la renta.
# mostrarRenta(total: float) -> None : muestra el total a pagar.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerHoras() -> int:
    horas = int(input("Ingrese las horas de renta: "))
    return horas

def calcularRenta(horas: int) -> float:
    if horas < 3:
        return horas * 30
    else:
        return horas * 30 * 0.85

def mostrarRenta(total: float) -> None:
    print(f"Total a pagar: ${total:.2f}")
    