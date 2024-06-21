
class cuadrado:
    def entrada(self):
        band = True
        sem = ""
        x = 0
        datos=[]
        sem2 = 0
        semilla = int(input("defina una semilla: "))
        res = int(input("cantidad de numeros aletorios: "))
        x,datos=c.usuario(band,sem,x,sem2,semilla,res,datos)
        ba=True
        print x
        while ba==True:
            semilla = int(input("defina una semilla: "))
            x,datos=c.usuario(band, sem, x, sem2, semilla, res,datos)
            print x
            if x==-1:
                ba=False
        print datos

    def usuario(self,band,sem,x,sem2,semilla,res,datos):

        while(x<res and band==True):
            #cantidad = int(input("cuantos numeros aleatorios: "))
            size=str(semilla)
            e=len(size)
            cuadrado=semilla**2
            print cuadrado
            #print "cuadrado: ",cuadrado
            aux=""
            final=""
            ayuda=""
            sizec=str(cuadrado)

            if len(sizec)<2*e:
                for i in range(0,(e*2)-len(sizec)):
                    aux=aux+"0"
                final=aux+sizec
               # print"final: ", final
                partir = len(final) / 2
                #partirmas=partir/2
                numero = final[partir - 1] + final[partir]
                partirmas = partir / 2
                for i in range(partirmas,e+partirmas):
                    ayuda=ayuda+final[i]
                #print "a"+ayuda
                #print "numero: ",ayuda
                #x = x + 1
                semilla=int(ayuda)
                sem = int(ayuda)
                if ayuda[0]=="0" and x<=res:
                    band=False
                    return x,datos

            else:
                partir=len(sizec)/2
                partirmas = partir / 2
                numero=sizec[partir-1]+sizec[partir]
                for i in range(partirmas,e+partirmas):
                    ayuda=ayuda+sizec[i]
                #print "a"+ayuda
                #print "sizec: ",sizec
                #print"numero: ",ayuda
               #x=x+1
                semilla = int(ayuda)
                sem=int(ayuda)
                if ayuda[0]=="0" and x<=res:
                    band=False
                    return x,datos

            #if x==res-1:
             #   band=False
            print sem
            if sem2==semilla and x<=res:
                print "la semilla no funciona"
                band=False
                return x,datos
                    # print partir

            sem2=sem
            datos.append(ayuda)
            x = x + 1
            if x==res:
                return -1,datos
            else:
                band=True
            #print numero
c=cuadrado()
#c.usuario()
c.entrada()




#sem2=0
 #                   sem=""
  #                  print "no funciono la semilla"
   #                 print x
    #                sem = ""
     #               nuevasemilla = int(input("defina una semilla: "))
      #              c.usuario(band, sem, x, sem2, nuevasemilla, res)