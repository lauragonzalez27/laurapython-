"""
determinar  si un aprendiz aprueba o desaprueba algoritmia, sabiendo que aprobara si su promedio de tres 
calificaciones es mayo o igual a 70; reprueba en caso contrario
"""
nombre=(input("ingrese el nombre del aprendiz")) ##Ingrese el nombre del aprendiz 
nota1=float(input("ingrese la primer nota")) ##Ingrese la nota 1 
nota2=float(input("ingrese la segunda nota")) ##Ingrese la nota 2 
nota3=float(input("ingrese la tercera nota")) ##Ingrese la nota 3
promedio=(nota1+nota2+nota3)/3 ##Se suman las tres notas, y se dividen por el numero de notas 
if promedio >=70 : ##El resultado del promedio debe ser mayor que 70 para aprobar 
    print("aprueba")
else:
    print("desaprueba") ##Si el resultado del promedio es menor, desaprueba
     


                     

