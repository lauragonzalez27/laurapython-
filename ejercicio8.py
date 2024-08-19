"""
tomando como base los resultados obtenidos en un laboratorio de analisis clinicos, un medico determina si una persona tiene anemia o no, lo cual depende de su nivel de emoglobina en la sangre, de su edad y sexo. si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como negativo. la tabla en la que el medico se basa para obtener el resultado es la siguiente:
edad nivel hemoglobina 
0-1 mes         13-26g%
>1y<= 6 meses   10-18g%
>6y<=12 meses   11-15g%
>1y<=5 años     11.5-15g%
5y<=10 años     13-14.5g%
>10y<=15 años   12-16g%
mujeres>15años  12-16g%
hombres>15años  14-18g%
"""

edad = float(input("Ingresa la edad de la persona en años: "))
sexo = input("Ingresa el sexo de la persona (femenino/masculino): ").lower()
nivel_hemoglobina = float(input("Ingresa el nivel de hemoglobina (g%): "))


limite_inferior = 0
limite_superior = 0


if 0 <= edad <= 1/12: 
    limite_inferior = 13
    limite_superior = 26
elif 1/12 < edad <= 0.5:  
    limite_inferior = 10
    limite_superior = 18
elif 0.5 < edad <= 1:  
    limite_inferior = 11
    limite_superior = 15
elif 1 < edad <= 5:  
    limite_inferior = 11.5
    limite_superior = 15
elif 5 < edad <= 10:  
    limite_inferior = 12.6
    limite_superior = 15.5
elif 10 < edad <= 15:  
    limite_inferior = 13
    limite_superior = 15.5
elif edad > 15 and sexo == "femenino":  
    limite_inferior = 12
    limite_superior = 16
elif edad > 15 and sexo == "masculino":  
    limite_inferior = 14
    limite_superior = 18

if nivel_hemoglobina < limite_inferior:
    resultado = "positivo para anemia"
else:
    resultado = "negativo para anemia"

# Mostrar resultados
print("Edad:", edad, "años")
print("Sexo:", sexo)
print("Nivel de hemoglobina:", nivel_hemoglobina, "g%")
print("Rango de hemoglobina adecuado:", limite_inferior, "-", limite_superior, "g%")
print("Resultado:", resultado)

