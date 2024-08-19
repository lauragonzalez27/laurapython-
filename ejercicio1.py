"""
determinar  si un aprendiz aprueba o desaprueba algoritmia, sabiendo que aprobara si su promedio de tres 
calificaciones es mayo o igual a 70; reprueba en caso contrario
"""
nombre=(input("ingrese el nombre del aprendiz"))
nota1=float(input("ingrese la primer nota"))
nota2=float(input("ingrese la segunda nota"))
nota3=float(input("ingrese la tercera nota"))
promedio=(nota1+nota2+nota3)/3
if promedio >=70 :
    print("aprueba")
else:
    print("desaprueba")
     


                     

