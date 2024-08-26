"""
 En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un color que se escoge al azar. Si el color de la balota es rojo el descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si el color es diferente a los indicados no obtendrá descuento. Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar.
"""
##Entrada del monto total de la compra 
montoTotal = float(input("Ingresa el monto total de la compra: "))

##Entrada del color de la balota 
colorBalota = input("Ingresa el color de la balota (rojo, verde, otro): ").lower()

##Inicializar variable 
descuento = 0

 ##Verificar el color de la balota y calcular el descuento 
if colorBalota == "rojo":
    descuento = montoTotal * (15 / 100) ##15% de descuento si la balota es roja 
elif colorBalota == "verde":
    descuento = montoTotal * (20 / 100) ##20% de descuento si la balota es verde 

else:
    descuento = 0  ##Sin descuento si el color es diferente 

##Calcular el valor a pagar 
valoraPagar = montoTotal - descuento
##Mostrar resultados 
print("Valor de la compra: $", montoTotal)
print("Color de la balota:", colorBalota)
print("Descuento aplicado: $", descuento)
print("Valor a pagar: $", valoraPagar)





                       
