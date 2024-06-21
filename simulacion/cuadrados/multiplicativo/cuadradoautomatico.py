import random
class cuadrado:
    def entrada(self,res):
        band = True
        sem = ""
        x = 0
        sem2 = 0
        #semilla = int(input("defina una semilla: "))
        semilla = random.randrange(0,100)
        #res = int(input("cantidad de numeros aletorios: "))
        nu=[]
        #x,nu=c.usuario(band,sem,x,sem2,semilla,res,nu)
        x, nu = c.usuario(band, sem, x, sem2, semilla, res, nu)
        ba=True
        print x
        while ba==True:
            #semilla = int(input("defina una semilla: "))
            b=True
            d=str(semilla)
            s=len(d)
            while b==True:
                semilla = random.randrange(0,100)
                t=str(semilla)
                if len(t)==s:
                    b=False
            print "x",x
            print "nu",nu
            if x==-1:
                ba=False
            #x,nu=c.usuario(band, sem, x, sem2, semilla, res,nu)
            x,nu = c.usuario(band, sem, x, sem2, semilla, res, nu)
            print x
            print nu
            if x==-1:
                ba=False
        return nu




    def usuario(self,band,sem,x,sem2,semilla,res,nu):
        while(x<res and band==True):
            size=str(semilla)
            e=len(size)
            cuadrado=semilla**2
            print cuadrado
            aux=""
            final=""
            ayuda=""
            sizec=str(cuadrado)

            if len(sizec)<2*e:
                for i in range(0,(e*2)-len(sizec)):
                    aux=aux+"0"
                final=aux+sizec
                partir = len(final) / 2
                numero = final[partir - 1] + final[partir]
                partirmas = partir / 2
                for i in range(partirmas,e+partirmas):
                    ayuda=ayuda+final[i]
                semilla=int(ayuda)
                sem = int(ayuda)
                if ayuda[0]=="0" and x<=res:
                    band=False

                    return x,nu


            else:
                partir=len(sizec)/2
                partirmas = partir / 2
                numero=sizec[partir-1]+sizec[partir]
                for i in range(partirmas,e+partirmas):
                    ayuda=ayuda+sizec[i]
                semilla = int(ayuda)
                sem=int(ayuda)
                if ayuda[0]=="0" and x<=res:
                    print "la semilla fallo"
                    band=False

                    return x, nu

            if x==res-1:
                band=False
            print sem
            if sem2==semilla and x<=res:
                print "la semilla no funciona"
                band=False
                return x, nu

            sem2=sem
            nu.append(sem)
            x = x + 1
            if x==res:
                return -1,nu
            else:
                band=True

c=cuadrado()
#c.usuario()
#c.entrada()