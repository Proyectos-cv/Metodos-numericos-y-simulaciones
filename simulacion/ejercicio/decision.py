
import random as r
class decidir:
    def analiza(self):
        viaje=0.0
        vez=int(input("veces: "))
        x=0.0
        while x < vez:
            bola=r.randrange(1,21)
            if bola>8:
                dado=r.randrange(2,13)
                if dado!=6:
                    viaje=viaje+1
            x=x+1
        #print viaje
        #print x
        pro=viaje/vez
        #print viaje
        print "probabilidad: ",pro
d=decidir()
d.analiza()