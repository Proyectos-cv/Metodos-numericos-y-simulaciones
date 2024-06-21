import numpy as np
class hungaro:
    def iniciar(self):
        fil=int(input("numero de filas: "))
        col=int(input("numero de columnas: "))
        a=np.zeros((2+fil,2+col))
        for i in range (1):
            for j in range((col+2)):
                if j > 0 and j<col+1:
                    a[i][j]=j
        for i1 in range(fil+2):
            for j1 in range(1):
                if i1>0 and i1<fil+1:
                    a[i1][j1]=i1
        for s in range(fil + 2):
            for z in range(col + 2):
                if (z > 0 and z < col + 1) and (s > 0 and s < fil + 1):
                    y = float(input("datos de la tabla: "))
                    a[s][z] = y
        print "matriz inicial"
        print a
        for i2 in range(1,fil+1):
            aux = 1000
            aux=h.menorfila(col,i2,a,aux)
            a=h.restafila(col,aux,i2,a)
            a[i2][col + 1]=aux
        print"matriz con resta en filas de numero menor"
        print a

        for i3 in range(1,col+1):
            aux = 1000
            aux=h.menorcolumna(fil,i3,a,aux)
            a=h.restacolumna(fil,aux,i3,a)
            a[fil + 1][i3]=aux
        print"matriz con resta en columnas de numero menor"
        print a

        b = np.zeros((2 + fil, 2 + col))
        c = np.zeros((2 + fil, 2 + col))
        d=np.zeros((2 + fil, 2 + col))
        for r in range(fil + 2):
            for n in range(col + 2):
                b[r][n]=a[r][n]
                c[r][n] = a[r][n]
                d[r][n]=a[r][n]

#cubrir de lineas fila-columna
        contalin=0
        l=[]
        for m in range(1,fil + 1):
            conta=0
            #conta=h.lineasfil(col,m,fil,a,b,conta)
            #filas
            for o in range(1, col + 1):
                if b[m][o] == 0:
                    conta = conta + 1
            if conta >1 :
                for k in range(1,col + 1):
                    b[m][k] = -1
                l.append(m)
                contalin=contalin+1
        l1=[]
        for m1 in range(1,col+1):
            conta1=0
            # columnas
            for o1 in range(1, fil + 1):
                if b[o1][m1] == 0:
                    conta1 = conta1 + 1
            if conta1 >= 1:
                for k in range(1, fil + 1):
                    b[k][m1] = -1
                l1.append(m1)
                contalin=contalin+1

# cubrir de lineas columna-fila
        contalin1=0
        l2=[]
        for m in range(1,col + 1):
            conta=0
            #columnas
            for o in range(1, fil + 1):
                if c[o][m] == 0:
                    conta = conta + 1
            if conta >1 :
                for k in range(1,fil + 1):
                    c[k][m] = -1
                l2.append(m)
                contalin1=contalin1+1
        l3=[]
        for m1 in range(1,fil+1):
            conta1=0
            # filas
            for o1 in range(1, col + 1):
                if c[m1][o1] == 0:
                    conta1 = conta1 + 1
            if conta1 >= 1:
                for k1 in range(1, col + 1):
                    c[m1][k1] = -1
                l3.append(m1)
                contalin1=contalin1+1


        #encontar nuevo menor y restar o sumar
        if contalin<=contalin1 and contalin<col:
            ayu=10000
            for x in range(1,fil+1):
                for y in range(1,col+1):
                    if b[x][y]!=(-1) and b[x][y]<ayu:
                        ayu=b[x][y]
            for x1 in range(1,fil+1):
                for y1 in range(1,col+1):
                    if b[x1][y1]!=(-1):
                        a[x1][y1]=b[x1][y1]-ayu
                    for x2 in range(len(l)):
                        for y2 in range(len(l1)):
                            if x1==l[x2] and y1==l1[y2]:
                                a[x1][y1] = d[x1][y1] + ayu
            print"matriz con lineas"
            print b
            print"matriz final"
            print a
        elif contalin1<=contalin and contalin1<col:
            ayu = 10000
            for x in range(1, fil + 1):
                for y in range(1, col + 1):
                    if c[x][y] != (-1) and c[x][y] < ayu:
                        ayu = c[x][y]
            for x1 in range(1, fil + 1):
                for y1 in range(1, col + 1):
                    if c[x1][y1] != (-1):
                        a[x1][y1] = c[x1][y1] - ayu
                    for x2 in range(len(l3)):
                        for y2 in range(len(l2)):
                            if x1 == l3[x2] and y1 == l2[y2]:
                                a[x1][y1] = d[x1][y1] + ayu
            print"matriz con lineas"
            print c
            print"matriz final"
            print a
        elif contalin >= contalin1 and contalin >= col:
            print"numero de lineas igual a m"
        elif contalin1 >= contalin and contalin1 >= col:
            print"numero de lineas igual a m"

    def menorfila(self,col,i2,a,aux):
        for j1 in range(1,col+1):
            if (a[i2][j1]<aux):
                aux=a[i2][j1]
        return aux
    def restafila(self,col,aux,i2,a):
        for j1 in range(1, col+1):
            a[i2][j1]=(a[i2][j1])-aux
        return a
    def menorcolumna(self,fil,i3,a,aux):
        for j1 in range(1,fil+1):
            if (a[j1][i3]<aux):
                aux=a[j1][i3]
        return aux
    def restacolumna(self,fil,aux,i3,a):
        for j1 in range(1, fil+1):
            a[j1][i3]=(a[j1][i3])-aux
        return a
h=hungaro()
h.iniciar()