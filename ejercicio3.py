"""
Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante:  Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante.
-si el monto total de la compra excede de $500 000 la empresa tendra la capacidad de invertir de su propio dinero eun 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagara solicitando un credito al fabricante.
- Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. 
El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
Imprimir el valor invertido de su propio dinero, el valor prestado al banco, y el valor del crédito solicitado al fabricante, según sea el caso.
"""
monto_total =float(input("ingrese el monto total de la compra:"))
inversion_propia = 0
prestamo_banco = 0
credito_fabricante = 0
intereses = 0
if monto_total > 500000:
    inversion_propia = monto_total * (55/100)
    prestamo_banco = monto_total * (30/100)
    credito_fabricante = monto_total * (15/100)
else:
    inversion_propia = monto_total * (70 / 100)  # 70% de inversión propia
    credito_fabricante = monto_total * (30 / 100)  # 30% de crédito al fabricante
intereses = credito_fabricante * (20 / 100)  # 20% de intereses sobre el crédito
credito_fabricante += intereses
print("Valor invertido de su propio dinero: $", inversion_propia)
print("Valor prestado al banco: $", prestamo_banco)
print("Valor del crédito solicitado al fabricante (incluyendo intereses): $", credito_fabricante)
