
''' 
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de 
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket con 
subtotal, descuento, IVA y total. 
''' 
# PROBLEMA 
# Se calcula el ticket de compra con subtotal, descuento, IVA y total. 
 
# ENTRADAS 
# subtotal : float, $, [0, ∞]
# descuento : float, $, [0, ∞]
# IVA : float, $, [0, ∞]

# SALIDAS
# total : float, $, [0, ∞], 2 decimales

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
# - Se asumió que el subtotal es un valor positivo.
# - Se asumió que el descuento se calcula antes de aplicar el IVA.
# - Se asumió que el IVA se calcula sobre el subtotal menos el descuento.
# - Se asumió que el total se redondea a 2 decimales.

# ALGORITMO
# 1. Leer subtotal
# 2. Si subtotal >= 5000: 
#       resultado = subtotal * 0.8
# 3. En caso contrario: 
#       resultado = subtotal * 0.9
# 4. Mostrar ...

# CASOS DE PRUEBA
# entrada(s) -> salida esperada
# (500) -> (80.0, 12.8, 92.8)
# (900) -> (810.0, 129.6, 939.6)
# (1000) -> (900.0, 144.0, 1044.0)
# (5000) -> (4000.0, 640.0, 4640.0)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 

# CONTRATO DE FUNCIONES
# leerSubtotal() -> float : lee el subtotal de la compra.
# calcularDescuento(subtotal: float) -> float : calcula el descuento a aplicar.
# calcularIVA(subtotal: float, descuento: float) -> float : calcula el IVA a aplicar.
# calcularTotal(subtotal: float, descuento: float, iva: float) -> float : calcula el total a pagar.
# mostrarTicket(subtotal: float, descuento: float, iva: float, total: float) -> None : muestra el ticket de compra.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerSubtotal() -> float:
    subtotal = float(input("Ingrese el subtotal de la compra: "))
    return subtotal

def calcularDescuento(subtotal: float) -> float:
    if subtotal >= 5000:
        return subtotal * 0.2
    elif subtotal >= 1000:
        return subtotal * 0.1
    return 0

def calcularIVA(subtotal: float, descuento: float) -> float:
    return (subtotal - descuento) * 0.16

def calcularTotal(subtotal: float, descuento: float, iva: float) -> float:
    return round(subtotal - descuento + iva, 2)

def mostrarTicket(subtotal: float, descuento: float, iva: float, total: float) -> None:
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")
