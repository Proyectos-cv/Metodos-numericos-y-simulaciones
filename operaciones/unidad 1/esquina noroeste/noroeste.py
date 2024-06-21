import numpy as np

fil=int(input("numero de filas: "))
col=int(input("numero de columnas: "))
a=np.zeros((2+fil,2+col))
a1=np.zeros((2+fil,2+col))
for i in range (1):
    for j in range((col+2)):
        if j > 0 and j<col+1:
            #x=float(input("datos de fila: "))
            #a[i][j]=x
            a[i][j]=j
for i1 in range(fil+2):
    for j1 in range(1):
        if i1>0 and i1<fil+1:
            #x1=float(input("datos de columna: "))
            #a[i1][j1]=x1
            a[i1][j1]=i1
for s in range(fil + 2):
    for z in range(col+2):
        if (s > 0 and s<fil+1)and z==col+1:
            y = float(input("datos de oferta: "))
            a[s][z] = y
for s in range(fil + 2):
    for z in range(col + 2):
        if (z > 0 and z < col + 1) and s == fil + 1:
            y = float(input("datos de demanda: "))
            a[s][z] = y
for o in range(fil + 1):
    for p in range(col + 1):
        if (p>0 and p< col + 1) and (o>0 and o< fil + 1):
            a1[o][p]=float(input("datos de la tabla: "))
print""
print"matriz de oferta y demanda"
print a
b=np.zeros((2+fil,2+col))
c=np.zeros((2+fil,2+col))

for s in range(1,fil + 1):
    for z in range(1,col + 1):
        if (z > 0 and z < col + 1) and (s > 0 and s < col + 1) and a[fil + 1][z]!=0:
            if a[fil + 1][z]<=a[s][col+1]:

                b[s][z]=a[fil+1][z]
                c[s][z] = 1

                q=a[s][col + 1]
                p= a[fil + 1][z]
                t=q-p

                a[s][col+1]=t
                a[fil+1][z]=0
            elif a[fil + 1][z] > a[s][col + 1] and a[s][col+1]!=0:
                b[s][z] = a[s][col+1]
                c[s][z] = 1

                q = a[s][col + 1]
                p = a[fil + 1][z]
                t = p-q

                a[fil + 1][z] = t
                a[s][col+1] = 0
                a[s][z] = a[s][z - 1]

            elif a[fil + 1][z] > a[s][col + 1] or a[s][col+1]==0:
                a[s][z]=a[s+1][z-1]

s=0
for c1 in range(fil+1):
    for c2 in range(col+1):
        if c[c1][c2]==1:
            s=s+(a1[c1][c2]*b[c1][c2])
print""
print "valor: ",s


u=[]
pu=[]
v=[]
pv=[]
u.append(0)
pu.append(1)

for o in range(fil + 1):
    for p in range(col + 1):
        if c[o][p] == 1:
            #for ru in range( len(pu)):
            if pu[len(pu)-1] == o:
                v.append(a1[o][p] - u[len(pu)-1])
                pv.append(p)
            elif pv[len(pv)-1] == p:
                u.append(a1[o][p]-v[len(pv)-1])
                pu.append(o)
            elif pu[len(pu)-1]!= o and pv[len(pv)-1]!= p:
                u.append(0)
                pu.append(o)
                v.append(a1[o][p] - u[len(pu)-1])
                pv.append(p)
aux=0
h=0
z=0
z1=0
k=[]
for d in range(1,fil+1):
    for d1 in range(1,col+1):
        if c[d][d1]==0 and d < fil+1 and d1 < col+1:
            h=(u[d-1])+(v[d1-1])-(a1[d][d1])
            k.append(h)
            print "u ",d," + v ",d1," - ",a1[d][d1]," = ",h
            if h>aux:
                z=d
                z1=d1
                aux=h
print "variable que entra= ",aux," posicion: ",z," , ",z1
#print k

for x in range(len (u)):
    print "u ",x+1," = ",u[x]
print""
for x1 in range(len (v)):
    print "v ",x1+1," = ",v[x1]
#print u
#print pu
#print v
#print pv
print""
print"matriz de datos de cada celda"
print a1
print""
print"matriz de recorrido"
print b
print""
print"matriz auxiliar de recorrido"
print c
print""
