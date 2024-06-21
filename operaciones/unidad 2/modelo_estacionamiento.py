from random import *
from numpy import *
from math import*
class modelo:
    def define(self,b):
        arrelleg=zeros(6)
        arresal = zeros(6)
        hora=8
        densidad=0
        clientesfuera=0
        minutos=0
        contador=1
        #ran=random.random()
        #print ran
        while contador<=b:
            prob = random.random()
            comienza=random.random()
            print"decimal"
            print comienza
            contador=contador +1
            #llegada=(log(comienza,10))
            print"logaritmo"
            llegada=(-60 / 10) * (log(comienza,10))
            densidad=(densidad+round(llegada))
            ida = 10 + (prob * (30 - 10))
            #(-60 / 10) * (LOG(A4))
            print llegada
            if llegada<0.5:
                llegada = 1
            print hora, ":", minutos

            horaactual = hora
            minutosactuales = minutos

            minutos=round(minutos+llegada)
            ida = round(ida+minutos)
            #if minutos<0.5:
             #   minutos=minutos+1
            if minutos>=60:
                hora+=1
                minutos=minutos-60
            print hora, ":",minutos


            band = False
            compara = minutos + hora
            for i in range(6):
                if compara > arresal[i]:
                    arresal[i]=0
                    arrelleg[i]=0
                    band=True

            print arrelleg
            c=0
            bandera2=False
            while band==True and c<=5:
                if arrelleg[c]==0:
                    arrelleg[c]=1
                    band=False
                    bandera2=True
                    arresal[c]=ida+hora

                c=c+1
            if bandera2==False:
                clientesfuera+=1
                print "me perdiste baby"


            print "datos de salida"
            print ida
            print "arreglo de llegada"
            print arrelleg
            print "arreglo de salida"
            print arresal
            print "clientes fuera"
            print clientesfuera
            sumaha=hora+minutos


            #print contador-1
            #print horaactual, minutosactuales

            promedio=minutosactuales/(contador-1)
            print "el promedio de llegada es de 1 auto cada: ",promedio,"minutos"
            print (densidad/contador-1)
            prom=((clientesfuera)*100/(contador-1))
            print "porcentaje de clientes que su fueron: "
            print prom,"%"
            pro=(c*100)/6
            print "porcentaje de lugares disponibles: ",pro,"%"

m=modelo()
b=int(input("cuantas iteraciones quieres: "))
m.define(b)