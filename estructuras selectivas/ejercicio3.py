"""
Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante:  Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante.
-si el monto total de la compra excede de $500 000 la empresa tendra la capacidad de invertir de su propio dinero eun 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagara solicitando un credito al fabricante.
- Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. 
El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
Imprimir el valor invertido de su propio dinero, el valor prestado al banco, y el valor del crédito solicitado al fabricante, según sea el caso.
"""
montoTotal =float(input("ingrese el monto total de la compra:")) ## Agregar el monto total de la compra

##Se ingresan los datos del fabricante 
inversionPropia = 0 
prestamoBanco = 0
creditoFabricante = 0
intereses = 0
if montoTotal > 500000:
    inversionPropia = montoTotal * (55/100) 
    prestamoBanco = montoTotal * (30/100) 
    creditoFabricante = montoTotal * (15/100) 
else:
    inversionPropia = montoTotal * (70 / 100)   
    creditoFabricante = montoTotal * (30 / 100)  
intereses = creditoFabricante * (20 / 100)  
creditoFabricante += intereses

##Forma de imprimir 
print("Valor invertido de su propio dinero: $", inversionPropia)
print("Valor prestado al banco: $", prestamoBanco)
print("Valor del crédito solicitado al fabricante (incluyendo intereses): $", creditoFabricante)
