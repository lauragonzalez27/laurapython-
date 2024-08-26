"""
calcular el numero de pulsaciones que debe de tener unna persona por cada 10 segundos de ejercicio aerobico;la formula que se aplica es:
-cuando el sexo es femenino : num.pulsaciones = (220-edad)/10
-y si el sexo es masculino : num.pulsaciones = (210 -edad)/10
"""
##Entrada de la edad 
edad = int(input("Ingresa la edad de la persona: "))

##Entrada del sexo 
sexo = input("Ingresa el sexo de la persona (femenino/masculino): ").lower()

##Inicializar variables para pulsaciones 
pulsaciones = 0

##Calcular pulsaciones segun el sexo 
if sexo == "femenino":
    pulsaciones = (220 - edad) / 10  
elif sexo == "masculino":
    pulsaciones = (210 - edad) / 10  

##Mostrar resultados 
print("Número de pulsaciones por cada 10 segundos de ejercicio:", pulsaciones)
