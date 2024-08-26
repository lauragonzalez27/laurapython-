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
##Entrada de los datos del paciente 
edad = float(input("Ingresa la edad de la persona en años: "))
sexo = input("Ingresa el sexo de la persona (femenino/masculino): ").lower()
nivelHemoglobina = float(input("Ingresa el nivel de hemoglobina (g%): "))

##inicializar variables para los limites de 
limiteInferior = 0
limiteSuperior = 0

##Determinar el rango de hemoglobina 
if 0 <= edad <= 1/12: 
    limiteInferior = 13
    limiteSuperior = 26
elif 1/12 < edad <= 0.5:  
    limiteInferior = 10
    limiteSuperior = 18
elif 0.5 < edad <= 1:  
    limiteInferior = 11
    limiteSuperior = 15
elif 1 < edad <= 5:  
    limiteInferior = 11.5
    limiteSuperior = 15
elif 5 < edad <= 10:  
    limiteInferior = 12.6
    limiteSuperior = 15.5
elif 10 < edad <= 15:  
    limiteInferior = 13
    limiteSuperior = 15.5
elif edad > 15 and sexo == "femenino":  
    limiteInferior = 12
    limiteSuperior = 16
elif edad > 15 and sexo == "masculino":  
    limiteInferior = 14
    limiteSuperior = 18

##Determinar si la persona tiene anemia 
if nivelHemoglobina < limiteInferior:
    resultado = "positivo para anemia"
else:
    resultado = "negativo para anemia"

##Mostrar resultados
print("Edad:", edad, "años")
print("Sexo:", sexo)
print("Nivel de hemoglobina:", nivelHemoglobina, "g%")
print("Rango de hemoglobina adecuado:", limiteInferior, "-", limiteSuperior, "g%")
print("Resultado:", resultado)

