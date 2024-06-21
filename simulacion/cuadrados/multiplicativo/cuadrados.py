from Tkinter import *
class cuadrado:
    def entrada(self):
        self.sl = Tk()
        self.sl.geometry("750x750")

        label_s = Label(self.sl, text="Semilla", fg="black",
                        font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=10, y=100)
        self.otro = IntVar()
        self.c = Entry(self.sl, textvariable=self.otro, font="Arial")
        self.c.place(x=110, y=100, width=150, height=35)

        label_s = Label(self.sl, text="datos", fg="black",
                        font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=300, y=100)
        self.otro1 = IntVar()
        self.c = Entry(self.sl, textvariable=self.otro1, font="Arial")
        self.c.place(x=500, y=100, width=150, height=35)

        boton = Button(self.sl, text="continuar", font=("Comic Sans MS", 20),
                       relief=SOLID, padx=20, pady=20, bg='grey', command=self.entrada1)
        boton.place(x=10, y=400)
        self.sl = mainloop()


    #def entrada1(self,semilla=34,res=10):
    def entrada1(self):
        self.band = True
        self.sem = ""
        self.x = 0
        self.datos=[]
        self.sem2 = 0
        #self.res=self.otro1
        #semilla=self.otro.get()
        self.res=self.otro1.get()
        #semilla = int(input("defina una semilla: "))
        #res = int(input("cantidad de numeros aletorios: "))
        self.x,self.datos=c.usuario(self.band,self.sem,self.x,self.sem2,self.otro.get(),self.res,self.datos)
        print self.x
        print self.datos
        print self.res
        print "condicion"
        if self.x==-1:
            print"llego"
            su = Toplevel()
            su.geometry("750x750")
            print self.datos
            lista = Listbox(su, width=60, height=10)
            for i in range(0, len(self.datos)):
                lista.insert(0, str(self.datos[i]))
            lista.place(x=10, y=10)
            su = mainloop()
        #if self.x!=self.res:
        else:
            c.ciclo()


    def ciclo(self):
        self.s= Tk()
        self.s.geometry("750x750")
        label_s = Label(self.s, text="la semilla no funciono agrega una nueva", fg="black",
                        font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=0, y=0)
        label_s = Label(self.s, text="Semilla", fg="black",
                              font=("Comic Sans MS", 20), bg='white', justify="center")
        label_s.place(x=10, y=100)
        #self.otro = IntVar()
        self.c = Entry(self.s, font="Arial")
        self.c.place(x=110, y=100, width=150, height=35)
        boton = Button(self.s, text="continuar", font=("Comic Sans MS", 20),
                               relief=SOLID, padx=20, pady=20, bg='grey', command=self.hecho)
        boton.place(x=10, y=400)
        self.s=mainloop()
    def hecho(self):
        obten=int (self.c.get())
        print "obten",obten
        print "x",self.x
        print "datos",self.datos
        print "res",self.res
        self.x, self.datos = c.usuario(True, "", self.x, 0, obten, self.res, self.datos)
        print "aqiu"

        if self.x!=-1:
            self.s.destroy()
            c.ciclo()
            print self.datos
        else:
            print self.datos
            print "retornando"

            su = Toplevel()
            su.geometry("750x750")
            print self.datos
            lista = Listbox(su, width=60, height=10)
            for i in range(0, len(self.datos)):
                lista.insert(0, str(self.datos[i]))
            lista.place(x=10, y=10)
            su = mainloop()

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
                print final
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
                numero = sizec[partir-1]+sizec[partir]
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

def entrada(self):
    self.sl = Tk()
    self.sl.geometry("750x750")

    label_s = Label(self.sl, text="Semilla", fg="black",
                    font=("Comic Sans MS", 20), bg='white', justify="center")
    label_s.place(x=10, y=100)
    self.otro = IntVar()
    self.c = Entry(self.sl, textvariable=self.otro, font="Arial")
    self.c.place(x=110, y=100, width=150, height=35)

    label_s = Label(self.sl, text="datos", fg="black",
                    font=("Comic Sans MS", 20), bg='white', justify="center")
    label_s.place(x=300, y=100)
    self.otro1 = IntVar()
    self.c = Entry(self.sl, textvariable=self.otro1, font="Arial")
    self.c.place(x=500, y=100, width=150, height=35)

    boton = Button(self.sl, text="continuar", font=("Comic Sans MS", 20),
                   relief=SOLID, padx=20, pady=20, bg='grey', command=self.entrada1)
    boton.place(x=10, y=400)
    self.sl = mainloop()