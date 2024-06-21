import numpy as n
import random
class multi:
    def mul(self,res):
        referencia=float(0)
        band=True
        al=0
        lugar=0
        lugar1=0
        anterior=10000
        anterior1 = 10000
        ahora=0
        datos=[]
        while band==True:
            al=random.randrange(100,800)
            if al%2!=0 and al%5!=0:
                band=False
        st=str(al)
        e=len(st)

        referencia=float(10**((float(e)/float(2))))
        #q1=n.array([3,2,1,45,5])
        q1=n.zeros(10)
        for i in range(0,10):
            ale=random.randrange(1,100)
            q1[i]=ale
        print q1
        for i in range(len(q1)-1):
            for j in range(len(q1)-1):
                if q1[j] > q1[j + 1]:
                    s1 = q1[j]
                    q1[j] = q1[j + 1]
                    q1[j + 1] = s1
        print q1
        print al
        print e
        #e=150
        print referencia
        #referencia=500
        anterior1=abs((200*(1)+q1[0]))


        vez=(int(referencia)/float(200))+1
        print vez
        c=0
        for lin in range(0,int(vez)):
            c=c+200
            print "subio"
            for j in range(0, len(q1)):
                ahora1 = abs((float(c * (1)) + float(q1[j])))
                print ahora1
                if ahora1 <= anterior1:
                    lugar1=j
                    anterior1 = ahora1
        print ""
        anterior = abs((float(200 * (1)) - q1[0]))
        vez = (referencia / float(200)) + 1
        c = 0
        for lin in range(0,int(vez)):
            c = c + 200
            print "subio"
            for j in range(0, len(q1)):
                ahora = abs((c * (1) - float(q1[j])))
                print ahora
                if ahora <= anterior:
                    lugar = j
                    anterior = ahora


        print ""
        print "referencia", referencia
        print "anterior -",anterior,"  ",lugar
        print "anterior +",anterior1,"  ",lugar1

        #res=int(input("iteraciones"))
        x=0
        #ayuda=int(input("semilla"))
        ar=0
        ayuda=al
        ayuda=ar
        if anterior<anterior1:
            x,datos=m.semillas(anterior,res,x,ayuda,datos)
            ba = True
            #print x
            while ba == True and x!=None:
                #ayuda = int(input("defina una semilla: "))
                ar = 0
                b=True
                while b == True:
                    ar = random.randrange(100, 800)
                    if al % 2 != 0 and al % 5 != 0:
                        b = False
                ayuda = ar
                x,datos = m.semillas(anterior,res,x,ayuda,datos)
                #print x
                print datos
                print x
                if x == -1:
                    ba = False
        else:
            x,datos=m.semillas(anterior1,res,x,ayuda,datos)
            ba=True
            while ba == True and x!=None:
                #ayuda = int(input("defina una semilla: "))
                ar = 0
                b=True
                while b == True:
                    ar = random.randrange(100, 800)
                    if al % 2 != 0 and al % 5 != 0:
                        b= False
                ayuda = ar
                x,datos = m.semillas(anterior1,res,x,ayuda,datos)
                #print x
                print datos
                print x
                if x == -1:
                    ba = False
        return datos

    def semillas(self,semilla,res,x,ayuda,datos):
        #semilla = 200 * (1) - 86
        #semilla = 107
        print semilla
        sem2=0
        #res=5
        band=True
        semilla=int(semilla)
        #x=0
        #ayuda=367
        #ayuda=int(input("defina una semilla"))
        while (x < res and band == True):

            size = str(ayuda)
            e = len(size)
            print e
            #cuadrado = semilla ** 2
            cuadrado=semilla*int(ayuda)
            print cuadrado
            print ayuda
            aux = ""
            final = ""
            ayuda = ""
            sizec = str(cuadrado)
            if len(sizec) < 2 * e:
                for i in range(0, (e * 2) - len(sizec)):
                    aux = aux + "0"
                final = aux + sizec
                print"final: ", final

                partir = len(final) / 2
                numero = final[partir - 1] + final[partir]
                partirmas = partir / 2
                #for i in range(partirmas, e + partirmas):
                for i in range(len(final)-e,len(final)):
                    ayuda = ayuda + final[i]

                print "numero: ", ayuda

                #x = x + 1
                semilla = int(ayuda)
                sem = int(ayuda)
                if ayuda[0] == "0":
                    band = False
                    print "no funciono la semilla"
                    print x
                    print datos
                    return x,datos
            else:

                partir = len(sizec) / 2
                partirmas = partir / 2
                numero = sizec[partir - 1] + sizec[partir]
                #for i in range(partirmas, e + partirmas):
                for i in range(len(sizec) - e, len(sizec)):
                    ayuda = ayuda + sizec[i]


                # print "a"+ayuda
                print "sizec: ", sizec
                print"numero: ", ayuda
                #x = x + 1
                semilla = int(ayuda)
                sem = int(ayuda)
                if ayuda[0] == "0":
                    band = False
                    print "no funciono la semilla"
                    print x
                    print datos
                    return x,datos
            #if x==res-1:
             #   band=False
            if sem2==semilla and x<=res:
                print "la semilla no funciona"
                band=False
                print x
                print datos
                return x,datos
                    # print partir
            sem2 = sem
            datos.append(ayuda)
            #print x
            x = x + 1
            if x==res:
                return -1,datos
            else:
                band=True
    def a(self):
        a=0
        l=[]
        for i in range(5):

            a,l=m.checa(a,l)
            print a,l

        a, l = m.checa(1, l)
        print a,l
    def checa(self,a,l):
        return a,l
m=multi()
#m.mul()
#m.a()
#m.semillas()