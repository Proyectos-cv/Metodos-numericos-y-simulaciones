import random
import numpy
class todo:
    def exito(self):
        ir=int(input("iteraciones: "))
        uno=0.0
        dos=0.0
        z=0
        while z<ir:
            nu=random.randrange(0,2)
            if nu==0:
                #for r in range(6):
                arre=numpy.zeros(5)
                for i in range(5):
                    ale=random.randrange(0,2)
                    arre[i]=ale
                if arre[0]==0 and arre[1]==0 and arre[2]==0 and arre[3]==0 and arre[4]==1:
                    uno=uno+1

            #for r in range(5):
            else:
                arre = numpy.zeros(6)
                for i1 in range(6):
                    ale = random.randrange(0, 2)
                    arre[i1] = ale
                if arre[0]==0 and arre[1]==0 and arre[2]==0 and arre[3]==0 and arre[4]==0 and arre[5]==1:
                    dos=dos+1
            z=z+1
        print uno
        print  dos
        prob=uno/ir
        prob1=dos/ir
        print"probabilidad ecenario 1: ",prob
        print"probabilidad ecenario 2: ", prob1
    def exitos(self):
        n = 4
        a = numpy.random.rand(n)
        print a
t=todo()
t.exito()
#0.03
#0.0000002

#60 por ciento mujerews y 40 por ciento de hombres
#5 por ciento de mujeres y dos de hombres estan dipuestos a comprar un carro
#a) determine la probavilidad de que al extrer una muestra una mujr este dispuesta a comprar u carro
#b) determine la probabilidad de que al extrarr una muestra de un hombre este dispuesot a compear el carro
