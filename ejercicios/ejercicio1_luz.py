''' 
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes. 
''' 
# PROBLEMA 
# Qué se calcula, Se necesita calcular el importe del recibo a partir del consumo del mes.  . 
 
# ENTRADAS 
# costo_hora : tipo, unidad, rango válido. 
#costo_hora : float, kWh, [0, ∞)
#consumo : float, kWh, [0, ∞)
 
# SALIDAS 
#importe : float, $US, [0, ∞), 2 decimales

 
# REGLAS Y SUPUESTOS 
#Tarifas:
# - $1.00 por kWh hasta 150 kWh.
# - $1.50 por kWh de 151 a 280 kWh.
# - $3.00 por kWh arriba de 280 kWh.
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 
# Se asumió que el costo por kWh es constante y no varía con el tiempo.
# Se asumió que el consumo se mide en kWh y es un valor positivo.
# Se asumió que el importe se redondea a 2 decimales.
# Se asumió que el consumo no puede ser negativo.
 
# ALGORITMO 
# 1. Leer consumo
# 2. Si consumo <= 150: 
#       resultado = consumo * 1.00
# 3. En caso contrario: 
#       resultado = (150 * 1.00) + ((consumo - 150) * 1.50) si consumo <= 280
#       resultado = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00) si consumo > 280
# 4. Mostrar resultado

# CASOS DE PRUEBA
#100 kWh -> $100.00
#150 kWh -> $150.00
#200 kWh -> $225.00
#280 kWh -> $330.00
#300 kWh -> $390.00

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden.  
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# nombreFuncion(parametro1, parametro2) -> valor_retorno : qué hace. 
#leerConsumo() -> float : lee el consumo del mes en kWh.
#calcularPago(consumo: float) -> float : calcula el importe del recibo según las tarifas.
#mostrarRecibo(importe: float) -> None : muestra el importe del recibo con 2 decimales.
 
# Implementa el algoritmo anterior utilizando las funciones del contrato.

