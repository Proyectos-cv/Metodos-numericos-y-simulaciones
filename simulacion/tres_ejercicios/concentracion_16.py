from random import *
import numpy
class toxicidad:
    def concentracion(self):
        limite=float(input("numero de iteraciones: "))
        x=0
        toxico=0.0
        suma=0.0
        unico=0.0
        total=0.0
        l=[]
        while x<limite:
            r = randint(0, 20)
            if r>=8:
                suma=suma+1.0
                total = total + r
                if r == 10:
                    unico=unico+1.0
            else:
                total=total+r
            l.append(r)
            x=x+1
        print ("probabilidad de tomar muestra toxica: ",suma/limite)
        print ("media: ",total/limite)
        print("varianza: ", numpy.var(l))
        print("probabilidad de concentracion de 10M: ",unico/limite)
    def concentracion1(self):
        l=numpy.array([50,51,52,53,52,50,51,50])
        x=numpy.var(l)
        print (x)
t=toxicidad()
t.concentracion()