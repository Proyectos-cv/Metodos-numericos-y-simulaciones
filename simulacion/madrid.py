#60 por ciento mujerews y 40 por ciento de hombres
#5 por ciento de mujeres y dos de hombres estan dipuestos a comprar un carro
#a) determine la probavilidad de que al extrer una muestra una mujr este dispuesta a comprar u carro
#b) determine la probabilidad de que al extrarr una muestra de un hombre este dispuesot a compear el carro

#archivo numero 5, tombola, pruebaaleatoria,madrid, geometrica, dispersion

import numpy
import random
class madrid:
    def comprar(self):
        mujer=0.0
        hombre=0.0
        x=0
        vez=int(input("iteraciones: "))
        while x<vez:
            ale=random.randrange(0,11)
            if ale<7:
                com=random.randrange(0,101)
                if com<6:
                    mujer=mujer+1
            else:
                com = random.randrange(0,101)
                if com < 2:
                    hombre = hombre + 1
            x=x+1
        proh=hombre/vez
        prom=mujer/vez
        print proh
        print prom
m=madrid()
m.comprar()