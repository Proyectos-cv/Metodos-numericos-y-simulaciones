import numpy as np
import simplex1
rest=int(input("numero de restricciones: "))
a=np.zeros((1+rest,3+(rest+1)))
a[0][0]=1
for i in range (1+rest):
    for j in range(3+(rest+1)):
        if a[i][1]==0:
            x1=float(input("datos de x1: "))
            a[i][1]=x1
for i1 in range(1 + rest):
    for j1 in range(3 + (rest)):
        if a[i1][2]==0:
            x1=float(input("datos de x2: "))
            a[i1][2]=x1
for i2 in range((1 + rest)):
    for j2 in range(3 + (rest)):
         if a[i2][(3+rest)]==0:
            x1=float(input("datos de las constantes: "))
            a[i2][3+(rest)]= x1
for i3 in range(1,(1 + rest)):
    for j3 in range(3,(3 + (rest))):
        if i3+2==j3:
            a[i3][j3]=1
a[0][3+rest]=0
print a

if a[0][1]>a[0][2]:
    simplex1.variable2(a, rest)
elif a[0][1]<a[0][2]:
    simplex1.variable1(a, rest)