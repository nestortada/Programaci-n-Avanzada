#Mariana Olivares Goméz y Nestor Andres tabares David#
#Primera tarea#

rep=2
bandera=10
numero=int(input('Ingrese un numero entero: '))
while numero<=0:
    numero=int(input("El valor no se puede debe ser un numero mayor a 0 y entero: "))
if(numero%2==0):
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')
if numero==1:
    print(f'El numero {numero} es primo')
else:
    while rep<numero:
        if numero%rep==0:
            bandera=1
        rep=rep+1
if bandera==1:
    print(f'El numero {numero} no es primo')
else:
    print(f'El numero {numero} es primo')
factorial=1
for i in range(1,numero+1):
    factorial*=i
print(f'El factorial de {numero} es: {factorial}')
if(numero%10000==0):
    print(f'El numero {numero} es multiplo de 10000')
else:
    print(f'El numero {numero} no es multiplo de 10000')
a=0
for x in range(1,numero+1):
    if (numero % x) == 0 :
        print(f'-Los divisores de {numero} son {x}')
        a+=1