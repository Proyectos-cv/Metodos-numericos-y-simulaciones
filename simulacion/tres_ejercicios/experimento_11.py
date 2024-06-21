from random import *
class experimento:
    def probabilidad(self):
        limite=float(input("numero de iteraciones: "))
        x=0
        suma=0
        exitos_prob=0.0
        exitos_4_prob=0.0
        exitos_5_prob=0.0
        while x<limite:
            exitos=0
            exitos_4=0
            exitos_5=0
            for i in range(0, 24):
                r = randint(0, 1)
                if r==1:
                    suma=suma+1
            if suma==4:
                exitos_4=exitos_4+suma
                exitos = exitos + suma
            elif suma==5:
                exitos_5=exitos_5+suma
                exitos = exitos + suma
            else:
                exitos = exitos +suma
            x = x + 1
        #print exitos
        #print exitos_5
        #print exitos_4
        exitos_prob = exitos_prob + exitos / 24.0
        exitos_5_prob = exitos_5_prob + exitos_5 / 24.0
        exitos_4_prob = exitos_4_prob + exitos_4 / 24.0
        #print exitos_prob
        #print exitos_5_prob
        #print exitos_4_prob
        #print float(exitos_prob/limite)
        print "probabilidad de exitos: ",exitos_prob/limite
        print "probabilidad de 4 exitos: ",exitos_4_prob/limite
        print "probabilidad de 5 exitos: ",exitos_5_prob/limite
e=experimento()
e.probabilidad()