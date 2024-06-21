from random import *
import numpy
class periodicos:
    def probabilidad(self):
        limite=float(input("numero de iteraciones: "))
        x=0
        referencia=int((90*limite)/100)
        conta=0.0
        venta=0
        while x<limite:
            r = randint(28, 32)
            if r==32:
                conta=conta+1
                if x<=referencia:
                    venta=venta+r
            elif x<=referencia:
                venta = venta + r
            x=x+1
        print "probabilidad de vender de 13 - 31 periodicos: ",(limite-conta)/limite
        print "periodicos vendidos en el 90% de las ocasiones: ", venta
        print"probabilidad de 2/10 quioscos vendan entre 13 - 31 periodicos: ",2*((limite-conta)/limite)/10

p=periodicos()
p.probabilidad()