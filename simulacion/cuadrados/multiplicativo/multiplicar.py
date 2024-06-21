import numpy as n
import random
from Tkinter import *
class multi:
    def entrada(self):
        self.sl = Tk()
        self.sl.geometry("750x750")

        label_s = Label(self.sl, text="Semilla", fg="black",
                        font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=10, y=100)
        self.otro = IntVar()
        self.c1 = Entry(self.sl, textvariable=self.otro, font="Arial")
        self.c1.place(x=110, y=100, width=150, height=35)

        label_s = Label(self.sl, text="datos", fg="black",
                        font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=300, y=100)
        self.otro1 = IntVar()
        self.c = Entry(self.sl, textvariable=self.otro1, font="Arial")
        self.c.place(x=500, y=100, width=150, height=35)

        boton = Button(self.sl, text="continuar", font=("Comic Sans MS", 20),
                       relief=SOLID, padx=20, pady=20, bg='grey', command=self.mul)
        boton.place(x=10, y=400)
        self.sl = mainloop()



    def mul(self):

        referencia=float(0)
        band=True
        al=0
        lugar=0
        lugar1=0
        self.anterior=10000
        self.anterior1 = 10000
        ahora=0
        while band==True:
            al=random.randrange(1,800)
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
                if ahora1 <= self.anterior1:
                    lugar1=j
                    self.anterior1 = ahora1
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
                if ahora <= self.anterior:
                    lugar = j
                    self.anterior = ahora


        print ""
        print "referencia", referencia
        print "anterior -",self.anterior,"  ",lugar
        print "anterior +",self.anterior1,"  ",lugar1
        self.datos=[]

        #res = int(self.c.get())
        #print"caja", res
        #semilla = int(self.c1.get())
        #print"semilla", semilla

        self.res=int(self.c.get())#int(input("iteraciones"))
        self.x=0
        ayuda=int(self.c1.get())#int(input("semilla"))


        if anterior < anterior1:
            self.x, self.datos = m.semillas(self.anterior, self.res, self.x, ayuda, self.datos)
            if self.x != -1:
                m.ciclo()
        else:
            self.x, self.datos = m.semillas(self.anterior1, self.res, self.x, ayuda, self.datos)
            if self.x != -1:
                m.ciclo()
    def ciclo(self):
        self.s = Tk()
        res = self.c.get()
        print"caja", res
        self.s.geometry("750x750")
        label_s = Label(self.s, text="la semilla no funciono agrega una nueva", fg="black",
                        font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=0, y=0)
        label_s = Label(self.s, text="Semilla", fg="black",
                        font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=10, y=100)
        # self.otro = IntVar()
        self.c3 = Entry(self.s, font="Arial")
        self.c3.place(x=110, y=100, width=150, height=35)
        boton = Button(self.s, text="continuar", font=("Comic Sans MS", 20),
                       relief=SOLID, padx=20, pady=20, bg='grey', command=self.hecho)
        boton.place(x=10, y=400)
        self.s = mainloop()

    def hecho(self):
        if self.anterior < self.anterior1:
            self.x, self.datos = m.semillas(self.anterior, self.res, self.x, self.c3.get(), self.datos)
            if self.x != -1:
                m.ciclo()
        else:
            self.x, self.datos = m.semillas(self.anterior1, self.res, self.x, self.c3.get(), self.datos)
            if self.x != -1:
                m.ciclo()
        if self.x!=-1:
            m.ciclo()
        else:
            su = Toplevel()
            su.geometry("750x750")
            print self.datos
            lista = Listbox(su, width=60, height=10)
            for i in range(0, len(self.datos)):
                lista.insert(0, str(self.datos[i]))
            lista.place(x=10, y=10)
            su = mainloop()

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
                    print x,datos
                    return x,datos
            #if x==res-1:
             #   band=False
            if sem2==semilla and x<=res:
                print "la semilla no funciona"
                band=False
                print x,datos
                return x,datos
                    # print partir
            sem2 = sem
            datos.append(ayuda)
            x = x + 1
            if x==res:
                print x,datos
                return -1,datos
            else:
                band=True



        #if self.x != -1:
         #   self.s.destroy()
          #  c.ciclo()
           # print self.datos
       # else:
        #    print self.datos
         #   print "retornando"

#            su = Toplevel()
 #           su.geometry("750x750")
  #          print self.datos
   #         lista = Listbox(su, width=60, height=10)
    #        for i in range(0, len(self.datos)):
     #           lista.insert(0, str(self.datos[i]))
      #      lista.place(x=10, y=10)
       #     su = mainloop()




    def mu(self):
        a=float(float(3)/float(2))
        print a
m=multi()
m.entrada()
#m.mul()
#m.semillas()
def sigue(self):
        if anterior<anterior1:
            x,datos=m.semillas(anterior,res,x,ayuda,datos)
            ba = True
            print x
            while ba == True and x!=None:
                ayuda = int(input("defina una semilla: "))
                x,datos = m.semillas(anterior,res,x,ayuda,datos)
                print x
                print datos
                if x == -1:
                    ba = False
        else:
            x,datos=m.semillas(anterior1,res,x,ayuda,datos)
            ba=True
            while ba == True and x!=None:
                ayuda = int(input("defina una semilla: "))
                x,datos = m.semillas(anterior1,res,x,ayuda,datos)
                print x
                print datos
                if x == -1:
                    ba = False
