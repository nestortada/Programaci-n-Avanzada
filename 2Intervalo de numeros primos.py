#Mariana Olivares  Goméz y Nestor Andres tabares David#
#Segunda tarea#

conti=0
contf=0
acum=[]
m=""
a=int(input("Ingrese un extremo: "))
while a<0:
    a=int(input("El valor debe ser mayor a cero, Ingrese un extremo: "))
b=int(input("Ingrese el otro extremo: "))
while b<a:
    b=int(input("El valor que ingreso debe ser mayor a "+ str(a) + " Ingrese el otro extremo: "))
for c in range (a,b+1,1):
    for i in range (1,c+1,1):
        if(c%i==0):
            conti=conti+1
    if (conti==2):
        acum=acum+[c]
        contf=contf+1
    conti=0
print("Cantidad de primos: ",contf)
print("Números primos: ",acum)