import random as r
import numpy as n
class familia:
    def sigue(self):
        vez=float(input("veces de iteracion: "))
        x=0
        contador=0.0
        contado = 0.0
        while x<vez:
            contador=f.prob(contador)
            x=x+1
        prob=contador/vez
        print contador
        print prob
    def prob(self,contador):
        fam=n.zeros(5)
        for i in range(5):
            ale=r.randrange(1,3)
            fam[i]=ale
        #print fam
        contah=0
        contam=0
        for j in range(5):
            if fam[j]==1:
                contam=contam+1
            elif fam[j]==2:
                contah=contah+1
        if contah==3 and contam==2:
            contador=contador+1
        return contador

f=familia()
#f.prob()
f.sigue()