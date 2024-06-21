from Tkinter import *
import numpy
import random as r
#from Tkinter import Messagebox
class Metodo_pocket:
    def __init__(self):
        self.ventana_metodo_pocket = Tk()
        self.ventana_metodo_pocket.geometry("900x900")
        #self.ventana_metodo_pocket.title('Metodo multiplicativo')
        self.ventana_metodo_pocket.config(bg="green")
#        self.ventana_metodo_pocket.iconbitmap("icono_proyecto_simulacion.ico")
        self.ventana_metodo_pocket.config(cursor="hand2")
        self.ventana_metodo_pocket.config(relief="sunken")
        label_titulo = Label(self.ventana_metodo_pocket, text="Metodo Pocker ",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_titulo.place(x=250, y=10)
        label_numero_alea=Label(self.ventana_metodo_pocket, text=" Cantidad de numeros  ",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_numero_alea.place(x=10,y=90)
        self.cantida_de_numeros=Entry(self.ventana_metodo_pocket,font="Arial")
        self.cantida_de_numeros.place(x=310,y=90,width=150, height=35)
        label_FO_de_diferentes=Label(self.ventana_metodo_pocket, text=" FO  Diferentes",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_FO_de_diferentes.place(x=10,y=150)
        self.resultado_FO_de_diferentes=Entry(self.ventana_metodo_pocket,font="Arial")
        self.resultado_FO_de_diferentes.place(x=310,y=150,width=150, height=35)
        label_FO_de_pares = Label(self.ventana_metodo_pocket, text=" FO  Pares", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_FO_de_pares.place(x=10, y=210)
        self.resultado_FO_de_pares=Entry(self.ventana_metodo_pocket,font="Arial")
        self.resultado_FO_de_pares.place(x=310,y=210,width=150, height=35)
        label_de_FO_de_dos_pares=Label(self.ventana_metodo_pocket, text=" FO Dos Pares", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_de_FO_de_dos_pares.place(x=10,y=260)
        self.resultado_FO_de_dos_pares = Entry(self.ventana_metodo_pocket, font="Arial")
        self.resultado_FO_de_dos_pares.place(x=310, y=260, width=150, height=35)
        label_de_FO_de_tercia = Label(self.ventana_metodo_pocket, text=" FO Tercia", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_de_FO_de_tercia.place(x=10, y=310)
        self.resultado_FO_de_tercia = Entry(self.ventana_metodo_pocket, font="Arial")
        self.resultado_FO_de_tercia.place(x=310, y=310, width=150, height=35)
        label_de_FO_de_full = Label(self.ventana_metodo_pocket, text=" FO Full ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_de_FO_de_full.place(x=10, y=360)
        self.resultado_FO_de_full = Entry(self.ventana_metodo_pocket, font="Arial")
        self.resultado_FO_de_full.place(x=310, y=360, width=150, height=35)
        label_de_FO_de_poker = Label(self.ventana_metodo_pocket, text=" FO Poker ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_de_FO_de_poker.place(x=10, y=410)
        self.resultado_FO_de_poker = Entry(self.ventana_metodo_pocket, font="Arial")
        self.resultado_FO_de_poker.place(x=310, y=410, width=150, height=35)
        label_de_FO_de_quintilla = Label(self.ventana_metodo_pocket, text=" FO Quintilla ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_de_FO_de_quintilla.place(x=10, y=460)
        self.resultado_FO_de_quintilla = Entry(self.ventana_metodo_pocket, font="Arial")
        self.resultado_FO_de_quintilla.place(x=310, y=460, width=150, height=35)
        label_probabilidad=Label(self.ventana_metodo_pocket,text=" Probabilidad ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_probabilidad.place(x=500,y=90)
        self.caja_probabilidad=Entry(self.ventana_metodo_pocket, font="Arial")
        self.caja_probabilidad.place(x=690, y=90, width=150, height=35)
        #Aqui van los botones
        boton_generar=Button(self.ventana_metodo_pocket, text="Generar ", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.principal)
        boton_generar.place(x=10,y=510)
        boton_salir=Button(self.ventana_metodo_pocket, text="Salir", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.ventana_metodo_pocket.destroy)
        boton_salir.place(x=210,y=510)
        self.ventana_metodo_pocket.mainloop()

    def principal(self):
        x = 0
        vez = float(self.cantida_de_numeros.get())
        f = 0
        funcion_princial = self.pruebaestadistica(vez)
        #funcion_fe = self.pueba(f)
        alea=self.aleatorios(x)
        #inteto=self.intento()
        resultado=self.fofe()

    def aleatorios(self,x):
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
        print("El valor de vez",vez)
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
            manocarta = self.aleatorios(x)
            #manocarta="04440"
            k = numpy.zeros(5)
            for i in range(5):
                k[i]=manocarta[i]

            for i in range(0, 5):
                for j in range(i + 1, 5):
                    if i != j:
                        if k[i] == k[j] and k[i] not in l:
                            l.append(k[i])
            print (k)
            for i in range(0, 5):
                aux = k[i]
                for j in range(i + 1, 5):
                    if k[j] == aux and k[j] != 11:

                        k[j] = '11'

                        cantidad = cantidad + 1
           # print l
            #print cantidad
            print (k)
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
        vez=int(self.cantida_de_numeros.get())
        print("Se muestra la funcion resultado")
        fo=[]
        fe=[]
        #vez = int(input("numero de aleatorios que quiere: "))
        tercia,par,doblepar,full,nada,quintilla,poker=self.pruebaestadistica(vez)
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
        print (fo)
        fe.append(0.3024)
        fe.append(0.504)
        fe.append(0.108)
        fe.append(0.072)
        fe.append(0.0092)
        fe.append(0.0045)
        fe.append(0.0001)
        print (fe)
        #vez=40
        for i in range(len(fe)):
            fe[i]=fe[i]*vez
        print (fe)
        print (fo)
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
                print (o)
                arre=numpy.zeros(o+2)
                arre1 = numpy.zeros(o + 2)
                for i in range(o+1):
                    arre[i]=fe[i]
                    arre1[i]=fo[i]
                arre[o+1]=sumafe
                arre1[o+1]=sumafo
                print (arre)
                print (arre1)
                band=False

        print("")
        print("tercia: ", tercia)
        self.resultado_FO_de_tercia.insert(0,tercia)
        print("par: ", par)
        self.resultado_FO_de_pares.insert(0,par)
        print("doblepar: ", doblepar)
        self.resultado_FO_de_dos_pares.insert(0,doblepar)
        print ("full: ", full)
        self.resultado_FO_de_full.insert(0,full)
        print("nada: ", nada)
        self.resultado_FO_de_diferentes.insert(0,nada)
        print("quintilla: ", quintilla)
        self.resultado_FO_de_quintilla.insert(0,quintilla)
        print("poker: ", poker)
        self.resultado_FO_de_poker.insert(0,poker)
        print("")
        est=0
        for i in range(len(arre1)):
            est=est+((arre1[i]-arre[i])**2/(arre[i]))
        print (est)
        self.caja_probabilidad.insert(0,est)


        #if est<18.31:
         #   messagebox.showinfo(message="Se acepta H0 cero", title="Aceptacion")
          #  messagebox.showinfo(message="SE CREO EL ARCHIVO", title="GUARDADO")
           # datos_prueba_pocket=open("numeros_prueba_poket.txt","w")
            #conversion=str(arre)
            #datos_prueba_pocket.writelines(conversion)
            #datos_prueba_pocket.close()



    def intento(self):
        print("Funcion intento")
        q=0.12435
        r=str(q)
        print (r)
        print (len(r))
        nuevo=""
        for i in range(2,len(r)):
            nuevo=nuevo+r[i]
        print (nuevo)
        f=0
        f=self.pueba(f)
        print (f)

    def pueba(self,f):
        f=f+1
        print("ESTOY EN LA FUNCION")
        return f




if __name__ == "__main__":
    obj=Metodo_pocket()