import random
import numpy
class geo:
    def geometrica(self):
        x = float(input("numero de corridas: "))
        favor = 0.0
        n = 0
        while n < x:
            truco = random.randrange(1, 4)
            if truco<3:
                arre = numpy.zeros(8)
                for i in range(8):
                    ale=random.randrange(1,3)
                    arre[i]=ale
                #arre=numpy.array([1,1,1,1,1,1,1,2])
                #print arre[7]
                if arre[0]==1 and arre[1]==1 and arre[2]==1 and arre[3]==1 and arre[4]==1 and arre[5]==1 and arre[6]==1 and arre[7]==2:
                    favor=favor+1
                n = n + 1
        prob=favor/x
        print favor
        #print arre
        print (prob)
g=geo()
g.geometrica()