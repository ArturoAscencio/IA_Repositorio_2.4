# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Funci�n para calcular el valor de la informaci�n
def valor_de_informacion(valor_con_informacion, valor_sin_informacion):
    return valor_sin_informacion - valor_con_informacion

# Valor sin informaci�n adicional
valor_sin_informacion = 100

# Valor con informaci�n adicional
valor_con_informacion = 120

# Calcular el valor de la informaci�n
valor_info = valor_de_informacion(valor_con_informacion, valor_sin_informacion)

# Imprimir el resultado
print(f"El valor de la informaci�n es: {valor_info}")
