# -*- coding: utf-8 -*-
#!/usr/bin/env python

from tkinter import *
#from ttk import Combobox,Treeview
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sys


class MenuUnidad6:
    def __init__(self):
        self.venUser=Toplevel()
        self.venUser.geometry("400x200")
        self.venUser.config(bg="#ffffff")
        self.venUser.config(cursor="cross")
        self.venUser.config(relief="sunken")
        self.venUser.title("Métodos Iterativos")
        ancho_ventana = 1210
        alto_ventana = 600
        x_ventana = self.venUser.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.venUser.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.venUser.geometry(posicion)
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial"), width=1000,height=5)
        lblEti.place(x=0, y=(0))
        lblEti = Label(self.venUser, text="Unidad 6: Solucion de ecuaciones diferenciales", fg="navy", bg="SkyBlue2",
                       font=("Arial", 36))
        lblEti.place(x=90, y=(0))
        lblSol = Label(self.venUser, text="Métodos de un paso", fg="navy", bg="SkyBlue2",
                       font=("Arial", 24))
        lblSol.place(x=350, y=(50))
        #METODOS CON INTERVALOS
        lblInt = Label(self.venUser, text="Valores iniciales=         x a        y=        H=                     Tolerancia               ", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblInt.place(x=0, y=(92))
        #CAJAS PARA VALORES INICIALES
        self.x1 = DoubleVar()
        self.x1e = Entry(self.venUser, textvariable=self.x1, width=5, )
        self.x1e.place(x=160, y=(97))
        self.x2 = DoubleVar()
        self.x2n = Entry(self.venUser, textvariable=self.x2, width=5, )
        self.x2n.place(x=225, y=(97))
        self.y1 = DoubleVar()
        self.y1n = Entry(self.venUser, textvariable=self.y1, width=5, )
        self.y1n.place(x=285, y=(97))
        self.w1 = DoubleVar()
        self.w1n = Entry(self.venUser, textvariable=self.w1, width=5, )
        self.w1n.place(x=345, y=(97))
        self.IntTol = DoubleVar()
        self.IntTole = Entry(self.venUser, textvariable=self.IntTol, width=5, )
        self.IntTole.place(x=550, y=(97))
        lblSupExp = Label(self.venUser, text="Adecua la expresion a tu problema:       x^       +       y^       +       x^       +       y^       +       x^       y+       y^       x+        =0", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblSupExp.place(x=0, y=(120))
        self.Fx1 = IntVar()
        self.Fx1n = Entry(self.venUser, textvariable=self.Fx1, width=4, )
        self.Fx1n.place(x=303, y=(125))
        self.Ex1 = IntVar()
        self.Ex1n = Entry(self.venUser, textvariable=self.Ex1, width=4, )
        self.Ex1n.place(x=355, y=(125))
        self.Fy1 = IntVar()
        self.Fy1n = Entry(self.venUser, textvariable=self.Fy1, width=4, )
        self.Fy1n.place(x=400, y=(125))
        self.Ey1 = IntVar()
        self.Ey1n = Entry(self.venUser, textvariable=self.Ey1, width=4, )
        self.Ey1n.place(x=450, y=(125))
        self.Fx2 = IntVar()
        self.Fx2n = Entry(self.venUser, textvariable=self.Fx2, width=4, )
        self.Fx2n.place(x=498, y=(125))
        self.Ex2 = IntVar()
        self.Ex2n = Entry(self.venUser, textvariable=self.Ex2, width=4, )
        self.Ex2n.place(x=548, y=(125))
        self.Fy2 = IntVar()
        self.Fy2n = Entry(self.venUser, textvariable=self.Fy2, width=4, )
        self.Fy2n.place(x=595, y=(125))
        self.Ey2 = IntVar()
        self.Ey2n = Entry(self.venUser, textvariable=self.Ey2, width=4, )
        self.Ey2n.place(x=648, y=(125))
        self.Fxy = IntVar()
        self.Fxyn = Entry(self.venUser, textvariable=self.Fxy, width=4, )
        self.Fxyn.place(x=690, y=(125))
        self.Pxy = IntVar()
        self.Pxyn = Entry(self.venUser, textvariable=self.Pxy, width=4, )
        self.Pxyn.place(x=740, y=(125))
        self.Fxy2 = IntVar()
        self.Fxy2n = Entry(self.venUser, textvariable=self.Fxy2, width=4, )
        self.Fxy2n.place(x=795, y=(125))
        self.Pxy2 = IntVar()
        self.Pxy2n = Entry(self.venUser, textvariable=self.Pxy2, width=4, )
        self.Pxy2n.place(x=845, y=(125))
        self.num = IntVar()
        self.numn = Entry(self.venUser, textvariable=self.num, width=4, )
        self.numn.place(x=903, y=(125))
        #Serie de ecuaciones para Taylor
        lblSupExp = Label(self.venUser,
                          text="Adecua la expresion a tu problema:       x^       +       x^       +       x^       +       x^       +       x^       +        =0",
                          fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(180))
        # Cajas de texto para recibir valores de la superfomula
        self.TFx1 = DoubleVar()
        self.TFx1n = Entry(self.venUser, textvariable=self.TFx1, width=4, )
        self.TFx1n.place(x=303, y=(185))
        self.TEx1 = DoubleVar()
        self.TEx1n = Entry(self.venUser, textvariable=self.TEx1, width=4, )
        self.TEx1n.place(x=355, y=(185))
        self.TFx2 = DoubleVar()
        self.TFx2n = Entry(self.venUser, textvariable=self.TFx2, width=4, )
        self.TFx2n.place(x=400, y=(185))
        self.TEx2 = DoubleVar()
        self.TEx2n = Entry(self.venUser, textvariable=self.TEx2, width=4, )
        self.TEx2n.place(x=450, y=(185))
        self.TFx3 = DoubleVar()
        self.TFx3n = Entry(self.venUser, textvariable=self.TFx3, width=4, )
        self.TFx3n.place(x=498, y=(185))
        self.TEx3 = DoubleVar()
        self.TEx3n = Entry(self.venUser, textvariable=self.TEx3, width=4, )
        self.TEx3n.place(x=548, y=(185))
        self.TFx4 = DoubleVar()
        self.TFx4n = Entry(self.venUser, textvariable=self.TFx4, width=4, )
        self.TFx4n.place(x=595, y=(185))
        self.TEx4 = DoubleVar()
        self.TEx4n = Entry(self.venUser, textvariable=self.TEx4, width=4, )
        self.TEx4n.place(x=648, y=(185))
        self.TFx5 = DoubleVar()
        self.TFx5n = Entry(self.venUser, textvariable=self.TFx5, width=4, )
        self.TFx5n.place(x=690, y=(185))
        self.TEx5 = DoubleVar()
        self.TEx5n = Entry(self.venUser, textvariable=self.TEx5, width=4, )
        self.TEx5n.place(x=740, y=(185))
        self.Tnum = DoubleVar()
        self.Tnumn = Entry(self.venUser, textvariable=self.Tnum, width=4, )
        self.Tnumn.place(x=792, y=(185))
        lblSupExp = Label(self.venUser,
                          text="Adecua la expresion a tu problema:       x^       +       x^       +       x^       +       x^       +       x^       +        =0",
                          fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(210))
        # Cajas de texto para recibir valores de la superfomula
        self.T3Fx1 = DoubleVar()
        self.T3Fx1n = Entry(self.venUser, textvariable=self.T3Fx1, width=4, )
        self.T3Fx1n.place(x=303, y=(215))
        self.T3Ex1 = DoubleVar()
        self.T3Ex1n = Entry(self.venUser, textvariable=self.T3Ex1, width=4, )
        self.T3Ex1n.place(x=355, y=(215))
        self.T3Fx2 = DoubleVar()
        self.T3Fx2n = Entry(self.venUser, textvariable=self.T3Fx2, width=4, )
        self.T3Fx2n.place(x=400, y=(215))
        self.T3Ex2 = DoubleVar()
        self.T3Ex2n = Entry(self.venUser, textvariable=self.T3Ex2, width=4, )
        self.T3Ex2n.place(x=450, y=(215))
        self.T3Fx3 = DoubleVar()
        self.T3Fx3n = Entry(self.venUser, textvariable=self.T3Fx3, width=4, )
        self.T3Fx3n.place(x=498, y=(215))
        self.T3Ex3 = DoubleVar()
        self.T3Ex3n = Entry(self.venUser, textvariable=self.T3Ex3, width=4, )
        self.T3Ex3n.place(x=548, y=(215))
        self.T3Fx4 = DoubleVar()
        self.T3Fx4n = Entry(self.venUser, textvariable=self.T3Fx4, width=4, )
        self.T3Fx4n.place(x=595, y=(215))
        self.T3Ex4 = DoubleVar()
        self.T3Ex4n = Entry(self.venUser, textvariable=self.T3Ex4, width=4, )
        self.T3Ex4n.place(x=648, y=(215))
        self.T3Fx5 = DoubleVar()
        self.T3Fx5n = Entry(self.venUser, textvariable=self.T3Fx5, width=4, )
        self.T3Fx5n.place(x=690, y=(215))
        self.T3Ex5 = DoubleVar()
        self.T3Ex5n = Entry(self.venUser, textvariable=self.T3Ex5, width=4, )
        self.T3Ex5n.place(x=740, y=(215))
        self.T3num = DoubleVar()
        self.T3numn = Entry(self.venUser, textvariable=self.T3num, width=4, )
        self.T3numn.place(x=792, y=(215))
        lblSupExp = Label(self.venUser,
                          text="Adecua la expresion a tu problema:       x^       +       x^       +       x^       +       x^       +       x^       +        =0",
                          fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp.place(x=0, y=(240))
        # Cajas de texto para recibir valores de la superfomula
        self.T4Fx1 = DoubleVar()
        self.T4Fx1n = Entry(self.venUser, textvariable=self.T4Fx1, width=4, )
        self.T4Fx1n.place(x=303, y=(245))
        self.T4Ex1 = DoubleVar()
        self.T4Ex1n = Entry(self.venUser, textvariable=self.T4Ex1, width=4, )
        self.T4Ex1n.place(x=355, y=(245))
        self.T4Fx2 = DoubleVar()
        self.T4Fx2n = Entry(self.venUser, textvariable=self.T4Fx2, width=4, )
        self.T4Fx2n.place(x=400, y=(245))
        self.T4Ex2 = DoubleVar()
        self.T4Ex2n = Entry(self.venUser, textvariable=self.T4Ex2, width=4, )
        self.T4Ex2n.place(x=450, y=(245))
        self.T4Fx3 = DoubleVar()
        self.T4Fx3n = Entry(self.venUser, textvariable=self.T4Fx3, width=4, )
        self.T4Fx3n.place(x=498, y=(245))
        self.T4Ex3 = DoubleVar()
        self.T4Ex3n = Entry(self.venUser, textvariable=self.T4Ex3, width=4, )
        self.T4Ex3n.place(x=548, y=(245))
        self.T4Fx4 = DoubleVar()
        self.T4Fx4n = Entry(self.venUser, textvariable=self.T4Fx4, width=4, )
        self.T4Fx4n.place(x=595, y=(245))
        self.T4Ex4 = DoubleVar()
        self.T4Ex4n = Entry(self.venUser, textvariable=self.T4Ex4, width=4, )
        self.T4Ex4n.place(x=648, y=(245))
        self.T4Fx5 = DoubleVar()
        self.T4Fx5n = Entry(self.venUser, textvariable=self.T4Fx5, width=4, )
        self.T4Fx5n.place(x=690, y=(245))
        self.T4Ex5 = DoubleVar()
        self.T4Ex5n = Entry(self.venUser, textvariable=self.T4Ex5, width=4, )
        self.T4Ex5n.place(x=740, y=(245))
        self.T4num = DoubleVar()
        self.T4numn = Entry(self.venUser, textvariable=self.T4num, width=4, )
        self.T4numn.place(x=792, y=(245))
        #COMBOBOX
        self.comboExample = ttk.Combobox(self.venUser,values=["Metodo de Euler","Metodo de Heun","Taylor","Runge-Kutta","         "],state="readonly")
        self.comboExample.place(x=750, y=(60))
        self.comboExample.bind("<<ComboboxSelected>>", self.Eleccion_metodo_resolverE)
        btnSalir = Button(self.venUser, text="Salir", bg='grey', command=self.pafuera,width=20,height=2)
        btnSalir.place(x=550, y=550)
        height = 5
        self.venUser.mainloop()

    def Eleccion_metodo_resolverE(self,event):
        if self.comboExample.get()=="Metodo de Euler":
            self.Met_Euler()
        if self.comboExample.get()=="Metodo de Heun":
            self.Heun()
        if self.comboExample.get()=="Taylor":
            self.Taylor()
        if self.comboExample.get()=="Runge-Kutta":
            self.Runge()
    #Funcion para evaluar fx con los valores x y y
    def fx(self,x,y):
        Fx1,Ex1,Fy1,Ey1,Fx2,Ex2,Fy2,Ey2=float(self.Fx1n.get()),float(self.Ex1n.get()),float(self.Fy1n.get()),float(self.Ey1n.get()),float(self.Fx2n.get()),float(self.Ex2n.get()),float(self.Fy2n.get()),float(self.Ey2n.get())
        Fxy1,Exy1,Fxy2,Exy2, num=float(self.Fxyn.get()),float(self.Pxyn.get()),float(self.Fxy2n.get()),float(self.Pxy2n.get()),int(self.numn.get())
        print (Fx1,Ex1,Fy1,Ey1,Fx2,Ex2,Fy2,Ey2)
        #print (Fx1,Ex1,Fy1,Ey1,Fx2,Ex2,Fy2,Ey2)
        #print(Fxy1,Exy1,Fxy2,Exy2, num)
        return Fx1*x**Ex1+Fx2*x**Ex2+Fy2*y**Ey2+Fy1*y**Ey1+Fxy1*y*x**Exy1+Fxy2*x*y**Exy2+num
    def fxi2(self,x):
        Fx1, Ex1, Fx2, Ex2, Fx3, Ex3, Fx4, Ex4 = float(self.TFx1n.get()), float(self.TEx1n.get()), float(
            self.TFx2n.get()), float(self.TEx2n.get()), float(self.TFx3n.get()), float(self.TEx3n.get()), float(
            self.TFx4n.get()), float(self.TEx4n.get())
        Fx5, Ex5, num = float(self.TFx5n.get()), float(self.TEx5n.get()), float(self.Tnumn.get())
        return Fx1*x**Ex1+Fx2*x**Ex2+Fx3*x**Ex3+Fx4*x**Ex4+Fx5*x**Ex5+num
    def fxi3(self,x):
        Fx1, Ex1, Fx2, Ex2, Fx3, Ex3, Fx4, Ex4 = float(self.T3Fx1n.get()), float(self.T3Ex1n.get()), float(
            self.T3Fx2n.get()), float(self.T3Ex2n.get()), float(self.T3Fx3n.get()), float(self.T3Ex3n.get()), float(
            self.T3Fx4n.get()), float(self.T3Ex4n.get())
        Fx5, Ex5, num = float(self.T3Fx5n.get()), float(self.T3Ex5n.get()), float(self.T3numn.get())
        return Fx1*x**Ex1+Fx2*x**Ex2+Fx3*x**Ex3+Fx4*x**Ex4+Fx5*x**Ex5+num
    def fxi4(self,x):
        Fx1, Ex1, Fx2, Ex2, Fx3, Ex3, Fx4, Ex4 = float(self.T4Fx1n.get()), float(self.T4Ex1n.get()), float(
            self.T4Fx2n.get()), float(self.T4Ex2n.get()), float(self.T4Fx3n.get()), float(self.T4Ex3n.get()), float(
            self.T4Fx4n.get()), float(self.T4Ex4n.get())
        Fx5, Ex5, num = float(self.T4Fx5n.get()), float(self.T4Ex5n.get()), float(self.T4numn.get())
        return Fx1*x**Ex1+Fx2*x**Ex2+Fx3*x**Ex3+Fx4*x**Ex4+Fx5*x**Ex5+num
    #Funcion para evaluar la primer derivada
    def dux(self,x,y):
        Fx1, Ex1, Fy1, Ey1, Fx2, Ex2, Fy2, Ey2 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fy1n.get()), float(self.Ey1n.get()), float(self.Fx2n.get()), float(self.Ex2n.get()), float(
            self.Fy2n.get()), float(self.Ey2n.get())
        Fxy1, Exy1, Fxy2, Exy2, num = float(self.Fxyn.get()), float(self.Pxyn.get()), float(self.Fxy2n.get()), float(
            self.Pxy2n.get()), int(self.numn.get())
        return Ex1*Fx1*x**(Ex1-1)+Ex2*Fx2*x**(Ex2-1)+Exy1*Fxy1*y*x**(Exy1-1)+Fxy2*y**(Exy2)
    def Met_Euler(self):
        # se reciben valores de entrada
        x0,xi, y1 = float(self.x1.get()),float(self.x2.get()), float(self.y1.get())
        h = float(self.w1.get())
        # se crea el numero de iteraciones y una tabla para mostrar
        n=int((xi-x0)/h)
        #print (x0,xi,y1,h,n)
        ta=np.zeros((n+1,3))
        conta=1
        ta[0, 0] = x0
        ta[0, 1] = y1
        #print(ta)
        #se ejecuta este siclo donde a
        while x0<=xi and conta<=n:
            ta[conta-1, 2] = (self.fx(ta[conta-1 , 0], ta[conta-1, 1]))
            ta[conta, 1] = ta[conta-1,1]+(self.fx(ta[conta-1,0],ta[conta-1,1]))*h

            x0+=h
            ta[conta,0]=x0
            conta+=1
            #print (ta)
            #print ("")
        print (ta)
        tabla = Frame(self.venUser, width=480, height=235)
        tabla.place(x=3, y=310)
        tabla.grid_propagate(False)
        tree = ttk.Treeview(tabla, columns=(1, 2, 3), height=10, show="headings")
        tree.pack(side='left')
        tree.heading(1, text="X")
        tree.heading(2, text="Y")
        tree.heading(3, text="f(x,y)")
        scroll = ttk.Scrollbar(tabla, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        for val in ta:
            tree.insert('', 'end', values=(val[0], val[1], val[2]))

    #funcion para calcular el metodo de Heun
    def Heun(self):
        # se reciben valores de entrada
        x0, xi, y1 = float(self.x1.get()), float(self.x2.get()), float(self.y1.get())
        h = float(self.w1.get())
        # se crea el numero de iteraciones y una tabla para mostrar
        n = int((xi - x0) / h)
        ta = np.zeros((n + 1, 9))
        conta=0
        while conta<=n:
            if conta==0:
                ta[conta, 0] = x0#xn
                ta[conta, 1]= y1#yn
                ta[conta, 2]= self.fx(ta[conta,0],ta[conta,1])
                ta[conta, 3] = ta[conta, 2]*h
                ta[conta, 4] = ta[conta, 0] + h
                ta[conta, 5] = ta[conta, 1] + ta[conta, 3]
                ta[conta, 6] = self.fx(ta[conta, 4], ta[conta, 5])
                ta[conta, 7]=(ta[conta, 2]+ta[conta, 6])/2
                ta[conta, 8]=ta[conta, 7]*h
            else:
                ta[conta, 0] = ta[conta-1, 0]+h
                ta[conta, 1] = ta[conta-1, 1]+ta[conta-1, 8]
                ta[conta, 2] = self.fx(ta[conta, 0], ta[conta, 1])
                ta[conta, 3] = ta[conta, 2] * h
                ta[conta, 4] = ta[conta, 0] + h
                ta[conta, 5] = ta[conta, 1] + ta[conta, 3]
                ta[conta, 6] = self.fx(ta[conta, 4], ta[conta, 5])
                ta[conta, 7] = (ta[conta, 2] + ta[conta, 6]) / 2
                ta[conta, 8] = ta[conta, 7] * h
            conta+=1
        # Creo un frame para poner la tabla en la que muestro mis iteraciones
        tablaframe = Frame(self.venUser, width=480, height=235)
        tablaframe.place(x=3, y=310)
        tablaframe.grid_propagate(False)
        # Utilizo un Treeview para poner la tabla, esta lineas son de configuracion
        tree = ttk.Treeview(tablaframe, columns=(1, 2, 3, 4,5,6,7,8,9), height=10, show="headings")
        tree.pack(side='left')
        tree.column('#1', width=100, anchor='c')
        tree.column('#2', width=100, anchor='c')
        tree.column('#3', width=100, anchor='c')
        tree.column('#4', width=100, anchor='c')
        tree.column('#5', width=100, anchor='c')
        tree.column('#6', width=100, anchor='c')
        tree.column('#7', width=100, anchor='c')
        tree.column('#8', width=100, anchor='c')
        tree.column('#9', width=100, anchor='c')
        tree.heading(1, text="Xn")
        tree.heading(2, text="Yn")
        tree.heading(3, text="(dy/dx)n")
        tree.heading(4, text="Delta y")
        tree.heading(5, text="xn+h")
        tree.heading(6, text="yn+Delta y")
        tree.heading(7, text="(dy/dx)n+1")
        tree.heading(8, text="(dy/dx)prom")
        tree.heading(9, text="Delta corr")
        scroll = ttk.Scrollbar(tablaframe, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        # con la matriz creada anteriormente lleno el treeview
        for val in ta:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3],val[4], val[5], val[6], val[7],val[8]))
        #print (ta)

    def Taylor(self):
        # se reciben valores de entrada
        x0, xi, y1 = float(self.x1.get()), float(self.x2.get()), float(self.y1.get())
        h = float(self.w1.get())
        f2=self.fxi2(x0)
        f3=self.fxi3(x0)
        f4 = self.fxi4(x0)
        print (f4,f2,f3)
        et2=((f2)/2)*(h)**2
        et3 = ((f3) / 6) * (h) ** 3
        et4 = ((f4) / 24) * (h) ** 4
        et=et2+et3+et4
        lblx = Label(self.venUser, text="Resultado  = " + str("{:.3f}".format(et)), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=0, y=(325))
        print (et2,et3,et4,et)
    def Runge(self):
        # se reciben valores de entrada
        x0, xi, y1 = float(self.x1.get()), float(self.x2.get()), float(self.y1.get())
        h = float(self.w1.get())
        # se crea el numero de iteraciones y una tabla para mostrar
        n = int((xi - x0) / h)
        ta = np.zeros((n + 1, 12))
        conta = 0
        while conta <= n:
            if conta == 0:
                ta[conta, 0] = x0#Xn
                ta[conta, 1] = y1#Yn
                ta[conta, 2] = self.fx(ta[conta, 0], ta[conta, 1])#k1
                ta[conta, 3] = ta[conta, 0] + h/2#x+h/2
                ta[conta, 4] = ta[conta, 1] + ta[conta, 2]*h/2#y+k1h/2
                ta[conta, 5] = self.fx(ta[conta, 3], ta[conta, 4])#k2
                ta[conta, 6] = ta[conta, 0] + h/2#x+h/2
                ta[conta, 7] = ta[conta, 1] + ta[conta, 5]*h/2#y+k2h/2
                ta[conta, 8] = self.fx(ta[conta, 6], ta[conta, 7])#k3
                ta[conta, 9] = ta[conta, 0] + h  # x+h
                ta[conta, 10] = ta[conta, 1]+ h*ta[conta, 8] # y+k3h
                ta[conta, 11] = self.fx(ta[conta, 9], ta[conta, 10]) # k4
            else:
                ta[conta, 0] = ta[conta - 1, 0] + h
                ta[conta, 1] = ta[conta - 1, 1] + (h/6)*(ta[conta - 1, 2]+2*ta[conta - 1, 5]+2*ta[conta - 1, 8]+ta[conta - 1, 11])
                ta[conta, 2] = self.fx(ta[conta, 0], ta[conta, 1])  # k1
                ta[conta, 3] = ta[conta, 0] + h / 2  # x+h/2
                ta[conta, 4] = ta[conta, 1] + ta[conta, 2] * h / 2  # y+k1h/2
                ta[conta, 5] = self.fx(ta[conta, 3], ta[conta, 4])  # k2
                ta[conta, 6] = ta[conta, 0] + h / 2  # x+h/2
                ta[conta, 7] = ta[conta, 1] + ta[conta, 5] * h / 2  # y+k2h/2
                ta[conta, 8] = self.fx(ta[conta, 6], ta[conta, 7])  # k3
                ta[conta, 9] = ta[conta, 0] + h  # x+h
                ta[conta, 10] = ta[conta, 1] + h * ta[conta, 8]  # y+k3h
                ta[conta, 11] = self.fx(ta[conta, 9], ta[conta, 10])  # k4
            conta += 1
        # Creo un frame para poner la tabla en la que muestro mis iteraciones
        tablaframe = Frame(self.venUser, width=480, height=235)
        tablaframe.place(x=3, y=310)
        tablaframe.grid_propagate(False)
        # Utilizo un Treeview para poner la tabla, esta lineas son de configuracion
        tree = ttk.Treeview(tablaframe, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12), height=10, show="headings")
        tree.pack(side='left')
        tree.column('#1', width=100, anchor='c')
        tree.column('#2', width=100, anchor='c')
        tree.column('#3', width=100, anchor='c')
        tree.column('#4', width=100, anchor='c')
        tree.column('#5', width=100, anchor='c')
        tree.column('#6', width=100, anchor='c')
        tree.column('#7', width=100, anchor='c')
        tree.column('#8', width=100, anchor='c')
        tree.column('#9', width=100, anchor='c')
        tree.column('#10', width=100, anchor='c')
        tree.column('#11', width=100, anchor='c')
        tree.column('#12', width=100, anchor='c')
        tree.heading(1, text="Xn")
        tree.heading(2, text="Yn")
        tree.heading(3, text="k1")
        tree.heading(4, text="x+h/2")
        tree.heading(5, text="y+k1h/2")
        tree.heading(6, text="k2")
        tree.heading(7, text="x+h/2")
        tree.heading(8, text="y+k2h/2")
        tree.heading(9, text="k3")
        tree.heading(10, text="x+h")
        tree.heading(11, text="y+k3h")
        tree.heading(12, text="k4")
        scroll = ttk.Scrollbar(tablaframe, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        # con la matriz creada anteriormente lleno el treeview
        for val in ta:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9], val[10], val[11]))
        # print (ta)
    def pafuera(self):
        sys.exit(1)

#s=MenuUnidad3()