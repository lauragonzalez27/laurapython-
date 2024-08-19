"""
 En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un color que se escoge al azar. Si el color de la balota es rojo el descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si el color es diferente a los indicados no obtendrá descuento. Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar.
"""

monto_total = float(input("Ingresa el monto total de la compra: "))
color_balota = input("Ingresa el color de la balota (rojo, verde, otro): ").lower()
descuento = 0

if color_balota == "rojo":
    descuento = monto_total * (15 / 100)  
elif color_balota == "verde":
    descuento = monto_total * (20 / 100) 
else:
    descuento = 0  

valor_a_pagar = monto_total - descuento
print("Valor de la compra: $", monto_total)
print("Color de la balota:", color_balota)
print("Descuento aplicado: $", descuento)
print("Valor a pagar: $", valor_a_pagar)





                       
