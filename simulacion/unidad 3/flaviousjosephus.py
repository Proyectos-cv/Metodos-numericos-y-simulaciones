import numpy as np
import random as r
class flavious:
    def descartar(self):
        ##definicion de variables principales
        auxciclo=""
        prin=raw_input("ingresar nombre: ")
        l=[]
        l1=[]
        total=0
        repeticion=0
        repnom=""
        var=-5
        contap=0
        referencia=np.array(["carlos ivan","alejandro","carlos nolasco", "leo","aldo","luis","alan","fany","ana laura","nayeli","diana","alma","ana isabel","estefania"])
        arre=np.array(["carlos ivan","alejandro","carlos nolasco", "leo","aldo","luis","alan","fany","ana laura","nayeli","diana","alma","ana isabel","estefania"])
        size=14
        posicion=0
        contaprim=0
        cuenta=0
        band=True
        arre1=np.zeros(14)
        x=0
        prob=0
        conta=0
        auxiliar=""
        empezar=0
        iteraciones=int(input("iteraciones: "))
        nombre=""



        ## encontrar al heroe

        while x<iteraciones:
            arre = np.array(
                ["carlos ivan", "alejandro", "carlos nolasco", "leo", "aldo", "luis", "alan", "fany", "ana laura",
                 "nayeli", "diana", "alma", "ana isabel", "estefania"])
            size=14
            #print arre
            band=True
            while band==True:
                empezar=r.randrange(0,size)
                correr=r.randrange(0,11)
                for i in range(0,correr):
                    empezar = empezar + 1
                    if empezar>=size:
                        empezar=0
                #print arre[empezar]
                for j in range(empezar,size-1):
                    arre[j]=arre[j+1]
                size=size-1
                if size==0:
                    band=False

            ##variable para el heroe
            nombre = arre[0]

            ##encontrar la pocision en el arreglo original
            posi=0
            for g in range(len(referencia)):
                if referencia[g]==nombre:
                    posi=g
            #print "nomb",nombre
            #print "pos",posi


            ##dos incisos

            #print nombre
            if nombre==auxiliar:
                conta=conta+1

                if conta == 3:
                    prob = prob + 1
                    l1.append(conta)
                    l1.append(nombre)
                    conta = 0

                if posi==0 or posi==1 or posi==2 or posi==4 or posi==6 or posi==10 or posi==12:
                    contap=contap+1
                    if contap==3:
                        contaprim=contaprim+1

                if posi==3 or posi==5 or posi==7 or posi==8 or posi==9 or posi==11 or posi==13:
                    contap=0

                if nombre==auxciclo:
                    repeticion=repeticion+1
                    if repeticion>total:
                        total=repeticion
                        repnom=nombre
                        l.append(total)
                        l.append(repnom)
                if nombre!=auxciclo:
                    repeticion=0
                auxciclo=nombre
                #print nombre
            elif nombre!=auxiliar:
                conta=0
                contap=0

            auxiliar=nombre

            ##encontrar al mayor y al menor

            a,b,c,d=f.d(nombre,arre1,prin)

            ##aumentar contador del while
            x=x+1

            ## probabilidades del medio

            if posi == var - 1 or posi == var + 1:
                cuenta = cuenta + 1
            var = posi


        #imprimir probabilidades
        print "3 sucesivas"
        print float(prob)/float(iteraciones)
        print l1
        print""
        print "primos"
        print float(contaprim)/float(iteraciones)
        print ""
        print "medio"
        print float(cuenta)/float(iteraciones)
        print ""
        print "mayor - menor"
        print ""
        print a
        print b
        print c
        print ""
        print "repetidos consecutivos"
        print "nombre: ",repnom
        print "cantidad: ",total
        print l
        print""
        print"probabilidad de una persona elegida"
        print d
        #print nombre
        #print prob

    def d(self,nombre,arre1,prin):
        cantidad = np.array(
            ["carlos ivan", "alejandro", "carlos nolasco", "leo", "aldo", "luis", "alan", "fany", "ana laura",
             "nayeli", "diana", "alma", "ana isabel", "estefania"])
        #print nombre
        if nombre=="carlos ivan":
            arre1[0]=arre1[0]+1
        elif nombre=="alejandro":
            arre1[1]=arre1[1]+1
        elif nombre =="carlos nolasco":
            arre1[2]=arre1[2]+1
        elif nombre =="leo":
            arre1[3]=arre1[3]+1
        elif nombre =="aldo":
            arre1[4]=arre1[4]+1
        elif nombre =="luis":
            arre1[5]=arre1[5]+1
        elif nombre =="alan":
            arre1[6]=arre1[6]+1
        elif nombre =="fany":
            arre1[7]=arre1[7]+1
        elif nombre =="ana laura":
            arre1[8]=arre1[8]+1
        elif nombre =="nayeli":
            arre1[9]=arre1[9]+1
        elif nombre =="diana":
            arre1[10]=arre1[10]+1
        elif nombre =="alma":
            arre1[11]=arre1[11]+1
        elif nombre =="ana isabel":
            arre1[12]=arre1[12]+1
        elif nombre =="estefania":
            arre1[13]=arre1[13]+1
        au=arre1[0]
        au1 = arre1[0]
        pos=0
        posic=0

        sumatotal=0
        sumaprin=0

        for i in range(14):
            if arre1[i]>au:
                au=arre1[i]
                pos=i
            elif arre1[i]<au1:
                au1=arre1[i]
                posic=i

        for z in range(14):
            #print arre1[z]
            if prin==cantidad[z]:
                sumaprin=arre1[z]
            else:
                sumatotal=sumatotal+arre1[z]
        a="arreglo: ", arre1
        b="menor cantidad: ", au1,cantidad[posic]
        c="mayor cantidad: ", au,cantidad[pos]
        #print sumaprin
        #print sumatotal
        d="probabilidad de la persona: ", sumaprin/sumatotal
        return a,b,c,d
        #print au1
        #print pos
        #return au,au1

f=flavious()
f.descartar()
###### inciso a
#la mayor cantidad de veces consecutivas que se repite la persona
#####la probabilidad de que una persona y la que este antes o despues de ella en la fila salgan seleccionadas una en seguidad e otra iteracion
#####probabilidad de que en una secuencia contigua de tres ocaciones (1) pero que se encuentre ubicada en una posicion con un valor primo
#####la mayor cantidad de veces que se reipte la misma persona
####la mayor cantidad de veces que sale menos veces
#idear probabilidad