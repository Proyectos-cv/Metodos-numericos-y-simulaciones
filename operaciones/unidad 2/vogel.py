import numpy as np
import random as r
class vogel:
    def inicio(self):
        fil=int(input("numero de filas: "))
        col=int(input("numero de columnas: "))
        a=np.zeros((1+fil,1+col))
        a1=np.zeros((1+fil,1+col))
        for i in range (fil):
            for j in range((col)):
                a[i][j]=r.randrange(1,100)
                #a[i][j]=int(input("inserta numero"))
        #filas
        for i2 in range(fil):
            aux=101
            aux2=0
            pos=-1
            aux2=p.calcula(aux, aux2, a,fil,col,i2,pos)
            pos = p.calcula1(aux, aux2, a, fil, col, i2,pos)
            aux=101
            aux=p.calcula(aux, aux2, a, fil, col,i2,pos)
            print aux
            print aux2
            if aux2>aux:
                q=aux2-aux
                a[i2][col]=q
            elif aux2<aux:
                q=aux-aux2
                a[i2][col]=q

            elif aux2==aux:
                q=aux2-aux
                a[i2][col]=0

        print a

        #columnas
        for i2 in range(col):
            aux=101
            aux2=0
            pos=-1
            aux2=p.calcula2(aux, aux2, a,fil,col,i2,pos)
            pos = p.calcula3(aux, aux2, a, fil, col, i2,pos)
            aux=101
            aux=p.calcula2(aux, aux2, a, fil, col,i2,pos)
            print aux
            print aux2
            if aux2>aux:
                q=aux2-aux
                a[fil][i2]=q
            elif aux2<aux:
                q=aux-aux2
                a[fil][i2]=q

            elif aux2==aux:
                q=aux2-aux
                a[fil][i2]=0

        print a


    def calcula(self,aux,aux2,a,fil,col,i2,pos):
        for j1 in range((col)):
            if (a[i2][j1]<aux and a[i2][j1]>aux2):
                aux=a[i2][j1]
            elif a[i2][j1]<aux and a[i2][j1]==aux2 and pos!=j1:
                aux = a[i2][j1]
        return aux

    def calcula1(self, aux, aux2, a, fil, col, i2,pos):
        for j1 in range((col)):
           # if (a[i2][j1] < aux and a[i2][j1] > aux2):
            #    aux = a[i2][j1]
             #   pos=j1
            if a[i2][j1] < aux and a[i2][j1] == aux2:
                aux = a[i2][j1]
                pos=j1
        return pos


    def calcula2(self,aux,aux2,a,fil,col,i2,pos):
        for j1 in range((fil)):
            if (a[j1][i2]<aux and a[j1][i2]>aux2):
                aux=a[j1][i2]
            elif a[j1][i2]<aux and a[j1][i2]==aux2 and pos!=j1:
                aux = a[j1][i2]
        return aux

    def calcula3(self, aux, aux2, a, fil, col, i2,pos):
        for j1 in range((fil)):
            if a[j1][i2] < aux and a[j1][i2] == aux2:
                aux = a[j1][i2]
                pos=j1
        return pos
p=vogel()
p.inicio()