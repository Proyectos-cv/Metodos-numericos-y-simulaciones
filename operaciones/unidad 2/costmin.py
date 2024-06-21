import numpy as np
fil=int(input("numero de filas: "))
col=int(input("numero de columnas: "))
a=np.zeros((2+fil,2+col))
a1=np.zeros((2+fil,2+col))
for i in range (1):
    for j in range((col+2)):
        if j > 0 and j<col+1:
            a[i][j]=j
for i1 in range(fil+2):
    for j1 in range(1):
        if i1>0 and i1<fil+1:
            a[i1][j1]=i1
for s in range(fil + 2):
    for z in range(col+2):
        if (s > 0 and s<fil+1)and z==col+1:
            y = float(input("datos de oferta: "))
            a[s][z] = y
for s1 in range(fil + 2):
    for z1 in range(col + 2):
        if (z1 > 0 and z1 < col + 1) and s1 == fil + 1:
            y = float(input("datos de demanda: "))
            a[s1][z1] = y
for s2 in range(fil + 2):
    for z2 in range(col + 2):
        if (z2 > 0 and z2 < col + 1) and (s2 > 0 and s2 < fil + 1):
            y = float(input("datos de la tabla: "))
            a[s2][z2] = y
print "matriz inicial"
print a
band=True
while band==True:
    aux=1000
    fila=1
    columna=1
    for r in range(1,fil+1):
        for k in range (1,col+1):
            if a[r][k]<aux and a[r][k]!= -1:
                aux = a[r][k]
                fila=r
                columna=k
    if a[fila][col+1]>a[fil+1][columna] and a[fila][columna]!=-1:
        p=a[fila][col + 1]-a[fil+1][columna]
        a1[fila][columna]=a[fil + 1][columna]
        a[fil + 1][columna]=0
        a[fila][col + 1]=p
        a[fila][columna]=a[fil+1][columna]
        for i in range(1,fil+1):
            a[i][columna]=-1
    elif a[fila][col + 1] < a[fil + 1][columna] and a[fila][columna]!=-1:
        p =  a[fil + 1][columna]-a[fila][col + 1]
        a[fil + 1][columna] = p
        a1[fila][columna] = a[fila][col+1]
        a[fila][col + 1] = 0
        for i in range(1,col+1):
            a[fila][i]=-1
        #a[fil + 1][columna]=a[fila][columna]
    elif a[fila][col + 1] == a[fil + 1][columna] and a[fila][columna]!=-1:
        a1[fila][columna] = a[fil + 1][columna]
        a[fila][col + 1] = 0
        a[fil + 1][columna] = 0
        for i in range(1,fil+1):
            a[i][columna]=-1
        for j in range(1, col + 1):
            a[fila][j] = -1
    else:
        band=False

print "matriz despues del proceso"
print a
print "matriz de asignaciones"
print a1
