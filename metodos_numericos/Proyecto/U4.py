#   Codigo para que se acepten caracteres especiales
# -*- coding: utf-8 -*-
#!/usr/bin/env python
#librerias necesarias Tkinter es la interfaz grafica
from tkinter import *
#from ttk import Combobox,Treeview
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sys


class MenuUnidad4:
    #Se crea un constructor
    def __init__(self):
        self.venUser=Toplevel() #Esta linea da a saber que es una ventana secundaria
        self.venUser.config(bg="#ffffff") #color de fondo
        self.venUser.config(cursor="cross")
        self.venUser.config(relief="sunken")
        self.venUser.title("Métodos de Derivada e Integración") #titulo de la ventana
        ancho_ventana = 1210 #Medidas del ancho
        alto_ventana = 600 #Medidas del largo
        x_ventana = self.venUser.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.venUser.winfo_screenheight() // 2 - alto_ventana // 2
        #Codigo para centrar la ventana
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.venUser.geometry(posicion)
        #Etiquetas para los banners azules
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial"), width=1000,height=5)
        lblEti.place(x=0, y=(0))

        #Texto de la ventana
        lblEti = Label(self.venUser, text="Unidad 4: Métodos de Derivación e Integración", fg="navy", bg="SkyBlue2",
                       font=("Arial", 36))
        lblEti.place(x=100, y=(0))
        #Etiquetas para pedir valores
        lblInt = Label(self.venUser, text="Valor de x=         Valor de h=                                         Decremento               ", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblInt.place(x=0, y=(67))
        #Cajas de texto que reciben los valores ingresados x,h y tolerancia
        self.x = DoubleVar()
        self.xn = Entry(self.venUser, textvariable=self.x, width=5, )
        self.xn.place(x=100, y=(72))
        self.h = DoubleVar()
        self.hn = Entry(self.venUser, textvariable=self.h, width=5, )
        self.hn.place(x=242, y=(72))
        self.IntTol = DoubleVar()
        self.IntTole = Entry(self.venUser, textvariable=self.IntTol, width=5, )
        self.IntTole.place(x=550, y=(72))
        #Etiqueta para referencia de la superformula
        lblSupExp = Label(self.venUser, text="Adecua la expresion a tu problema:       x^       +       x^       +       x^       +       x^       +       x^       +        +      xe^(      x)=0", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblSupExp.place(x=0, y=(90))
        #Cajas de texto para recibir valores de la superfomula
        self.Fx1 = DoubleVar()
        self.Fx1n = Entry(self.venUser, textvariable=self.Fx1, width=4, )
        self.Fx1n.place(x=303, y=(95))
        self.Ex1 = DoubleVar()
        self.Ex1n = Entry(self.venUser, textvariable=self.Ex1, width=4, )
        self.Ex1n.place(x=355, y=(95))
        self.Fx2 = DoubleVar()
        self.Fx2n = Entry(self.venUser, textvariable=self.Fx2, width=4, )
        self.Fx2n.place(x=400, y=(95))
        self.Ex2 = DoubleVar()
        self.Ex2n = Entry(self.venUser, textvariable=self.Ex2, width=4, )
        self.Ex2n.place(x=450, y=(95))
        self.Fx3 = DoubleVar()
        self.Fx3n = Entry(self.venUser, textvariable=self.Fx3, width=4, )
        self.Fx3n.place(x=498, y=(95))
        self.Ex3 = DoubleVar()
        self.Ex3n = Entry(self.venUser, textvariable=self.Ex3, width=4, )
        self.Ex3n.place(x=548, y=(95))
        self.Fx4 = DoubleVar()
        self.Fx4n = Entry(self.venUser, textvariable=self.Fx4, width=4, )
        self.Fx4n.place(x=595, y=(95))
        self.Ex4 = DoubleVar()
        self.Ex4n = Entry(self.venUser, textvariable=self.Ex4, width=4, )
        self.Ex4n.place(x=648, y=(95))
        self.Fx5 = DoubleVar()
        self.Fx5n = Entry(self.venUser, textvariable=self.Fx5, width=4, )
        self.Fx5n.place(x=690, y=(95))
        self.Ex5 = DoubleVar()
        self.Ex5n = Entry(self.venUser, textvariable=self.Ex5, width=4, )
        self.Ex5n.place(x=740, y=(95))
        self.num =DoubleVar()
        self.numn = Entry(self.venUser, textvariable=self.num, width=4, )
        self.numn.place(x=792, y=(95))
        self.Pe = DoubleVar()
        self.Pen = Entry(self.venUser, textvariable=self.Pe, width=4, )
        self.Pen.place(x=838, y=(95))
        self.Ee = DoubleVar()
        self.Een = Entry(self.venUser, textvariable=self.Ee, width=4, )
        self.Een.place(x=890, y=(95))
        #Cajas de texto para intervalos desiguales
        lblSupExp = Label(self.venUser,
                          text="X                                                                                                                      ",
                          fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(115))
        self.Intervalo = DoubleVar()
        self.Intervalon = Entry(self.venUser, textvariable=self.Intervalo, width=4, )
        self.Intervalon.place(x=30, y=(120))
        self.Intervalo2 = DoubleVar()
        self.Intervalo2n = Entry(self.venUser, textvariable=self.Intervalo2, width=4, )
        self.Intervalo2n.place(x=60, y=(120))
        self.Intervalo3 = DoubleVar()
        self.Intervalo3n = Entry(self.venUser, textvariable=self.Intervalo3, width=4, )
        self.Intervalo3n.place(x=90, y=(120))
        self.Intervalo4 = DoubleVar()
        self.Intervalo4n = Entry(self.venUser, textvariable=self.Intervalo4, width=4, )
        self.Intervalo4n.place(x=120, y=(120))
        self.Intervalo5 = DoubleVar()
        self.Intervalo5n = Entry(self.venUser, textvariable=self.Intervalo5, width=4, )
        self.Intervalo5n.place(x=150, y=(120))
        self.Intervalo6 = DoubleVar()
        self.Intervalo6n = Entry(self.venUser, textvariable=self.Intervalo6, width=4, )
        self.Intervalo6n.place(x=180, y=(120))
        self.Intervalo7 = DoubleVar()
        self.Intervalo7n = Entry(self.venUser, textvariable=self.Intervalo7, width=4, )
        self.Intervalo7n.place(x=210, y=(120))
        self.Intervalo8 = DoubleVar()
        self.Intervalo8n = Entry(self.venUser, textvariable=self.Intervalo8, width=4, )
        self.Intervalo8n.place(x=240, y=(120))
        self.Intervalo9 = DoubleVar()
        self.Intervalo9n = Entry(self.venUser, textvariable=self.Intervalo9, width=4, )
        self.Intervalo9n.place(x=270, y=(120))
        self.Intervalo10 = DoubleVar()
        self.Intervalo10n = Entry(self.venUser, textvariable=self.Intervalo10, width=4, )
        self.Intervalo10n.place(x=300, y=(120))
        self.Intervalo11 = DoubleVar()
        self.Intervalo11n = Entry(self.venUser, textvariable=self.Intervalo11, width=4, )
        self.Intervalo11n.place(x=330, y=(120))
        #COMBOBOX
        self.comboExample = ttk.Combobox(self.venUser,values=["Método de Derivacion","Método del trapecio","Método Simpson 1/3","Método Simpson 3/8","Intervalos desiguales","Formula de tres puntos","Formula de cinco puntos","Cuadratura Gaussiana","         "],state="readonly",width=30)
        self.comboExample.place(x=850, y=(72))
        self.comboExample.bind("<<ComboboxSelected>>", self.Eleccion_metodo_resolverE)

        btnSalir = Button(self.venUser, text="Salir", bg='grey', command=self.pafuera,width=20,height=2)
        btnSalir.place(x=550, y=550)
        height = 5
        self.venUser.mainloop()

    def Eleccion_metodo_resolverE(self,event):
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                     font=("Arial", 12))
        lblx.place(x=0, y=(200))
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                      font=("Arial", 12))
        lblx.place(x=0, y=(225))
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                     font=("Arial", 12))
        lblx.place(x=0, y=(250))
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                     font=("Arial", 12))
        lblx.place(x=0, y=(275))
        if self.comboExample.get()=="Método de Derivacion":
            self.MetodoDerivativo()
        if self.comboExample.get()=="Método del trapecio":
            self.MetodoTrapecio()
        if self.comboExample.get()=="Método Simpson 1/3":
            self.MetodoSimpson13()
        if self.comboExample.get()=="Método Simpson 3/8":
            self.MetodoSimpson38()
        if self.comboExample.get()=="Intervalos desiguales":
            self.IntervalosIrregulares()
        if self.comboExample.get()=="Formula de tres puntos":
            self.Formula3puntos()
        if self.comboExample.get()=="Formula de cinco puntos":
            self.Formula5puntos()
        if self.comboExample.get()=="Cuadratura Gaussiana":
            self.CuadraturaGaussiana()
    #Funcion para el calculo de xi o f(a) para metodo de trapecio
    def fxi(self,x):
        Fx1, Ex1, Fx2, Ex2, Fx3, Ex3, Fx4, Ex4 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fx2n.get()), float(self.Ex2n.get()), float(self.Fx3n.get()), float(self.Ex3n.get()), float(
            self.Fx4n.get()), float(self.Ex4n.get())
        Fx5, Ex5, num = float(self.Fx5n.get()), float(self.Ex5n.get()), float(self.numn.get())
        Factore, Expoe = float(self.Pen.get()), float(self.Een.get())
        return Fx1*x**Ex1+Fx2*x**Ex2+Fx3*x**Ex3+Fx4*x**Ex4+Fx5*x**Ex5+num+(Factore*x*np.exp(x*Expoe))

    # Funcion para el calculo de xi+1 o f(b) para metodo de trapecio
    def fxi1(self,x):
        Fx1, Ex1, Fx2, Ex2, Fx3, Ex3, Fx4, Ex4 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fx2n.get()), float(self.Ex2n.get()), float(self.Fx3n.get()), float(self.Ex3n.get()), float(
            self.Fx4n.get()), float(self.Ex4n.get())
        Fx5, Ex5, num = float(self.Fx5n.get()), float(self.Ex5n.get()), float(self.numn.get())
        Factore,Expoe=float(self.Pen.get()), float(self.Een.get())
        return Fx1*x**Ex1+Fx2*x**Ex2+Fx3*x**Ex3+Fx4*x**Ex4+Fx5*x**Ex5+num+(Factore*x*np.exp(x*Expoe))

    # Funcion para el calculo de la derivada f(x)
    def derivadafx(self,x):
        Fx1, Ex1, Fx2, Ex2, Fx3, Ex3, Fx4, Ex4 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fx2n.get()), float(self.Ex2n.get()), float(self.Fx3n.get()), float(self.Ex3n.get()), float(
            self.Fx4n.get()), float(self.Ex4n.get())
        Fx5, Ex5, num = float(self.Fx5n.get()), float(self.Ex5n.get()), float(self.numn.get())
        Factore, Expoe = float(self.Pen.get()), float(self.Een.get())
        return Ex1*Fx1*x**(Ex1-1)+Ex2*Fx2*x**(Ex2-1)+Ex3*Fx3*x**(Ex3-1)+Ex4*Fx4*x**(Ex4-1)+Ex5*Fx5*x**(Ex5-1)+(Expoe*Factore*np.exp(x*Expoe))+(Expoe*Factore*x*np.exp(x*Expoe))

    def MetodoDerivativo(self):
        #Recibo valores
        x,h,decremento=float(self.xn.get()),float(self.hn.get()),float(self.IntTole.get())
        #determino el numero de iteraciones enteras de mi aumento y mi disminucion
        iteraciones=int(h/decremento)
        Tabla=np.zeros((iteraciones,8))
        conta=0
        while h>0:
            Tabla[conta][0]=h
            Tabla[conta][1] =x
            xi1 = x + h
            Tabla[conta][2] =x+h
            fx=self.fxi(x)
            fxi = self.fxi1(xi1)
            Tabla[conta][3] = "{:.3f}".format(fx)
            Tabla[conta][4] = "{:.3f}".format(fxi)

            print ("{:.3f}".format(fx),"{:.3f}".format(fxi))
            dfx=(fxi-fx)/h
            derfx=self.derivadafx(x)
            Tabla[conta][5] = derfx
            Tabla[conta][6] = derfx
            print (dfx)
            print (derfx)
            error=(abs(derfx-dfx)/derfx)*100
            Tabla[conta][7] = error
            conta+=1
            h-=decremento
        #Creo un frame para poner la tabla en la que muestro mis iteraciones
        tablaframe = Frame(self.venUser, width=480, height=235)
        tablaframe.place(x=3, y=310)
        tablaframe.grid_propagate(False)
        #Utilizo un Treeview para poner la tabla, esta lineas son de configuracion
        tree = ttk.Treeview(tablaframe, columns=(1, 2, 3, 4, 5, 6, 7, 8), height=10, show="headings")
        tree.pack(side='left')
        tree.column('#1', width=100, anchor='c')
        tree.column('#2', width=100, anchor='c')
        tree.column('#3', width=100, anchor='c')
        tree.column('#4', width=100, anchor='c')
        tree.column('#5', width=100, anchor='c')
        tree.column('#6', width=100, anchor='c')
        tree.column('#7', width=100, anchor='c')
        tree.column('#8', width=100, anchor='c')
        tree.heading(1, text="h")
        tree.heading(2, text="xi")
        tree.heading(3, text="xi+1")
        tree.heading(4, text="f(xi)")
        tree.heading(5, text="f(xi+1)")
        tree.heading(6, text="f'(xi)")
        tree.heading(7, text="f'(xi)real")
        tree.heading(8, text="error")
        scroll = ttk.Scrollbar(tablaframe, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        #con la matriz creada anteriormente lleno el treeview
        for val in Tabla:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]))
    #Fucion para obtener la integral de f(x)
    def Integral(self,h,x):
        Fx1, Ex1, Fx2, Ex2, Fx3, Ex3, Fx4, Ex4 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fx2n.get()), float(self.Ex2n.get()), float(self.Fx3n.get()), float(self.Ex3n.get()), float(
            self.Fx4n.get()), float(self.Ex4n.get())
        Fx5, Ex5, num = float(self.Fx5n.get()), float(self.Ex5n.get()), float(self.numn.get())
        sup=((Fx1*h**(Ex1+1))/(Ex1+1))+((Fx2*h**(Ex2+1))/(Ex2+1))+((Fx3*h**(Ex3+1))/(Ex3+1))+((Fx4*h**(Ex4+1))/(Ex4+1))+((Fx5*h**(Ex5+1))/(Ex5+1))+num*h
        #print (sup)
        inf=((Fx1*x**(Ex1+1))/(Ex1+1))+((Fx2*x**(Ex2+1))/(Ex2+1))+((Fx3*x**(Ex3+1))/(Ex3+1))+((Fx4*x**(Ex4+1))/(Ex4+1))+((Fx5*x**(Ex5+1))/(Ex5+1))+num*x
        #print(inf)
        return sup-inf
    #Funcion para hacer el metodo del trapecio
    def MetodoTrapecio(self):
        #recibo a y b en este caso x y h
        x, h= float(self.xn.get()), float(self.hn.get())
        #resuelve fxi y fxi+1
        fa=self.fxi(x)
        fb=self.fxi1(h)
        print (fa,fb)
        I=(h-x)*((fa+fb)/2)
        #resolvemos la integral analiticamente
        IntegralReal=self.Integral(h,x)
        error = (abs(IntegralReal - I) / IntegralReal) * 100
        print (I,IntegralReal,error)
        lblx = Label(self.venUser, text="Resultado= " + str("{:.3f}".format(I)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(200))
        lblx = Label(self.venUser, text="Integral Analitica= " + str("{:.3f}".format(IntegralReal)), fg="navy",
                     bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(225))
        lblx = Label(self.venUser, text="Error= " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(250))
    def MetodoSimpson13(self):
        #obtenemos los limites de la ventana
        a, b = float(self.xn.get()), float(self.hn.get())
        #obtenemos h
        h=(a+b)/2
        #calculamos los diferentes x a trabajar
        x0=a
        x1=a+h
        x2=x1+h
        #Determinamos fx0,fx1,fx2
        fx0=self.fxi(x0)
        fx1 = self.fxi(x1)
        fx2 = self.fxi(x2)
        #print (fx0)
        #print(fx1)
        #print(fx2)
        #Obtenemos el valor segun formula
        I=(h/3)*(fx0+4*fx1+fx2)
        #Obtenemos valor de la integral de forma analitica
        IntegralReal = self.Integral(b, a)
        #obtenemos el error
        error = (abs(IntegralReal - I) / IntegralReal) * 100
        #Mandamos resultado a pantalla con 3 cifras significativas
        lblx = Label(self.venUser, text="Resultado= " + str("{:.3f}".format(I)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(200))
        lblx = Label(self.venUser, text="Integral Analitica= " + str("{:.3f}".format(IntegralReal)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(225))
        lblx = Label(self.venUser, text="Error= " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(250))
    def MetodoSimpson38(self):
        # obtenemos los limites de la ventana
        a, b = float(self.xn.get()), float(self.hn.get())
        # obtenemos h
        h = (a + b) / 3
        # calculamos los diferentes x a trabajar
        x0 = a
        x1 = a + h
        x2 = x1 + h
        x3=x2+h
        fx0 = self.fxi(x0)
        fx1 = self.fxi(x1)
        fx2 = self.fxi(x2)
        fx3 = self.fxi(x3)
        # print (fx0)
        # print(fx1)
        # print(fx2)
        # Obtenemos el valor segun formula
        I = ((3*h) / 8) * (fx0 + 3  * fx1 + 3*fx2+fx3)
        # Obtenemos valor de la integral de forma analitica
        IntegralReal = self.Integral(b, a)
        # obtenemos el error
        error = (abs(IntegralReal - I) / IntegralReal) * 100
        # Mandamos resultado a pantalla con 3 cifras significativas
        lblx = Label(self.venUser, text="Resultado= " + str("{:.3f}".format(I)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(200))
        lblx = Label(self.venUser, text="Integral Analitica= " + str("{:.3f}".format(IntegralReal)), fg="navy",
                     bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(225))
        lblx = Label(self.venUser, text="Error= " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(250))
    def IntervalosIrregulares(self):
        Arre=np.zeros((11,4))
        I=0
        Arre[0][0],Arre[1][0],Arre[2][0],Arre[3][0]=float(self.Intervalon.get()),float(self.Intervalo2n.get()),float(self.Intervalo3n.get()),float(self.Intervalo4n.get())
        Arre[4][0], Arre[5][0], Arre[6][0], Arre[7][0] = float(self.Intervalo5n.get()), float(self.Intervalo6n.get()), float(self.Intervalo7n.get()), float(self.Intervalo8n.get())
        Arre[8][0], Arre[9][0], Arre[10][0]= float(self.Intervalo9n.get()), float(self.Intervalo10n.get()), float(self.Intervalo11n.get())
        for i in range(11):
            Arre[i][1]=self.fxi(Arre[i][0])
        for i in range(10):
            h=Arre[i+1][0]-Arre[i][0]
            Arre[i][2]=h
            #print (h)
        for i in range(10):
            Arre[i][3]=Arre[i][2]*((Arre[i][1]+Arre[i+1][1])/2)
        for i in range(10):
            I=I+Arre[i][3]
        #print (Arre)
            # Creo un frame para poner la tabla en la que muestro mis iteraciones
            tablaframe = Frame(self.venUser, width=480, height=235)
            tablaframe.place(x=3, y=310)
            tablaframe.grid_propagate(False)
            # Utilizo un Treeview para poner la tabla, esta lineas son de configuracion
            tree = ttk.Treeview(tablaframe, columns=(1, 2, 3, 4), height=10, show="headings")
            tree.pack(side='left')
            tree.column('#1', width=100, anchor='c')
            tree.column('#2', width=100, anchor='c')
            tree.column('#3', width=100, anchor='c')
            tree.column('#4', width=100, anchor='c')
            tree.heading(1, text="X")
            tree.heading(2, text="f(x)")
            tree.heading(3, text="h")
            tree.heading(4, text="I parcial")

            scroll = ttk.Scrollbar(tablaframe, orient="vertical", command=tree.yview)
            scroll.pack(side='right', fill='y')
            tree.configure(yscrollcommand=scroll.set)
            # con la matriz creada anteriormente lleno el treeview
            for val in Arre:
                tree.insert('', 'end', values=(val[0], val[1], val[2], val[3]))
            # Obtenemos valor de la integral de forma analitica
            IntegralReal = self.Integral(Arre[10][0], Arre[0][0])
            # obtenemos el error
            error = (abs(IntegralReal - I) / IntegralReal) * 100
            # Mandamos resultado a pantalla con 3 cifras significativas
            lblx = Label(self.venUser, text="Resultado= " + str("{:.3f}".format(I)), fg="navy", bg="SkyBlue2",font=("Arial", 12))
            lblx.place(x=0, y=(200))
            lblx = Label(self.venUser, text="Integral Analitica= " + str("{:.3f}".format(IntegralReal)), fg="navy",bg="SkyBlue2", font=("Arial", 12))
            lblx.place(x=0, y=(225))
            lblx = Label(self.venUser, text="Error= " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                             font=("Arial", 12))
            lblx.place(x=0, y=(250))
    def Formula3puntos(self):
        #se reciben los valores de x0,x1 y x2
        x0= float(self.Intervalon.get())
        #se obtienen los valores fx0,fx1 y fx2 ademas de h
        #fx0, fx1, fx2 = float(self.Intervalo4n.get()), float(self.Intervalo5n.get()), float(self.Intervalo6n.get())
        h = float(self.hn.get())
        fx0 = self.fxi(x0)
        fx1 = self.fxi((x0+h))
        fx2 = self.fxi((x0+(2*h)))
        fx3 = self.fxi((x0-h))
        fx4 = self.fxi((x0-(2*h)))
        derivada=self.derivadafx(x0)
        #print (derivada,fx0,fx1,fx2,fx3,fx4)
        #se ejecuta la formula
        dfx0=(-3*fx0+4*fx1-fx2)/(2*h)
        dfx2=(-3*fx0+4*fx3-fx4)/(-2*h)
        dfx1=(fx1-fx3)/(2*h)
        #Se manda a pantalla
        lblx = Label(self.venUser, text="f(0)= " + str("{:.3f}".format(dfx0)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(200))
        lblx = Label(self.venUser, text="f(1)= " + str("{:.3f}".format(dfx1)), fg="navy",
                     bg="SkyBlue2", font=("Arial", 12))
        lblx.place(x=0, y=(225))
        lblx = Label(self.venUser, text="f(2)= " + str("{:.3f}".format(dfx2)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(250))
        lblx = Label(self.venUser, text="Deriva analitica= " + str("{:.3f}".format(derivada)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(275))
    def Formula5puntos(self):
        # se reciben los valores de x0,x1 y x2
        x0= float(self.Intervalon.get())
        h = float(self.hn.get())
        # se obtienen los valores fx0,fx1 y fx2 ademas de h
        fx0 = self.fxi(x0)
        fx1 = self.fxi(x0 + h)
        fx2 = self.fxi(x0 + 2 * h)
        fx3 = self.fxi(x0 - h)
        fx4 = self.fxi(x0 - 2 * h)
        derivada = self.derivadafx(x0)
        #se ejecuta la formula
        aproximada=(1/(12*h))*(fx4-8*fx3+8*fx1-fx2)
        # Se da formato y se  manda a pantalla
        lblx = Label(self.venUser, text="derivada= " + str("{:.3f}".format(aproximada)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(200))
        lblx = Label(self.venUser, text="Deriva analitica= " + str("{:.3f}".format(derivada)), fg="navy",
                     bg="SkyBlue2", font=("Arial", 12))
        lblx.place(x=0, y=(225))
    def CuadraturaGaussiana(self):
        #se reciben los intervalos
        a, b= float(self.xn.get()), float(self.hn.get())
        #se aplica la formula de la cuadratura gausiana para obtener los intervalos
        x0 = -1 / np.sqrt(3)
        x1 = -x0
        xa = (b + a) / 2 + (b - a) / 2 * (x0)
        xb = (b + a) / 2 + (b - a) / 2 * (x1)
        #Se obtiene la aproximacion
        I = ((b - a) / 2) * (self.fxi(xa) + self.fxi(xb))
        # Obtenemos valor de la integral de forma analitica
        IntegralReal = self.Integral(b, a)
        # obtenemos el error
        error = (abs(IntegralReal - I) / IntegralReal) * 100
        # Mandamos resultado a pantalla con 3 cifras significativas
        lblx = Label(self.venUser, text="Resultado= " + str("{:.3f}".format(I)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(200))
        lblx = Label(self.venUser, text="Integral Analitica= " + str("{:.3f}".format(IntegralReal)), fg="navy",
                     bg="SkyBlue2", font=("Arial", 12))
        lblx.place(x=0, y=(225))
        lblx = Label(self.venUser, text="Error= " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(250))
    #Funcion para salir de la ventana
    def pafuera(self):
        sys.exit(1)
