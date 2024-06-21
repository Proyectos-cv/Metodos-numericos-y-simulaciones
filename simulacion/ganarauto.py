#probabilidad de ganar, precio tendra 6 cifras
#veces que saco
#https://github.com/login?client_id=01ab8ac9400c4e429b23&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D01ab8ac9400c4e429b23%26response_type%3Dcode%26scope%3Dread%253Auser%26state%3DLWKgbejO8mdUfcfBGomROkvz5CY%252FeyJjYWxsYmFja1VyaSI6InZzY29kZTovL3ZzY29kZS5naXRodWItYXV0aGVudGljYXRpb24vZGlkLWF1dGhlbnRpY2F0ZT93aW5kb3dpZD0xIiwicmVzcG9uc2VUeXBlIjoiY29kZSIsInN0YXRlIjoiZWJkMTU4ZjgtZjMwZS00YTU0LTkzNzItMzdjYTEyMzcxNDI0IiwiaWQiOiIxODcuMTMzLjEwMC4xMTIifQ
#https://www.youtube.com/watch?v=ANF1X42_ae4&list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU
import numpy
import random
class chabelo:
    def ganar(self):
        xr=0
        sacar=0
        pierde=0
        vez=int(input("iteraciones: "))

        l=[]
        ganar=0.0
        perder=0.0
        while xr<vez:
            band = True
            #perder = 0
            #ganar = 0
            precio = numpy.array([4, 5, 3, 6, 2, 1])
            urna = numpy.array([1, 2, 3, 4, 5, 6, 0, 0, 0])
            k=[]
            while band==True:
                elige1=random.randrange(0,9)
                elige=urna[elige1]
                if elige!=0:
                    posicion=random.randrange(6)
                    con=0
                    for i in range(len(l)):
                        if l[i]==elige:
                            con=con+1
                    if precio[posicion]==elige and con==0:
                        l.append(elige)
                        precio[posicion]=11
                        if precio[0]==11 and precio[1]==11 and precio[2]==11 and precio[3]==11 and precio[4]==11:
                            ganar=ganar+1
                            #print "gana"
                            band=False
                elif elige==0:
                    b=True
                    for i in range(len(k)):
                        if k[i]==elige1:
                            b=False
                    if b==True:
                        perder=perder+1
                    if perder>=3:
                        pierde=pierde+1
                        band=False
                    k.append(elige1)

                        #print "pierde"

            xr=xr+1
        #print xr
        print"probabilidad de ganar dadas las iteraciones: ", ganar
        #print pierde

c=chabelo()
c.ganar()