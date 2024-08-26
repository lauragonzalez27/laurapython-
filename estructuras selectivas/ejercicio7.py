"""
en una llantera se ha establecido una promocion de las llantas marcas "todo terreno", dicha promocion consiste en lo siguiente.
-si se compran menos de cinco llantas el precio es de $300 000 cada una, de %250 000 si se compran de cinco a 10 y de %200 000 si se compran mas de 10.
obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compre.
"""
##Entrada de la cantidad de llantas a comprar 
cantidadLlantas = int(input("Ingresa la cantidad de llantas que vas a comprar: "))

##Inicializar variables 
precioporllanta = 0

##Verificar la cantidad de llantas y determinar el precio por llanta 
if cantidadLlantas < 5:
    precioporllanta = 300000  
elif 5 <= cantidadLlantas <= 10:
    precioporllanta = 250000  
else:
    precioporllanta = 200000  

##Calcular el costo total
costoTotal = cantidadLlantas * precioporllanta

#Mostrar resultados 
print("Cantidad de llantas compradas:", cantidadLlantas)
print("Precio por llanta: $", precioporllanta)
print("Costo total a pagar: $", costoTotal)