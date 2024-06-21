#n=int(input("numero de discos: "))
#origen='a'
#destino='b'
#auxiliar='c'
#def hanoi(n,origen,auxiliar, destino):
   # if n==1:
    #    print "se mueve de la torre: ", origen, "a torre: ", destino
    #else:
     #   hanoi(n-1,origen,destino,auxiliar)
      #  print "se mueve de la torre: ", origen,"a torre: ", destino
       # hanoi(n-1,auxiliar,origen,destino)

#hanoi(n,origen,auxiliar, destino)
import numpy as np
class re:
    def inicia1(self):
        b = int(input("dimension: "))
        a = np.zeros(b)
        for i in range(b):
            a[i] = int(input("numero: "))
        r.derecha(a, b)
    def derecha(self,a, b):
        aux = len(a)
        if b > 0:
            print a[b-1]
            return r.derecha (a, b-1)


    def inicia(self):
        b = int(input("inicio de la contabilidad: "))
        f=int(input("dimension del arreglo: "))
        a = np.zeros(f)
        for i in range(f):
            a[i] = int(input("numero: "))
        r.izquierda(a,b,f)

    def izquierda(self,a, b,f):
        aux = len(a)
        if b < aux:
            print a[b]
            return r.izquierda(a,b+1,f)
    def han1(self):
        n=int(input("discos: "))
        origen='a'
        auxiliar='b'
        destino='c'
        tope=0
        band=False

        while n>0 and band==False:
            while n>1:
                tope=tope+1
                pilan=n
                pilao=origen
                pilad=destino
                pilax=auxiliar
                n=n-1
                varaux = destino
                destino = auxiliar
                auxiliar = varaux
            print "mover de: ",origen," a: ",destino
            band=True
            if tope>0:
                n=pilan
                origen=pilao
                destino=pilad
                auxiliar=pilax
                tope=tope-1
                print "mover }de: ", origen, " a: ", destino
                n=n-1
                varaux=origen
                origen=auxiliar
                auxiliar=varaux
                band=False

    def han(self):
        n=int(input("discos: "))
        origen='a'
        auxiliar='b'
        destino='c'
        band=False

        #while n>0:
        while band==False:
            pilan=n
            pilao=origen
            pilad=destino
            pilax=auxiliar

            varaux = destino
            destino = auxiliar
            auxiliar = varaux
            print "mover de: ",origen," a: ",destino
            if n>1:
                n=pilan
                origen=pilao
                destino=pilad
                auxiliar=pilax
                print "mover }de: ", origen, " a: ", destino

                varaux=origen
                origen=auxiliar
                auxiliar=varaux
                n=n-1
            else:
                band=True

r=re()
r.han()
#r.inicia1()
