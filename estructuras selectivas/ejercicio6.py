"""
se ha establecido un programa para estomula a los alumnos, el cual consiste en lo siguiente:
si el promedio obtenido por un alumno en el ultimo periodo es mayor que 4.0, se le hara un descuento del 30% sobre la pension; si el promedio obtenido es mayor que 4.0, se le hara pagar la pension completa, la cual incluye el 105 de IVA. obtener cuanto debe pagar un alumno.
"""
##Entrada del promedio obtenido por el alumno 
promedio = float(input("Ingresa el promedio del alumno: "))

##Entrada del costo de la pension 
pension = float(input("Ingresa el costo de la pensión: "))

##Inicializar variables 
descuento = 0
iva = 0
total_a_pagar = 0

##verificar el promedio y calcular el descuento 
if promedio >= 4.0:
    descuento = pension * (30 / 100) 
    totalaPagar = pension - descuento
else:
    iva = pension * (10 / 100) 
    totalaPagar = pension + iva

##Mostrar resultados
print("Promedio del alumno:", promedio)
print("Descuento aplicado: $", descuento)
print("IVA aplicado: $", iva)
print("Total a pagar: $", totalaPagar)