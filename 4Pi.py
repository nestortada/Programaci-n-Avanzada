#Mariana Olivares Goméz y Nestor Andres Tabares David#
#Cuarta tarea#

import random
x=0
sumatoria=0
pot=1
n=random.randint(10000,100000)
for rep in range(n):
    sub= (2*x+1)*(-1)**(pot+1)
    sumatoria= (1/sub)+sumatoria
    x=x+1
    pot=pot+1
pi=sumatoria*4
print(pi)