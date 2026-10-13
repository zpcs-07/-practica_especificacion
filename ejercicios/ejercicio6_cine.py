

''' 
Ejercicio 6. Boleto de cine 
Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos de 60 años o más pagan la mitad. 
Se necesita mostrar el precio del boleto según la edad. 
''' 
# PROBLEMA  
# Se calcula el precio del boleto de cine según la edad del espectador.

# ENTRADAS 
# edad : int, años, [0, ∞]

# SALIDAS 
# precio : float, $, [0, ∞], 2 decimales

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
 
# ALGORITMO 
# 1. Leer edad
# 2. Si edad <= 12 o edad >= 60: 
#       resultado = 80 * 0.5
# 3. En caso contrario:
#       resultado = 80
# 4. Mostrar precio

# CASOS DE PRUEBA 
# entrada(s) -> salida esperada 
# (8) -> (40.0)
# (12) -> (40.0)
# (13) -> (80.0)
# (59) -> (80.0)
# (60) -> (40.0)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerEdad() -> int : lee la edad del espectador.
# calcularPrecio(edad: int) -> float : calcula el precio del boleto.
# mostrarPrecio(precio: float) -> None : muestra el precio del boleto.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerEdad() -> int:
    edad = int(input("Ingrese la edad del espectador: "))
    return edad

def calcularPrecio(edad: int) -> float:
    if edad <= 12 or edad >= 60:
        return 80 * 0.5
    else:
        return 80

def mostrarPrecio(precio: float) -> None:
    print(f"Precio del boleto: ${precio:.2f}")
