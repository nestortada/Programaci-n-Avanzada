#Mariana Olivares Goméz y Nestor Andres tabares David#
#Tercera tarea#

promedio=0
ptotal=0
p=[[0 for rep in range(3)]for i in range(5)]
for rep in range(5):
    print("encuesta del servicio del trasporte")
    print("responda la encuesta del 0-10 (0= totalmente en desacuerdo y 10= totalmente de acuerdo)")
    print("responda la persona # ",rep+1)
    print("1. ¿Cree usted que la ruta llega a tiempo?")
    print("2. ¿Cree usted que la ruta esta limpia?")
    print("3. ¿cree usted que la ruta tiene suficientes paradas? ")
    for i in range(3):
        p[rep][i]=int(input())
        while p[rep][i]<0 or p[rep][i]>10:
            print("la respuesta es invalida digite del 0 hasta el 10 y esta en la pregunta ",i+1)
            p[rep][i]=int(input())
for rep in range(5):
    if rep>0:
        print("el promedio de respuestas de la persona # ", rep, "ess igual ",(ptotal/3))
    ptotal=0
    for i in range(3):
        ptotal=ptotal+p[rep][i]
        promedio=promedio+p[rep][i]
print("el promedio de respuesta de la persona # 5 es igual ",(ptotal/3))
print("el promedio del servicio en general es de ",(promedio/15))



