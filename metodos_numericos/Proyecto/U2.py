# -*- coding: utf-8 -*-
#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sys


class MenuUnidad2:
    def __init__(self):
        self.venUser=Toplevel()
        self.venUser.geometry("400x200")
        self.venUser.config(bg="#ffffff")
        self.venUser.config(cursor="cross")
        self.venUser.config(relief="sunken")
        self.venUser.title("Menu de Unidades")
        ancho_ventana = 1210
        alto_ventana = 600
        x_ventana = self.venUser.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.venUser.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.venUser.geometry(posicion)
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial"), width=1000,
                       height=5)
        lblEti.place(x=0, y=(0))
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial", 15), width=1000,
                       height=2)
        lblEti.place(x=0, y=(550))
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial", 15), width=1000,
                       height=2)
        lblEti.place(x=0, y=(200))
        lblEti = Label(self.venUser, text="Unidad 2: Solución de ecuaciones", fg="navy", bg="SkyBlue2",
                       font=("Arial", 36))
        lblEti.place(x=250, y=(0))
        lblSol = Label(self.venUser, text="Metodos de solucion de ecuaciones", fg="navy", bg="SkyBlue2",
                       font=("Arial", 24))
        lblSol.place(x=350, y=(50))
        #CAJAS DE TEXTO PARA SOLUCION DE ECUACIONES X, Y y Resultado
        lblx = Label(self.venUser, text="          X+              =              ", fg="navy", bg="SkyBlue2",
                       font=("Arial", 12))
        lblx.place(x=79, y=(100))
        lbly = Label(self.venUser, text="Y", fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lbly.place(x=180, y=(100))
        lblx2 = Label(self.venUser, text="          X+              =              ", fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx2.place(x=79, y=(130))
        lbly2 = Label(self.venUser, text="Y", fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lbly2.place(x=180, y=(130))
        self.Valorx1 = IntVar()
        self.Valorxn1 = Entry(self.venUser, textvariable=self.Valorx1, width=5,)
        self.Valorxn1.place(x=80, y=(102))
        self.Valory1 = IntVar()
        self.Valoryn1 = Entry(self.venUser, textvariable=self.Valory1, width=5,)
        self.Valoryn1.place(x=145, y=(102))
        self.Valorres1 = IntVar()
        self.Valorres1n = Entry(self.venUser, textvariable=self.Valorres1, width=5)
        self.Valorres1n.place(x=225, y=(102))
        self.Valorx2 = IntVar()
        self.Valorxn2 = Entry(self.venUser, textvariable=self.Valorx2, width=5)
        self.Valorxn2.place(x=80, y=(132))
        self.Valory2 = IntVar()
        self.Valoryn2 = Entry(self.venUser, textvariable=self.Valory2, width=5)
        self.Valoryn2.place(x=145, y=(132))
        self.Valorres2 = IntVar()
        self.Valorres2n = Entry(self.venUser, textvariable=self.Valorres2, width=5)
        self.Valorres2n.place(x=225, y=(132))
        #METODOS CON INTERVALOS
        lblSol = Label(self.venUser, text="Metodos de Intervalo", fg="navy", bg="SkyBlue2",
                       font=("Arial", 24))
        lblInt = Label(self.venUser, text="Intervalos=          a                Tolerancia               ", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblSol.place(x=450, y=(200))
        lblInt.place(x=0, y=(252))
        self.IntINF = IntVar()
        self.IntINFe = Entry(self.venUser, textvariable=self.IntINF, width=5, )
        self.IntINFe.place(x=100, y=(257))
        self.IntSUP = IntVar()
        self.IntSUPn = Entry(self.venUser, textvariable=self.IntSUP, width=5, )
        self.IntSUPn.place(x=175, y=(257))
        self.IntTol = DoubleVar()
        self.IntTole = Entry(self.venUser, textvariable=self.IntTol, width=5, )
        self.IntTole.place(x=350, y=(257))
        lblSupExp = Label(self.venUser, text="Adecua la expresion a tu problema:      e^(      x)+      cos(      x)+      sen(      x)+       x^       +       x^       +       x^       +       x^       +        =0", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblSupExp.place(x=0, y=(280))
        self.Prode = IntVar()
        self.Proden = Entry(self.venUser, textvariable=self.Prode, width=4, )
        self.Proden.place(x=300, y=(285))
        self.Expe = IntVar()
        self.Expen = Entry(self.venUser, textvariable=self.Expe, width=4, )
        self.Expen.place(x=355, y=(285))
        self.Pcos = IntVar()
        self.Pcosn = Entry(self.venUser, textvariable=self.Pcos, width=4, )
        self.Pcosn.place(x=410, y=(285))
        self.Pcosx = IntVar()
        self.Pcosxn = Entry(self.venUser, textvariable=self.Pcosx, width=4, )
        self.Pcosxn.place(x=477, y=(285))
        self.Psen = IntVar()
        self.Psenn = Entry(self.venUser, textvariable=self.Psen, width=4, )
        self.Psenn.place(x=535, y=(285))
        self.Psenx = IntVar()
        self.Psenxn = Entry(self.venUser, textvariable=self.Psenx, width=4, )
        self.Psenxn.place(x=600, y=(285))
        self.Px = IntVar()
        self.Pxn = Entry(self.venUser, textvariable=self.Px, width=4, )
        self.Pxn.place(x=660, y=(285))
        self.Ex = IntVar()
        self.Exn = Entry(self.venUser, textvariable=self.Ex, width=4, )
        self.Exn.place(x=710, y=(285))
        self.Px2 = IntVar()
        self.Pxn2 = Entry(self.venUser, textvariable=self.Px2, width=4, )
        self.Pxn2.place(x=755, y=(285))
        self.Ex2 = IntVar()
        self.Exn2 = Entry(self.venUser, textvariable=self.Ex2, width=4, )
        self.Exn2.place(x=810, y=(285))
        self.Px3 = IntVar()
        self.Pxn3 = Entry(self.venUser, textvariable=self.Px3, width=4, )
        self.Pxn3.place(x=855, y=(285))
        self.Ex3 = IntVar()
        self.Exn3 = Entry(self.venUser, textvariable=self.Ex3, width=4, )
        self.Exn3.place(x=905, y=(285))
        self.Px4 = IntVar()
        self.Pxn4 = Entry(self.venUser, textvariable=self.Px4, width=4, )
        self.Pxn4.place(x=950, y=(285))
        self.Ex4 = IntVar()
        self.Exn4 = Entry(self.venUser, textvariable=self.Ex4, width=4, )
        self.Exn4.place(x=1000, y=(285))
        self.num = IntVar()
        self.numn = Entry(self.venUser, textvariable=self.num, width=4, )
        self.numn.place(x=1050, y=(285))
        #COMBOBOX
        self.comboExample = ttk.Combobox(self.venUser,values=["Metodo de Sustitucion","Metodo de Reduccion","Metodo de Igualacion","Metodo Grafico"],state="readonly")
        self.comboExample.place(x=280, y=(115))
        self.comboExample.bind("<<ComboboxSelected>>", self.Eleccion_metodo_resolverE)
        self.comboIntervalos = ttk.Combobox(self.venUser,
                                         values=["Metodo de Intervalo", "Metodo de biseccion", "Metodo de aproximaciones sucesivas","Falsa Posicion",
                                                 "Metodo Grafico"], state="readonly")
        self.comboIntervalos.place(x=520, y=(257))
        self.comboIntervalos.bind("<<ComboboxSelected>>", self.Eleccion_metodo_resolverE)
        #btnIniciarRE = Button(self.venUser, text="Salir", bg='grey', command=self.Eleccion_metodo_resolverE)
        #btnIniciarRE.place(x=205, y=150)
        btnSalir = Button(self.venUser, text="Salir", bg='grey', command=self.pafuera,width=20,height=2)
        btnSalir.place(x=550, y=550)
        height = 5
        self.venUser.mainloop()


    def pafuera(self):
        sys.exit(1)
    def Eleccion_metodo_resolverE(self,event):
        lblx = Label(self.venUser, fg="navy", bg="#ffffff",
                     font=("Arial", 12),width=1000,height=3)
        lblx.place(x=479, y=(100))
        lblRaiz = Label(self.venUser, text="                                                                         ", fg="navy",
                        bg="SkyBlue2",
                        font=("Arial", 14))
        lblRaiz.place(x=700, y=(252))
        if self.comboExample.get()=="Metodo de Sustitucion":
            self.metodo_sustitucion()
        if self.comboExample.get()=="Metodo de Reduccion":
            self.metodo_reduccion()
        if self.comboExample.get()=="Metodo de Igualacion":
            self.metodos_igualacion()
        if self.comboExample.get()=="Metodo Grafico":
            self.metodo_grafico()
        if self.comboIntervalos.get()=="Metodo Grafico":
            self.metodo_grafico_intervalos()
        if self.comboIntervalos.get()=="Metodo de biseccion":
            self.metodo_biseccion()
        if self.comboIntervalos.get() == "Metodo de aproximaciones sucesivas":
            self.AproximacionesSucesivas()
        if self.comboIntervalos.get() == "Falsa Posicion":
            self.interpolacion()
    def metodo_sustitucion(self):
        x1,y1,res1 = int(self.Valorxn1.get()), int(self.Valoryn1.get()), int(self.Valorres1n.get())
        x2, y2, res2 = int(self.Valorxn2.get()), int(self.Valoryn2.get()), int(self.Valorres2n.get())
        textDespeje="Despeje :X=( "+str(res1)+"+("+str(-1*(y1))+")Y)/"+str(x1)
        textSustitucion="Sustitucion :"+str(x2)+"("+str(res1)+"+("+str(-1*(y1))+"Y))/"+str(x1)+")+("+str(y2)+")Y= "+ str(res2)
        y3=x2*(-1*(y1))/x1
        res3=x2*((res1))/x1
        textSustitucion2="("+str(y3)+"Y+("+str(res3)+"))+("+str(y2)+")Y= "+str(res2)
        textSustitucion3 = str(y3+y2)+"Y="+str(res2-res3)
        textSustitucion4="Y="+str((res2-res3)/(y3+y2))
        soly=((res2-res3)/(y3+y2))
        solx=(res1-y1*soly)/x1
        textSolucion="X="+str(solx)
        lblx = Label(self.venUser, text=(textDespeje), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=479, y=(100))
        lblx = Label(self.venUser, text=textSustitucion, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=479, y=(130))
        lblx = Label(self.venUser, text=textSustitucion2, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(100))
        lblx = Label(self.venUser, text=textSustitucion3, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(130))
        lblx = Label(self.venUser, text=textSustitucion4, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=950, y=(100))
        lblx = Label(self.venUser, text=textSolucion, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=950, y=(130))

    def metodo_reduccion(self):
        x1, y1, res1 = int(self.Valorxn1.get()), int(self.Valoryn1.get()), int(self.Valorres1n.get())
        x2, y2, res2 = int(self.Valorxn2.get()), int(self.Valoryn2.get()), int(self.Valorres2n.get())
        if x1<x2:
            if x1>0:
                redArriba=str(-1*x2)+"("+str(x1)+"X+("+str(y1)+"Y)="+str(res1)+")"
                redAbajo=str(x1)+"("+str(x2)+"X+("+str(y2)+"Y)="+str(res2)+")"
                redArriba1 = str(x1*-x2) + "X+(" + str(y1*-x2) + "Y)=" + str(res1*-x2)
                redAbajo1 = str(x2*x1) + "X+(" + str(y2*x1) + "Y)=" + str(res2*x1)
                redRes=str(x2+(x1*-x2)) + "X+(" + str(y2+(y1*-x2)) + "Y)=" + str(res2+(res1*-x2))
                soly = (res2*x1+(res1*-x2)) / (y2*x1+(y1*-x2))
                solx = (res1 - y1*soly) / x1
                textSustitucion4 = "Y=" + str(soly)
                textSolucion = "X=" + str(solx)
            else:
                print ("hola")
                redArriba = str(x2) + "(" + str(x1) + "X+(" + str(y1) + "Y)=" + str(res1) + ")"
                redAbajo = str(x2) + "X+(" + str(y2) + "Y)=" + str(res2)
                redArriba1 = str(x1 * x2) + "X+(" + str(y1 * x2) + "Y)=" + str(res1 * x2)
                redAbajo1 = str(x2*-x1) + "X+(" + str(y2*-x1) + "Y)=" + str(res2*-x1)
                redRes = str(x2*-x1 + (x1 * x2)) + "X+(" + str(y2*-x1 + (y1 * x2)) + "Y)=" + str(res2*-x1 + (res1 * x2))
                soly = (res2*-x1 + (res1 * x2)) / (y2*-x1 + (y1 * x2))
                solx = (res1 - y1*soly) / x1
                textSustitucion4 = "Y=" + str(soly)
                textSolucion = "X=" + str(solx)
        else:
            if x2>0:
                redArriba = str(x1) + "X+(" + str(y1) + "Y)=" + str(res1)
                redAbajo = str(-1*x1)+"("+str(x2)+"X+("+str(y2)+"Y)="+str(res2)+")"
                redArriba1 = str(x1) + "X+(" + str(y1) + "Y)=" + str(res1)
                redAbajo1 = str(x2*-x1) + "X+(" + str(y2*-x1) + "Y)=" + str(res2*-x1)
                redRes =str(x1+(x2*-x1)) + "X+(" + str(y1+(y2*-x1)) + "Y)=" + str(res1+(res2*-x1))
                soly = (res1+(res2*-x1))/(y1+(y2*-x1))
                solx = (res1 - y1*soly) / x1
                textSustitucion4 = "Y=" + str(soly)
                textSolucion = "X=" + str(solx)
            else:
                redArriba = str(x1) + "X+(" + str(y1) + "Y)=" + str(res1)
                redAbajo = str(x1) + "(" + str(x2) + "X+(" + str(y2) + "Y)=" + str(res2) + ")"
                redArriba1 = str(x1) + "X+(" + str(y1) + "Y)=" + str(res1)
                redAbajo1 = str(x2 * x1) + "X+(" + str(y2 * x1) + "Y)=" + str(res2 * x1)
                redRes = str(x1 + (x2 * x1)) + "X+(" + str(y1 + (y2 * x1)) + "Y)=" + str(res1 + (res2 * x1))
                soly = (res1 + (res2 * x1)) / (y1 + (y2 * x1))
                solx = (res1 - y1*soly) / x1
                textSustitucion4 = "Y=" + str(soly)
                textSolucion = "X=" + str(solx)
        lblx = Label(self.venUser, text=(redArriba), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=479, y=(100))
        lblx = Label(self.venUser, text=redAbajo, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=479, y=(130))
        lblx = Label(self.venUser, text=(redArriba1), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(100))
        lblx = Label(self.venUser, text=redAbajo1, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(130))
        lblx = Label(self.venUser, text=redRes, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(160))
        lblx = Label(self.venUser, text=textSustitucion4, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=950, y=(100))
        lblx = Label(self.venUser, text=textSolucion, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=950, y=(130))
    def metodos_igualacion(self):
        x1, y1, res1 = int(self.Valorxn1.get()), int(self.Valoryn1.get()), int(self.Valorres1n.get())
        x2, y2, res2 = int(self.Valorxn2.get()), int(self.Valoryn2.get()), int(self.Valorres2n.get())
        textDespeje1 = "Despeje 1:X=( " + str(res1) + "+(" + str(-1 * (y1)) + ")Y)/" + str(x1)
        textDespeje2 = "Despeje 1:X=( " + str(res2) + "+(" + str(-1 * (y2)) + ")Y)/" + str(x2)
        textdepeje3="("+str("{:.3f}".format(-1 * (y2/x2)))+"+("+str("{:.3f}".format((y1/x1))) + "))Y="+str("{:.3f}".format(res1/x1))+"+("+str("{:.3f}".format((-1*res2)/x2))+")"
        igualacion="("+str(res2) + "+(" + str(-1 * (y2)) + ")Y)/" + str(x2)+"=("+ str(res1) + "+(" + str(-1 * (y1)) + ")Y)/" + str(x1)
        textsoly=str("{:.3f}".format((-1 * (y2/x2))+((y1/x1))))+"Y="+str("{:.3f}".format(((res1/x1)+((-1*res2)/x2))))
        soly=(((res1/x1)+((-1*res2)/x2)))/((-1 * (y2/x2))+((y1/x1)))
        solx=(res1 - y1*soly) / x1
        textSustitucion4 = "Y=" + str("{:.3f}".format(soly))
        textSolucion = "X=" + str("{:.3f}".format(solx))
        lblx = Label(self.venUser, text=(textDespeje1), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=479, y=(100))
        lblx = Label(self.venUser, text=textDespeje2, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=479, y=(130))
        lblx = Label(self.venUser, text=(igualacion), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(100))
        lblx = Label(self.venUser, text=(textdepeje3), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(130))
        lblx = Label(self.venUser, text=textsoly, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=750, y=(160))
        lblx = Label(self.venUser, text=textSustitucion4, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=1050, y=(100))
        lblx = Label(self.venUser, text=textSolucion, fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=1050, y=(130))
    def metodo_grafico(self):
        x1, y1, res1,IntInf,IntSup = int(self.Valorxn1.get()), int(self.Valoryn1.get()), int(self.Valorres1n.get()),int(self.IntINFe.get()),int(self.IntSUPn.get())
        x2, y2, res2 = int(self.Valorxn2.get()), int(self.Valoryn2.get()), int(self.Valorres2n.get())
        x = np.arange(IntInf,IntSup,0.1)
        funy1=(res1-(x1*x))/y1
        funy2=(res2-(x2*x))/y2
        plt.plot(x, funy1)
        plt.plot(x, funy2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Método Gráfico')
        plt.grid()
        plt.show()
    def fx(self,x):
        IntInf, IntSup, Factore, Expoe, Pcosx, Ecosx = float(self.IntINFe.get()), float(self.IntSUPn.get()), int(
            self.Proden.get()), int(self.Expen.get()), int(self.Pcosn.get()), int(self.Pcosx.get())
        Psenx, Psennx, Px, Ex, Px2, Ex2 = int(self.Psenn.get()), int(self.Psenxn.get()), int(self.Pxn.get()), int(
            self.Exn.get()), int(self.Pxn2.get()), int(self.Exn2.get())
        Px3, Ex3, Px4, Ex4, num = int(self.Pxn3.get()), int(self.Exn3.get()), int(self.Pxn4.get()), int(
            self.Exn4.get()), int(self.numn.get())
        return (Factore*np.exp(x*Expoe))+(Pcosx*np.cos(x*Ecosx))+(Psenx*np.sin(x*Psennx))+(Px*x**Ex)+(Px2*x**Ex2)+(Px3*x**Ex3)+(Px4*x**Ex4)+num
    def gx(self,x):
        IntInf, IntSup, Factore, Expoe, Pcosx, Ecosx = float(self.IntINFe.get()), float(self.IntSUPn.get()), int(
            self.Proden.get()), int(self.Expen.get()), int(self.Pcosn.get()), int(self.Pcosx.get())
        Psenx, Psennx, Px, Ex, Px2, Ex2 = int(self.Psenn.get()), int(self.Psenxn.get()), int(self.Pxn.get()), int(
            self.Exn.get()), int(self.Pxn2.get()), int(self.Exn2.get())
        Px3, Ex3, Px4, Ex4, num = int(self.Pxn3.get()), int(self.Exn3.get()), int(self.Pxn4.get()), int(
            self.Exn4.get()), int(self.numn.get())
        return (Factore * np.exp(x * Expoe)) + (Pcosx * np.cos(x * Ecosx)) + (Psenx * np.sin(x * Psennx)) + (
                    Px * x ** Ex) + (Px2 * x ** Ex2) + (Px3 * x ** Ex3) + (Px4 * x ** Ex4) + num+x
    def metodo_grafico_intervalos(self):
        IntInf, IntSup=int(self.IntINFe.get()), int(self.IntSUPn.get())
        a=np.zeros((7,2))
        tabla=Frame(self.venUser,width=480,height=235)
        tabla.place(x=300,y=310)
        tree = ttk.Treeview(tabla, columns=(1, 2), height=5, show="headings")
        tree.pack(side='left')
        tree.heading(1, text="X")
        tree.heading(2, text="F(x)")
        scroll = ttk.Scrollbar(tabla, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        #print (a)
        s=((IntSup-IntInf)/5)

        a[0, 0] = IntInf
        a[0,1]=self.fx(IntInf)
        l=s
        print(IntInf,s,l)
        for i in range(1,7):

            if s>IntSup:
                a[i, 0] =IntInf+s
            s += l
        for i in range(1,7):
            x=a[i,0]
            a[i,1]=self.fx(x)
        for val in a:
            tree.insert('', 'end', values=(val[0], val[1]))
        x = np.arange(IntInf, IntSup, 0.1)
        xi=0
        plt.plot(x, self.fx(x))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axvline(xi,label='f(x)=0,x={xi:.6f}',color='k')
        plt.axhline(0,color='k')
        plt.title('Método Gráfico')
        plt.grid()
        plt.show()
        #print(a)
    def metodo_biseccion(self):
        IntInf, IntSup,Tol=int(self.IntINFe.get()), int(self.IntSUPn.get()),float(self.IntTole.get())
        xl,xu,a=IntInf,IntSup,np.zeros((100,6))
        print (Tol)
        ea=100
        xra=0
        conta=1
        while abs(ea)>Tol and conta<99:
            xr=(xl+xu)/2
            a[conta,0],a[conta,1],a[conta,2],a[conta,3]=conta,xl,xu,xr
            fxl=self.fx(xl)
            fxr=self.fx(xr)
            if (fxl*fxr)<0:
                xu=xr
            if(fxl*fxr)>0:
                xl=xr
            if (fxl*fxr)==0:
                break
            ea=abs(((xr-xra)/xr)*100)
            a[conta, 4]=ea
            xra=xr
            conta+=1
            #if abs(ea)<Tol:
                #break
            if conta>98:
                break
        col=0
        for i in range(100):
            if a[i,0]!=0:
                col+=1
        tabla = Frame(self.venUser, width=480, height=235)
        tabla.place(x=3, y=310)
        tabla.grid_propagate(False)
        tree = ttk.Treeview(tabla, columns=(1, 2, 3, 4, 5, 6), height=10, show="headings")
        tree.pack(side='left')
        tree.heading(1, text="Iteracion")
        tree.heading(2, text="Xl")
        tree.heading(3, text="Xu")
        tree.heading(4, text="Xr")
        tree.heading(5, text="Ea(%)")
        tree.heading(6, text="Et(%)")
        scroll = ttk.Scrollbar(tabla, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        for val in a:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5]))
        lblRaiz = Label(self.venUser, text="Raiz"+str(xr), fg="navy",
                       bg="SkyBlue2",
                       font=("Arial", 14))
        lblRaiz.place(x=900, y=(252))
    def AproximacionesSucesivas(self):
        IntInf, IntSup, Tol = float(self.IntINFe.get()), float(self.IntSUPn.get()), float(self.IntTole.get())
        xi, a, i = IntInf, np.zeros((100, 5)), 0
        error=np.abs(self.gx(xi)-xi)
        while error>Tol and i<99:
            a[i, 0], a[i, 1], a[i, 2], a[i, 3], a[i, 4] = i, xi,self.fx(xi),self.gx(xi), error
            if i>0:
                error = np.abs(self.gx(xi) - xi)
            xi=(self.gx(xi))
            i+=1
        tabla = Frame(self.venUser, width=480, height=235)
        tabla.place(x=3, y=310)
        tabla.grid_propagate(False)
        tree = ttk.Treeview(tabla, columns=(1, 2, 3, 4, 5), height=10, show="headings")
        tree.pack(side='left')
        tree.heading(1, text="Iteracion")
        tree.heading(2, text="xi")
        tree.heading(3, text="fx(xi)")
        tree.heading(4, text="gx(xi)")
        tree.heading(5, text="Error(%)")
        scroll = ttk.Scrollbar(tabla, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        for val in a:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4]))
        lblRaiz = Label(self.venUser, text="Raiz" + str(xi), fg="navy",
                        bg="SkyBlue2",
                        font=("Arial", 14))
        lblRaiz.place(x=900, y=(252))
        x=np.linspace(IntInf,IntSup,100)
        plt.title('Metodo del punto fijo o aproximaciones sucesivas')
        plt.plot(x,self.fx(x),label='f(x)')
        plt.plot(x, self.gx(x), label='g(x)')
        plt.plot(x,x,label='f(x)=x')
        plt.axvline(xi, label='f(x)=0,x={xi:.6f}', color='k')
        plt.axhline(0, color='k')
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
    def interpolacion(self):
        IntInf, IntSup, Tol = float(self.IntINFe.get()), float(self.IntSUPn.get()), float(self.IntTole.get())
        a, b, arre = IntInf, IntSup, np.zeros((100, 6))
        tramo=abs(b-a)
        while not(tramo<=Tol):
            fa=self.fx(a)
            fb=self.fx(b)
            print (fa,fb)
            c=b-fb*(a-b)/(fa-fb)
            fc=self.fx(c)
            cambio=np.sign(fa)*np.sign(fc)
            if cambio>0:
                tramo=abs(c-a)
                a=c
            else:
                tramo=abs(b-c)
                b=c
        lblRaiz = Label(self.venUser, text="Raiz" + str(c)+" tramo="+str(tramo), fg="navy",
                        bg="SkyBlue2",
                        font=("Arial", 14))
        lblRaiz.place(x=700, y=(252))

