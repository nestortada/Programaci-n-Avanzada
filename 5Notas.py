#Mariana Olivares Goméz y Nestor Andres tabares David#
#Quinta tarea#

print("Notas")
suma = 0.0
print("Que cantidad de notas quiere: ")
c=int(input())
while c<=0 or c>20:
    print("Cantidad de notas invalida debe ser mayor a 0 y menor a 21 y tiene que ser entero, Qué cantidad de notas quieres ")
    c=int(input())
n = [0 for rep in range(c)]
for rep in range(c):
    print("Digite la nota #", rep+1)
    n[rep] = float(input())
    while n[rep] < 0.0 or n[rep] > 5.0:
        print("Nota invalida de la nota # ", rep+1, " porfavor digite una nota entre 0.0 a 5.0")
        n[rep] = float(input())
    suma = n[rep]+suma
promedio = suma/c
print("Las notas son  ", n)
print("El promedio de las notas son de  ", promedio)
print("La cantidad de notas sobre el promedio es de ", (c/promedio))
