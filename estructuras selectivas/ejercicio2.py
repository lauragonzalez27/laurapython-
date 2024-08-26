"""
Calcular el total a pagar por la compra de zapatillas. Si se compran tres o más zapatillas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar una vez aplicado el descuento.
"""
numeroZapatilla=int (input("digite la cantidad de zapatillas:")) ##Agregar la cantidad de zapatillas 
valorCompra=int (input("digite el valor total de la compra:")) ##Agregar el valor total de la compra 
if numeroZapatilla >=3 : ##El resultado del numero de zapatillas tiene que se mayor que 3 
    descuento1= valorCompra * (20 / 100) ##El descuento 1 tiene un porcientaje del 20 de descuento 
    valorFinal= valorCompra - descuento1
    print(f"el valor de la compra es : ${valorCompra} con el descuento de 20% es: ${descuento1} el valor total a pagar es: $ {valorFinal}")
elif numeroZapatilla < 3 :
    descuento2= valorCompra * (10 / 100)##El decuento 2 tiene un porcientaje del 10 de descuento 
    valorfinal1= valorCompra - descuento2
    print(f"el valor de la compra es : ${valorCompra} con el descuento de 10% es: ${descuento2} el valor total a pagar es: $ {valorfinal1}")



