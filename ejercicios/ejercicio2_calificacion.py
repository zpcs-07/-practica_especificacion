
''' 
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó. 
''' 
# PROBLEMA 
# La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se necesita mostrar la calificación final y si el alumno aprobó.

# ENTRADAS 
# parcial1 : float, %, [0, 100]
# parcial2 : float, %, [0, 100]
# parcial3 : float, %, [0, 100]


# SALIDAS 
# calificacion_final : float, %, [0, 100], 2 decimales
# estado : str, -, "Aprobado" o "Reprobado"

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
# Se asumó que la calificación final se redondea a 2 decimales


# ALGORITMO 
# 1. Leer parciales
# 2. Si algún parcial < 50: 
#       resultado = "Reprobado"
# 3. En caso contrario: 
#       resultado = (parcial1 * 0.3) + (parcial2 * 0.3) + (parcial3 * 0.4)
# 4. Mostrar resultado

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# (80, 70, 90) -> (80 * 0.3) + (70 * 0.3) + (90 * 0.4) = 82.0
# (70, 70, 70) -> (70 * 0.3) + (70 * 0.3) + (70 * 0.4) = 70.0
# (100, 100, 40) -> "Reprobado"
# (69, 70, 70) -> "Reprobado"

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# def leerParciales() -> tuple[float, float, float] : lee las calificaciones de los tres parciales.
# def calcularFinal(parciales: tuple[float, float, float]) -> float | str : calcula la calificación final.
# def determinarEstado(calificacion_final: float | str) -> str : determina el estado del alumno.
# def mostrarResultado(calificacion_final: float | str, estado: str) -> None : muestra el resultado final.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerParciales() -> tuple[float, float, float]:
    parcial1 = float(input("Ingrese la calificación del primer parcial: "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
    return (parcial1, parcial2, parcial3)

def calcularFinal(parciales: tuple[float, float, float]) -> float | str:
    parcial1, parcial2, parcial3 = parciales
    if parcial1 < 50 or parcial2 < 50 or parcial3 < 50:
        return "Reprobado"
    else:
        calificacion_final = (parcial1 * 0.3) + (parcial2 * 0.3) + (parcial3 * 0.4)
        return round(calificacion_final, 2)

def determinarEstado(calificacion_final: float | str) -> str:
    if calificacion_final == "Reprobado":
        return "Reprobado"
    elif calificacion_final >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

def mostrarResultado(calificacion_final: float | str, estado: str) -> None: 
    if calificacion_final == "Reprobado":
        print(f"Calificación final: {calificacion_final}, Estado: {estado}")
    else:
        print(f"Calificación final: {calificacion_final:.2f}, Estado: {estado}")

        # Fin del programa

