"""
calcular el numero de pulsaciones que debe de tener unna persona por cada 10 segundos de ejercicio aerobico;la formula que se aplica es:
-cuando el sexo es femenino : num.pulsaciones = (220-edad)/10
-y si el sexo es masculino : num.pulsaciones = (210 -edad)/10
"""

edad = int(input("Ingresa la edad de la persona: "))


sexo = input("Ingresa el sexo de la persona (femenino/masculino): ").lower()


pulsaciones = 0


if sexo == "femenino":
    pulsaciones = (220 - edad) / 10  
elif sexo == "masculino":
    pulsaciones = (210 - edad) / 10  

print("Número de pulsaciones por cada 10 segundos de ejercicio:", pulsaciones)
