import numpy
import random as r
class metodopoker:
    def aleatorios(self):
        x=0
        #while x<vez:
        num = ""
       # numero = 0
        for i in range(5):
            ale=r.randrange(0,10)
            num=num+str(ale)
           # numero=int(num)
        #k.append(num)
        x=x+1
        #print"num", num
        return num

        #print"ale", numero

    def pruebaestadistica(self,vez):

        nada = float(0)
        par = float(0)
        doblepar = float(0)
        tercia = float(0)
        quintilla = float(0)
        poker = float(0)
        full = float(0)
        comodin = float(0)

        #manocarta=numpy.array([2,1,2,9,2])
        itera=1
        x=0
        while x<vez:
            l = []
            cantidad = 0
            manocarta = m.aleatorios()
            #manocarta="04440"
            k = numpy.zeros(5)
            for i in range(5):
                k[i]=manocarta[i]

            for i in range(0, 5):
                for j in range(i + 1, 5):
                    if i != j:
                        if k[i] == k[j] and k[i] not in l:
                            l.append(k[i])
            print k
            for i in range(0, 5):
                aux = k[i]
                for j in range(i + 1, 5):
                    if k[j] == aux and k[j] != 11:

                        k[j] = '11'

                        cantidad = cantidad + 1
           # print l
            #print cantidad
            print k
            if len(l) == 1 and cantidad == 2:
                tercia = tercia + 1
            elif len(l) == 1 and cantidad == 1:
                par = par + 1
            elif len(l) == 2 and cantidad==2:
                doblepar = doblepar + 1
            elif len(l) == 1 and cantidad == 4:
                quintilla = quintilla + 1
            elif len(l) == 2 and cantidad == 3:  # and comodin==1:
                full = full + 1
            elif len(l) == 1 and cantidad == 3 :
                poker = poker + 1

            else:
                nada = nada + 1

            x = x + 1
        #print manocarta
        return tercia,par,doblepar,full,nada,quintilla,poker


    def fofe(self):
        fo=[]
        fe=[]
        vez = int(input("numero de aleatorios que quiere: "))
        tercia,par,doblepar,full,nada,quintilla,poker=m.pruebaestadistica(vez)
        fo.append(nada)
        fo.append(par)
        fo.append(doblepar)
        fo.append(tercia)
        fo.append(full)
        fo.append(poker)
        fo.append(quintilla)

        #fo.append(15)
        #fo.append(17)
        #fo.append(4)
        #fo.append(3)
        #fo.append(1)
        #fo.append(0)
        #fo.append(0)
        print fo
        fe.append(0.3024)
        fe.append(0.504)
        fe.append(0.108)
        fe.append(0.072)
        fe.append(0.0092)
        fe.append(0.0045)
        fe.append(0.0001)
        print fe
        #vez=40
        for i in range(len(fe)):
            fe[i]=fe[i]*vez
        print fe
        print fo
        band=True
        o=len(fe)-1
        sumafe=0
        sumafo=0
        while band==True:
            if sumafe<5:
                sumafe=sumafe+fe[o]
                sumafo=sumafo+fo[o]
                o=o-1
            else:
                print o
                arre=numpy.zeros(o+2)
                arre1 = numpy.zeros(o + 2)
                for i in range(o+1):
                    arre[i]=fe[i]
                    arre1[i]=fo[i]
                arre[o+1]=sumafe
                arre1[o+1]=sumafo
                print arre
                print arre1
                band=False

        print""
        print"tercia: ", tercia
        print"par: ", par
        print"doblepar: ", doblepar
        print "full: ", full
        print"nada: ", nada
        print"quintilla: ", quintilla
        print"poker: ", poker
        print""
        est=0
        for i in range(len(arre1)):
            est=est+((arre1[i]-arre[i])**2/(arre[i]))
        print est



    def intento(self):
        q=0.12435
        r=str(q)
        print r
        print len(r)
        nuevo=""
        for i in range(2,len(r)):
            nuevo=nuevo+r[i]
        print nuevo
        f=0
        f=m.pueba(f)
        print f

    def pueba(self,f):
        f=f+1
        return f

m=metodopoker()
#m.pruebaestadistica()
m.fofe()
#m.intento()
#m.aleatorios()