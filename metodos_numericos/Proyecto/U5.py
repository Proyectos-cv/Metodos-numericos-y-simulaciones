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


class MenuUnidad5:
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
        lblInt = Label(self.venUser, text="Valor de x=         m=", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblInt.place(x=0, y=(67))
        #Cajas de texto que reciben los valores ingresados x,h y tolerancia
        self.x = DoubleVar()
        self.xn = Entry(self.venUser, textvariable=self.x, width=5, )
        self.xn.place(x=100, y=(72))
        self.m = DoubleVar()
        self.mn = Entry(self.venUser, textvariable=self.m, width=5, )
        self.mn.place(x=190, y=(72))
        #Etiqueta para referencia de la tabla
        lblSupExp = Label(self.venUser, text="   X     |       f(X)   ", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblSupExp.place(x=0, y=(90))
        lblSupExp = Label(self.venUser, text="          |                 ", fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(115))
        lblSupExp = Label(self.venUser, text="          |                 ", fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(140))
        lblSupExp = Label(self.venUser, text="          |                 ", fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(165))
        lblSupExp = Label(self.venUser, text="          |                 ", fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(190))
        lblSupExp = Label(self.venUser, text="          |                 ", fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(215))
        lblSupExp = Label(self.venUser, text="          |                 ", fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(240))
        #Cajas de texto para recibir valores de la superfomula
        self.x1 = DoubleVar()
        self.x1n = Entry(self.venUser, textvariable=self.x1, width=4, )
        self.x1n.place(x=15, y=(120))
        self.Fx1 = DoubleVar()
        self.Fx1n = Entry(self.venUser, textvariable=self.Fx1, width=4, )
        self.Fx1n.place(x=90, y=(120))
        self.x2 = DoubleVar()
        self.x2n = Entry(self.venUser, textvariable=self.x2, width=4, )
        self.x2n.place(x=15, y=(145))
        self.Fx2 = DoubleVar()
        self.Fx2n = Entry(self.venUser, textvariable=self.Fx2, width=4, )
        self.Fx2n.place(x=90, y=(145))
        self.x3 = DoubleVar()
        self.x3n = Entry(self.venUser, textvariable=self.x3, width=4, )
        self.x3n.place(x=15, y=(170))
        self.Fx3 = DoubleVar()
        self.Fx3n = Entry(self.venUser, textvariable=self.Fx3, width=4, )
        self.Fx3n.place(x=90, y=(170))
        self.x4 = DoubleVar()
        self.x4n = Entry(self.venUser, textvariable=self.x4, width=4, )
        self.x4n.place(x=15, y=(195))
        self.Fx4 = DoubleVar()
        self.Fx4n = Entry(self.venUser, textvariable=self.Fx4, width=4, )
        self.Fx4n.place(x=90, y=(195))
        self.x5 = DoubleVar()
        self.x5n = Entry(self.venUser, textvariable=self.x5, width=4, )
        self.x5n.place(x=15, y=(220))
        self.Fx5 = DoubleVar()
        self.Fx5n = Entry(self.venUser, textvariable=self.Fx5, width=4, )
        self.Fx5n.place(x=90, y=(220))
        self.x6 = DoubleVar()
        self.x6n = Entry(self.venUser, textvariable=self.x6, width=4, )
        self.x6n.place(x=15, y=(245))
        self.Fx6 = DoubleVar()
        self.Fx6n = Entry(self.venUser, textvariable=self.Fx6, width=4, )
        self.Fx6n.place(x=90, y=(245))
        self.x7 = DoubleVar()
        self.x7n = Entry(self.venUser, textvariable=self.x7, width=4, )
        self.x7n.place(x=15, y=(270))
        self.Fx7 = DoubleVar()
        self.Fx7n = Entry(self.venUser, textvariable=self.Fx7, width=4, )
        self.Fx7n.place(x=90, y=(270))
        #COMBOBOX
        self.comboExample = ttk.Combobox(self.venUser,values=["Polinomio I. Newton Lineal","Polinomio I. Newton Cuadratico","Polinomio I. Newton Cubico","Polinomio I. Lagrange Lineal","Polinomio I. Lagrange Cuadratico","Trazador lineal","Regresion polinomial","Minimos cuadrados","         "],state="readonly",width=30)
        self.comboExample.place(x=850, y=(72))
        self.comboExample.bind("<<ComboboxSelected>>", self.Eleccion_metodo_resolverE)

        btnSalir = Button(self.venUser, text="Salir", bg='grey', command=self.pafuera,width=20,height=2)
        btnSalir.place(x=550, y=550)
        height = 5
        self.venUser.mainloop()

    def Eleccion_metodo_resolverE(self,event):
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                      font=("Arial", 12))
        lblx.place(x=0, y=(325))
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                     font=("Arial", 12))
        lblx.place(x=0, y=(350))
        lblx = Label(self.venUser, text="                                                           ", fg="navy", bg="white",
                     font=("Arial", 12))
        lblx.place(x=0, y=(375))
        if self.comboExample.get()=="Polinomio I. Newton Lineal":
            self.NewtonLineal()
        if self.comboExample.get()=="Polinomio I. Newton Cuadratico":
            self.NewtonCuadratica()
        if self.comboExample.get()=="Polinomio I. Newton Cubico":
            self.NewtonCubica()
        if self.comboExample.get()=="Polinomio I. Lagrange Lineal":
            self.LagrangeLineal()
        if self.comboExample.get()=="Polinomio I. Lagrange Cuadratico":
            self.LagrangeCuadratica()
        if self.comboExample.get()=="Trazador lineal":
            self.TrazadorPrimer()
        if self.comboExample.get()=="Regresion polinomial":
            self.RegresionPolinomial()
        if self.comboExample.get()=="Minimos cuadrados":
            self.minCuadrados()
    #Funcion para el calculo de xi o f(a) para metodo de newton cuadratica
    def NewtonCuadratica(self):
        #Recibimos los datos de x y fx
        x0,x1,x,x2=float(self.x1n.get()), float(self.x2n.get()),float(self.xn.get()),float(self.x3n.get())
        fx0, fx1,fx2 = float(self.Fx1n.get()), float(self.Fx2n.get()), float(self.Fx3n.get())
        #Hacemos las operaciones para obtener los valores
        b1 =((fx1 - fx0) / (x1 - x0))
        b2=(((fx2 - fx1) / (x2 - x1))-b1)/(x2-x1)
        #aplicamos la ecuacion para obtener el polinomio
        fx=fx0+b1*(x-x0)+b2*(x-x0)*(x-x1)
        #obtenemos el error
        error = (abs(x - fx) / x) * 100
        #print(fx)
        #print (b1,b2)
        #Mandamos a pantalla
        lblx = Label(self.venUser, text="Newton Cubica= " + str("{:.3f}".format(fx)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="Error  = " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))

    # Funcion para el calculo de xi o f(a) para metodo de newton cubica
    def NewtonCubica(self):
        # Recibimos los datos de x y fx
        x0, x1, x, x2,x3 = float(self.x1n.get()), float(self.x2n.get()), float(self.xn.get()), float(self.x3n.get()), float(self.x4n.get())
        fx0, fx1, fx2,fx3 = float(self.Fx1n.get()), float(self.Fx2n.get()), float(self.Fx3n.get()), float(self.Fx4n.get())
        #Hacemos los calculos de cada parte de la ecuacion
        b1 = ((fx1 - fx0) / (x1 - x0))
        b2 = (((fx2 - fx1) / (x2 - x1)) - b1) / (x2 - x1)
        # aplicamos la ecuacion para obtener el polinomio
        b3=(((fx3 - fx2) / (x3 - x2))-((fx2 - fx1) / (x2 - x1))-((fx1 - fx0) / (x1 - x0)))/(x3 - x2)
        fx = fx0 + b1 * (x - x0) + b2 * (x - x0) * (x - x1)+b3*(x-x0)*(x-x1)*(x-x2)
        # obtenemos el error
        error = (abs(x - fx) / x) * 100
        # print(fx)
        #print(b1, b2)
        # Mandamos a pantalla
        lblx = Label(self.venUser, text="Newton Cuadratica= " + str("{:.3f}".format(fx)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="Error  = " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))
    # Funcion para el calculo de xi o f(a) para metodo de newton lineal
    def NewtonLineal(self):
        # Recibimos los datos de x y fx
        x0, x1, x = float(self.x1n.get()), float(self.x2n.get()), float(self.xn.get())
        fx0, fx1 = float(self.Fx1n.get()), float(self.Fx2n.get())
        # aplicamos la ecuacion para obtener el polinomio
        fx = fx0 + ((fx1 - fx0) / (x1 - x0)) * (x - x0)
        # obtenemos el error
        error = (abs(x - fx) / x) * 100
        # print(fx)
        # Mandamos a pantalla
        lblx = Label(self.venUser, text="Newton Lineal= " + str("{:.3f}".format(fx)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="Error  = " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))
    #Funcion para polinomio de lagrange lineal
    def LagrangeLineal(self):
        x0, x1, x = float(self.x1n.get()), float(self.x2n.get()), float(self.xn.get())
        fx0, fx1 = float(self.Fx1n.get()), float(self.Fx2n.get())
        fx=(fx0*((x-x1)/(x0-x1)))+(fx1*((x-x0)/(x1-x0)))
        # obtenemos el error
        error = (abs(x - fx) / x) * 100
        # print(fx)
        # Mandamos a pantalla
        lblx = Label(self.venUser, text="Lagrange Lineal= " + str("{:.3f}".format(fx)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="Error  = " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))

    # Funcion para polinomio de lagrange cuadratica
    def LagrangeCuadratica(self):
        # Recibimos los datos de x y fx
        x0, x1, x, x2 = float(self.x1n.get()), float(self.x2n.get()), float(self.xn.get()), float(self.x3n.get())
        fx0, fx1, fx2 = float(self.Fx1n.get()), float(self.Fx2n.get()), float(self.Fx3n.get())
        # aplicamos la ecuacion para obtener el polinomio
        fx = (fx0*(((x-x1)*(x-x2))/((x0-x1)*(x0-x2))))+(fx1*(((x-x0)*(x-x2))/((x1-x0)*(x1-x2))))+(fx2*(((x-x0)*(x-x1))/((x2-x0)*(x2-x1))))
        # obtenemos el error
        error = (abs(x - fx) / x) * 100
        # print(fx)
        # print (b1,b2)
        # Mandamos a pantalla
        lblx = Label(self.venUser, text="Lagrange Cuadratica= " + str("{:.3f}".format(fx)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="Error  = " + str("{:.3f}".format(error)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))
    def TrazadorPrimer(self):
        # Recibimos los datos de x y fx
        x0, x1, x = float(self.x1n.get()), float(self.x2n.get()), float(self.xn.get())
        fx0, fx1 = float(self.Fx1n.get()), float(self.Fx2n.get())
        #sustituimos valores en la formula
        m=(fx1-fx0)/(x1-x0)
        lblx = Label(self.venUser, text="Trazador lineal= " + str("{:.3f}".format(m)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
    def RegresionPolinomial(self):
        #recibimos los valores
        m,x,x0, x1, x2, x3, x4, x5 = float(self.mn.get()),float(self.xn.get()),float(self.x1n.get()), float(self.x2n.get()), float(self.x3n.get()), float(self.x4n.get()), float(self.x5n.get()), float(self.x6n.get())
        fx0, fx1,fx2,fx3 ,fx4 ,fx5  = float(self.Fx1n.get()), float(self.Fx2n.get()), float(self.Fx3n.get()), float(self.Fx4n.get()), float(self.Fx5n.get()), float(self.Fx6n.get())
        #obtengo las sumatorias de todo
        xi=x0+x1+x2+x3+x4+x5
        yi = fx0 + fx1 + fx2 + fx3 + fx4 + fx5
        xi2 = x0**2 + x1**2 + x2**2 + x3**2 + x4**2 + x5**2
        xi3 = x0 ** 3 + x1 ** 3 + x2 ** 3 + x3 ** 3 + x4 ** 3 + x5 ** 3
        xi4= x0 ** 4 + x1 ** 4 + x2 ** 4 + x3 ** 4 + x4 ** 4 + x5 ** 4
        xyi = fx0*x0 + fx1*x1 + fx2*x2 + fx3*x3 + fx4*x4 + fx5*x5
        xyi2 = fx0*x0**2 + fx1*x1**2 + fx2*x2**2 + fx3*x3**2 + fx4*x4**2 + fx5*x5**2
        ymed=yi/x
        yiymed=(fx0-ymed)**2+(fx1-ymed)**2+(fx2-ymed)**2+(fx3-ymed)**2+(fx4-ymed)**2+(fx5-ymed)**2
        #print (xi,xi2,xi3,xi4,yi,xyi,xyi2)
        #uso la funcion inversa de numpy para resolver el sistema de ecuaciones
        A = np.array([[x, xi, xi2], [xi, xi2, xi3], [xi2, xi3, xi4]])
        B = np.array([yi,xyi,xyi2])
        X = np.linalg.inv(A).dot(B)
        #print(X)
        #print (X[2])
        sumyi=(fx0-X[0]-X[1]*x0-X[2]*(x0**2))**2+(fx1-X[0]-X[1]*x1-X[2]*x1**2)**2+(fx2-X[0]-X[1]*x2-X[2]*x2**2)**2+(fx3-X[0]-X[1]*x3-X[2]*x3**2)**2+(fx4-X[0]-X[1]*x4-X[2]*x4**2)**2+(fx5-X[0]-X[1]*x5-X[2]*x5**2)**2
        syx=(sumyi/(x-(m+1)))**(1/2)
        #print(syx)
        r2=(yiymed-sumyi)/yiymed
        lblx = Label(self.venUser, text="y= " + str("{:.3f}".format(X[0]))+"+ "+ str("{:.3f}".format(X[1]))+" X +"+ str("{:.3f}".format(X[2]))+"X2", fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="Sy/x  = " + str("{:.3f}".format(syx)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))
        lblx = Label(self.venUser, text="Coeficiente correlacion  = " + str("{:.3f}".format(r2)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(350))
    def minCuadrados(self):
        m, x, x0, x1, x2, x3, x4, x5,x6 = float(self.mn.get()), float(self.xn.get()), float(self.x1n.get()), float(
            self.x2n.get()), float(self.x3n.get()), float(self.x4n.get()), float(self.x5n.get()), float(self.x6n.get()), float(self.x7n.get())
        fx0, fx1, fx2, fx3, fx4, fx5,fx6 = float(self.Fx1n.get()), float(self.Fx2n.get()), float(self.Fx3n.get()), float(
            self.Fx4n.get()), float(self.Fx5n.get()), float(self.Fx6n.get()), float(self.Fx7n.get())
        #se obtienen todos los factores que necesita
        xi = x0 + x1 + x2 + x3 + x4 + x5+x6
        yi = fx0 + fx1 + fx2 + fx3 + fx4 + fx5+fx6
        xi2 = x0 ** 2 + x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x5 ** 2+x6**2
        xi3 = x0 ** 3 + x1 ** 3 + x2 ** 3 + x3 ** 3 + x4 ** 3 + x5 ** 3+x6**3
        xyi = fx0 * x0 + fx1 * x1 + fx2 * x2 + fx3 * x3 + fx4 * x4 + fx5 * x5+fx6*x6
        xmed=xi/x
        yimed=yi/x
        a1=(x*xyi-xi*yi)/(x*xi2-(xi**2))
        a0=yimed-a1*xmed
        print (xi,yi,xi2,xi3,xyi,xmed,yimed,a1,a0)

        #se obtiene el coeficiente para cuantificar el error
        yiymed=(fx0-yimed)**2+(fx1-yimed)**2+(fx2-yimed)**2+(fx3-yimed)**2+(fx4-yimed)**2+(fx5-yimed)**2+(fx6-yimed)**2
        sr=(fx0-a0-a1*x0)**2+(fx2-a0-a1*x2)**2+(fx1-a0-a1*x1)**2+(fx3-a0-a1*x3)**2+(fx4-a0-a1*x4)**2+(fx5-a0-a1*x5)**2+(fx6-a0-a1*x6)**2

        syx = (sr / (x - 2)) ** (1 / 2)
        print (yiymed,sr,syx)
        r2=(yiymed-sr)/yiymed
        lblx = Label(self.venUser,
                     text="y= " + str("{:.3f}".format(a0)) + "+ " + str("{:.3f}".format(a1)) + " X", fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(300))
        lblx = Label(self.venUser, text="Sy/x  = " + str("{:.3f}".format(syx)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))
        lblx = Label(self.venUser, text="Coeficiente correlacion  = " + str("{:.3f}".format(r2))+"r="+str("{:.3f}".format(r)), fg="navy",
                     bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(350))
    #Funcion para salir de la ventana
    def pafuera(self):
        sys.exit(1)
