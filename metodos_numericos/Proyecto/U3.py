# -*- coding: utf-8 -*-
#!/usr/bin/env python

from tkinter import *
#from ttk import Combobox,Treeview
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sys


class MenuUnidad3:
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
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial", 15), width=1000,
                       height=2)
        lblEti.place(x=0, y=(550))
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial", 15), width=1000,
                       height=2)
        lblEti.place(x=0, y=(200))
        lblEti = Label(self.venUser, text="Unidad 3: Métodos Iterativos", fg="navy", bg="SkyBlue2",
                       font=("Arial", 36))
        lblEti.place(x=250, y=(0))
        lblSol = Label(self.venUser, text="Métodos Iterativos", fg="navy", bg="SkyBlue2",
                       font=("Arial", 24))
        lblSol.place(x=350, y=(50))
        #CAJAS DE TEXTO PARA SOLUCION DE ECUACIONES X, Y y Resultado
        self.x= IntVar()
        self.xn = Entry(self.venUser, textvariable=self.x, width=5)
        self.xn.place(x=250, y=(110))
        self.x11 = IntVar()
        self.cx11 = Entry(self.venUser, textvariable=self.x11, width=5)
        self.cx11.place(x=50, y=(110))
        self.x12 = IntVar()
        self.cx12 = Entry(self.venUser, textvariable=self.x12, width=5)
        self.cx12.place(x=90, y=(110))
        self.x13 = IntVar()
        self.cx13 = Entry(self.venUser, textvariable=self.x13, width=5)
        self.cx13.place(x=130, y=(110))
        self.x14 = IntVar()
        self.cx14 = Entry(self.venUser, textvariable=self.x14, width=5)
        self.cx14.place(x=170, y=(110))
        self.x21 = IntVar()
        self.cx21 = Entry(self.venUser, textvariable=self.x21, width=5)
        self.cx21.place(x=50, y=(130))
        self.x22 = IntVar()
        self.cx22 = Entry(self.venUser, textvariable=self.x22, width=5)
        self.cx22.place(x=90, y=(130))
        self.x23 = IntVar()
        self.cx23 = Entry(self.venUser, textvariable=self.x23, width=5)
        self.cx23.place(x=130, y=(130))
        self.x24 = IntVar()
        self.cx24 = Entry(self.venUser, textvariable=self.x24, width=5)
        self.cx24.place(x=170, y=(130))
        self.x31 = IntVar()
        self.cx31 = Entry(self.venUser, textvariable=self.x31, width=5)
        self.cx31.place(x=50, y=(150))
        self.x32 = IntVar()
        self.cx32 = Entry(self.venUser, textvariable=self.x32, width=5)
        self.cx32.place(x=90, y=(150))
        self.x33 = IntVar()
        self.cx33 = Entry(self.venUser, textvariable=self.x33, width=5)
        self.cx33.place(x=130, y=(150))
        self.x34 = IntVar()
        self.cx34 = Entry(self.venUser, textvariable=self.x34, width=5)
        self.cx34.place(x=170, y=(150))
        self.x41 = IntVar()
        self.cx41 = Entry(self.venUser, textvariable=self.x41, width=5)
        self.cx41.place(x=50, y=(170))
        self.x42 = IntVar()
        self.cx42 = Entry(self.venUser, textvariable=self.x42, width=5)
        self.cx42.place(x=90, y=(170))
        self.x43 = IntVar()
        self.cx43 = Entry(self.venUser, textvariable=self.x43, width=5)
        self.cx43.place(x=130, y=(170))
        self.x44 = IntVar()
        self.cx44 = Entry(self.venUser, textvariable=self.x44, width=5)
        self.cx44.place(x=170, y=(170))
        self.xo1 = IntVar()
        self.co1 = Entry(self.venUser, textvariable=self.xo1, width=5, bg='light green')
        self.co1.place(x=210, y=(110))
        self.xo2 = IntVar()
        self.co2 = Entry(self.venUser, textvariable=self.xo2, width=5, bg='light green')
        self.co2.place(x=210, y=(130))
        self.xo3 = IntVar()
        self.co3 = Entry(self.venUser, textvariable=self.xo3, width=5, bg='light green')
        self.co3.place(x=210, y=(150))
        self.xo4 = IntVar()
        self.co4 = Entry(self.venUser, textvariable=self.xo4, width=5, bg='light green')
        self.co4.place(x=210, y=(170))

        #METODOS CON INTERVALOS
        lblSol = Label(self.venUser, text="Métodos ecuaciones no lineales", fg="navy", bg="SkyBlue2",
                       font=("Arial", 24))
        lblInt = Label(self.venUser, text="Valores iniciales=         x a        y                                  Tolerancia               ", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblSol.place(x=450, y=(200))
        lblInt.place(x=0, y=(252))
        self.x1 = DoubleVar()
        self.x1e = Entry(self.venUser, textvariable=self.x1, width=5, )
        self.x1e.place(x=160, y=(257))
        self.y1 = DoubleVar()
        self.y1n = Entry(self.venUser, textvariable=self.y1, width=5, )
        self.y1n.place(x=225, y=(257))
        self.z1 = DoubleVar()
        self.z1n = Entry(self.venUser, textvariable=self.z1, width=5, )
        self.z1n.place(x=285, y=(257))
        self.w1 = DoubleVar()
        self.w1n = Entry(self.venUser, textvariable=self.w1, width=5, )
        self.w1n.place(x=345, y=(257))
        self.IntTol = DoubleVar()
        self.IntTole = Entry(self.venUser, textvariable=self.IntTol, width=5, )
        self.IntTole.place(x=550, y=(257))
        lblSupExp = Label(self.venUser, text="Adecua la expresion a tu problema:       x^       +       y^       +       x^       +       y^       +       x^       y+       y^       x+        =0", fg="navy", bg="SkyBlue2",
                       font=("Arial", 14))
        lblSupExp.place(x=0, y=(280))
        self.Fx1 = IntVar()
        self.Fx1n = Entry(self.venUser, textvariable=self.Fx1, width=4, )
        self.Fx1n.place(x=303, y=(285))
        self.Ex1 = IntVar()
        self.Ex1n = Entry(self.venUser, textvariable=self.Ex1, width=4, )
        self.Ex1n.place(x=355, y=(285))
        self.Fy1 = IntVar()
        self.Fy1n = Entry(self.venUser, textvariable=self.Fy1, width=4, )
        self.Fy1n.place(x=400, y=(285))
        self.Ey1 = IntVar()
        self.Ey1n = Entry(self.venUser, textvariable=self.Ey1, width=4, )
        self.Ey1n.place(x=450, y=(285))
        self.Fx2 = IntVar()
        self.Fx2n = Entry(self.venUser, textvariable=self.Fx2, width=4, )
        self.Fx2n.place(x=498, y=(285))
        self.Ex2 = IntVar()
        self.Ex2n = Entry(self.venUser, textvariable=self.Ex2, width=4, )
        self.Ex2n.place(x=548, y=(285))
        self.Fy2 = IntVar()
        self.Fy2n = Entry(self.venUser, textvariable=self.Fy2, width=4, )
        self.Fy2n.place(x=595, y=(285))
        self.Ey2 = IntVar()
        self.Ey2n = Entry(self.venUser, textvariable=self.Ey2, width=4, )
        self.Ey2n.place(x=648, y=(285))
        self.Fxy = IntVar()
        self.Fxyn = Entry(self.venUser, textvariable=self.Fxy, width=4, )
        self.Fxyn.place(x=690, y=(285))
        self.Pxy = IntVar()
        self.Pxyn = Entry(self.venUser, textvariable=self.Pxy, width=4, )
        self.Pxyn.place(x=740, y=(285))
        self.Fxy2 = IntVar()
        self.Fxy2n = Entry(self.venUser, textvariable=self.Fxy2, width=4, )
        self.Fxy2n.place(x=795, y=(285))
        self.Pxy2 = IntVar()
        self.Pxy2n = Entry(self.venUser, textvariable=self.Pxy2, width=4, )
        self.Pxy2n.place(x=845, y=(285))
        self.num = IntVar()
        self.numn = Entry(self.venUser, textvariable=self.num, width=4, )
        self.numn.place(x=903, y=(285))
        #SEGUNDA ECUACION
        lblSupExp1 = Label(self.venUser,
                          text="Adecua la expresion a tu problema:       x^       +       y^       +       x^       +       y^       +       x^       y+       y^       x+        =0",
                          fg="navy", bg="SkyBlue2",
                          font=("Arial", 14))
        lblSupExp1.place(x=0, y=(310))
        self.Fx11 = IntVar()
        self.Fx1n1 = Entry(self.venUser, textvariable=self.Fx11, width=4, )
        self.Fx1n1.place(x=303, y=(315))
        self.Ex11 = IntVar()
        self.Ex1n1 = Entry(self.venUser, textvariable=self.Ex11, width=4, )
        self.Ex1n1.place(x=355, y=(315))
        self.Fy11 = IntVar()
        self.Fy1n1 = Entry(self.venUser, textvariable=self.Fy11, width=4, )
        self.Fy1n1.place(x=400, y=(315))
        self.Ey11 = IntVar()
        self.Ey1n1 = Entry(self.venUser, textvariable=self.Ey11, width=4, )
        self.Ey1n1.place(x=450, y=(315))
        self.Fx21 = IntVar()
        self.Fx2n1 = Entry(self.venUser, textvariable=self.Fx21, width=4, )
        self.Fx2n1.place(x=498, y=(315))
        self.Ex21 = IntVar()
        self.Ex2n1 = Entry(self.venUser, textvariable=self.Ex21, width=4, )
        self.Ex2n1.place(x=548, y=(315))
        self.Fy21 = IntVar()
        self.Fy2n1 = Entry(self.venUser, textvariable=self.Fy21, width=4, )
        self.Fy2n1.place(x=595, y=(315))
        self.Ey21 = IntVar()
        self.Ey2n1 = Entry(self.venUser, textvariable=self.Ey21, width=4, )
        self.Ey2n1.place(x=648, y=(315))
        self.Fxy1 = IntVar()
        self.Fxyn1 = Entry(self.venUser, textvariable=self.Fxy1, width=4, )
        self.Fxyn1.place(x=690, y=(315))
        self.Pxy1 = IntVar()
        self.Pxyn1 = Entry(self.venUser, textvariable=self.Pxy1, width=4, )
        self.Pxyn1.place(x=740, y=(315))
        self.Fxy21 = IntVar()
        self.Fxy2n1 = Entry(self.venUser, textvariable=self.Fxy21, width=4, )
        self.Fxy2n1.place(x=795, y=(315))
        self.Pxy21 = IntVar()
        self.Pxy2n1 = Entry(self.venUser, textvariable=self.Pxy21, width=4, )
        self.Pxy2n1.place(x=845, y=(315))
        self.num1 = IntVar()
        self.numn1 = Entry(self.venUser, textvariable=self.num1, width=4, )
        self.numn1.place(x=903, y=(315))
        #COMBOBOX
        self.comboExample = ttk.Combobox(self.venUser,values=["Metodo de Jacobi","Gauss-Seidel","         "],state="readonly")
        self.comboExample.place(x=350, y=(115))
        self.comboExample.bind("<<ComboboxSelected>>", self.Eleccion_metodo_resolverE)
        self.comboIntervalos = ttk.Combobox(self.venUser,
                                         values=["Metodo de Newton-Raphson", "Metodo de punto fijo",
                                                 "        "], state="readonly")
        self.comboIntervalos.place(x=50, y=(230))
        self.comboIntervalos.bind("<<ComboboxSelected>>", self.Eleccion_metodo_resolverE)
        btnSalir = Button(self.venUser, text="Salir", bg='grey', command=self.pafuera,width=20,height=2)
        btnSalir.place(x=550, y=550)
        height = 5
        self.venUser.mainloop()

    def Eleccion_metodo_resolverE(self,event):
        lblx = Label(self.venUser, fg="navy", bg="#ffffff",
                     font=("Arial", 12),width=1000,height=3)
        lblx.place(x=479, y=(100))
        lblRaiz = Label(self.venUser, text="                                                                         ", fg="navy",
                        bg="SkyBlue2",
                        font=("Arial", 14))
        lblRaiz.place(x=700, y=(252))
        if self.comboIntervalos.get()=="Metodo de Newton-Raphson":
            self.newton()
        if self.comboExample.get()=="Metodo de Jacobi":
            self.jacobi1()
        if self.comboExample.get()=="Gauss-Seidel":
            self.Gauss1()
        if self.comboIntervalos.get()=="Metodo de punto fijo":
            self.punto_fijo()
    def fx(self,x,y):
        Fx1,Ex1,Fy1,Ey1,Fx2,Ex2,Fy2,Ey2=float(self.Fx1n.get()),float(self.Ex1n.get()),float(self.Fy1n.get()),float(self.Ey1n.get()),float(self.Fx2n.get()),float(self.Ex2n.get()),float(self.Fy2n.get()),float(self.Ey2n.get())
        Fxy1,Exy1,Fxy2,Exy2, num=float(self.Fxyn.get()),float(self.Pxyn.get()),float(self.Fxy2n.get()),float(self.Pxy2n.get()),int(self.numn.get())
        Fx11, Ex11, Fy11, Ey11, Fx21, Ex21, Fy21, Ey21 = float(self.Fx1n1.get()), float(self.Ex1n1.get()), float(
            self.Fy1n1.get()), float(self.Ey1n1.get()), float(self.Fx2n1.get()), float(self.Ex2n1.get()), float(
            self.Fy2n1.get()), float(self.Ey2n1.get())
        Fxy11, Exy11, Fxy21, Exy21, num1 = float(self.Fxyn1.get()), float(self.Pxyn1.get()), float(self.Fxy2n1.get()), float(
            self.Pxy2n1.get()), int(self.numn1.get())
        # print (Fx1,Ex1,Fy1,Ey1,Fx2,Ex2,Fy2,Ey2)
        #print (Fx1,Ex1,Fy1,Ey1,Fx2,Ex2,Fy2,Ey2)
        #print(Fxy1,Exy1,Fxy2,Exy2, num)
        return np.array([Fx1*x**Ex1+Fx2*x**Ex2+Fy2*y**Ey2+Fy1*y**Ey1+Fxy1*y*x**Exy1+Fxy2*x*y**Exy2+num,Fx11*x**Ex11+Fx21*x**Ex21+Fy21*y**Ey21+Fy11*y**Ey11+Fxy11*y*x**Exy11+Fxy21*x*y**Exy21+num1])
    def ufx(self,x,y):
        Fx1, Ex1, Fy1, Ey1, Fx2, Ex2, Fy2, Ey2 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fy1n.get()), float(self.Ey1n.get()), float(self.Fx2n.get()), float(self.Ex2n.get()), float(
            self.Fy2n.get()), float(self.Ey2n.get())
        Fxy1, Exy1, Fxy2, Exy2, num = float(self.Fxyn.get()), float(self.Pxyn.get()), float(self.Fxy2n.get()), float(
            self.Pxy2n.get()), int(self.numn.get())
        return Fx1 * x ** Ex1 + Fx2 * x ** Ex2 + Fy2 * y ** Ey2 + Fy1 * y ** Ey1 + Fxy1 * y * x ** Exy1 + Fxy2 * x * y ** Exy2 + num
    def vfx(self,x,y):
        Fx11, Ex11, Fy11, Ey11, Fx21, Ex21, Fy21, Ey21 = float(self.Fx1n1.get()), float(self.Ex1n1.get()), float(
            self.Fy1n1.get()), float(self.Ey1n1.get()), float(self.Fx2n1.get()), float(self.Ex2n1.get()), float(
            self.Fy2n1.get()), float(self.Ey2n1.get())
        Fxy11, Exy11, Fxy21, Exy21, num1 = float(self.Fxyn1.get()), float(self.Pxyn1.get()), float(
            self.Fxy2n1.get()), float(
            self.Pxy2n1.get()), int(self.numn1.get())
        return Fx11*x**Ex11+Fx21*x**Ex21+Fy21*y**Ey21+Fy11*y**Ey11+Fxy11*y*x**Exy11+Fxy21*x*y**Exy21+num1
    def matrizInversa(self,x,y):
        Fx1, Ex1, Fy1, Ey1, Fx2, Ex2, Fy2, Ey2 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fy1n.get()), float(self.Ey1n.get()), float(self.Fx2n.get()), float(self.Ex2n.get()), float(
            self.Fy2n.get()), float(self.Ey2n.get())
        Fxy1, Exy1, Fxy2, Exy2, num = float(self.Fxyn.get()), float(self.Pxyn.get()), float(self.Fxy2n.get()), float(
            self.Pxy2n.get()), int(self.numn.get())
        Fx11, Ex11, Fy11, Ey11, Fx21, Ex21, Fy21, Ey21 = float(self.Fx1n1.get()), float(self.Ex1n1.get()), float(
            self.Fy1n1.get()), float(self.Ey1n1.get()), float(self.Fx2n1.get()), float(self.Ex2n1.get()), float(
            self.Fy2n1.get()), float(self.Ey2n1.get())
        Fxy11, Exy11, Fxy21, Exy21, num1 = float(self.Fxyn1.get()), float(self.Pxyn1.get()), float(
            self.Fxy2n1.get()), float(
            self.Pxy2n1.get()), int(self.numn1.get())
        return np.array([[Ex1*Fx1*x**(Ex1-1)+Ex2*Fx2*x**(Ex2-1)+Exy1*Fxy1*y*x**(Exy1-1)+Fxy2*y**(Exy2),Ey2*Fy2*y**(Ey2-1)+Ey1*Fy1*y**(Ey1-1)+Fxy1*x**Exy1+Exy2*Fxy2*x*y**(Exy2-1)],
                         [Ex11*Fx11*x**(Ex11-1)+Ex21*Fx21*x**(Ex2-1)+Exy1*Fxy1*y*x**(Exy1-1)+Fxy2*y**(Exy2),Ey21*Fy21*y**(Ey21-1)+Ey11*Fy11*y**(Ey11-1)+Fxy11*x**Exy11+Exy21*Fxy21*x*y**(Exy21-1)]])
    def dux(self,x,y):
        Fx1, Ex1, Fy1, Ey1, Fx2, Ex2, Fy2, Ey2 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fy1n.get()), float(self.Ey1n.get()), float(self.Fx2n.get()), float(self.Ex2n.get()), float(
            self.Fy2n.get()), float(self.Ey2n.get())
        Fxy1, Exy1, Fxy2, Exy2, num = float(self.Fxyn.get()), float(self.Pxyn.get()), float(self.Fxy2n.get()), float(
            self.Pxy2n.get()), int(self.numn.get())
        return Ex1*Fx1*x**(Ex1-1)+Ex2*Fx2*x**(Ex2-1)+Exy1*Fxy1*y*x**(Exy1-1)+Fxy2*y**(Exy2)
    def dvx(self,x,y):
        Fx11, Ex11, Fy11, Ey11, Fx21, Ex21, Fy21, Ey21 = float(self.Fx1n1.get()), float(self.Ex1n1.get()), float(
            self.Fy1n1.get()), float(self.Ey1n1.get()), float(self.Fx2n1.get()), float(self.Ex2n1.get()), float(
            self.Fy2n1.get()), float(self.Ey2n1.get())
        Fxy11, Exy11, Fxy21, Exy21, num1 = float(self.Fxyn1.get()), float(self.Pxyn1.get()), float(
            self.Fxy2n1.get()), float(
            self.Pxy2n1.get()), int(self.numn1.get())
        return Ex11*Fx11*x**(Ex11-1)+Ex21*Fx21*x**(Ex21-1)+Exy11*Fxy11*y*x**(Exy11-1)+Fxy21*y**(Exy21)
    def duy(self,x,y):
        Fx1, Ex1, Fy1, Ey1, Fx2, Ex2, Fy2, Ey2 = float(self.Fx1n.get()), float(self.Ex1n.get()), float(
            self.Fy1n.get()), float(self.Ey1n.get()), float(self.Fx2n.get()), float(self.Ex2n.get()), float(
            self.Fy2n.get()), float(self.Ey2n.get())
        Fxy1, Exy1, Fxy2, Exy2, num = float(self.Fxyn.get()), float(self.Pxyn.get()), float(self.Fxy2n.get()), float(
            self.Pxy2n.get()), int(self.numn.get())
        return Ey2 * Fy2 * y ** (Ey2 - 1) + Ey1 * Fy1 * y ** (Ey1 - 1) + Fxy1 * x ** Exy1 + Exy2 * Fxy2 * x * y ** (Exy2 - 1)
    def dvy(self,x,y):
        Fx11, Ex11, Fy11, Ey11, Fx21, Ex21, Fy21, Ey21 = float(self.Fx1n1.get()), float(self.Ex1n1.get()), float(
            self.Fy1n1.get()), float(self.Ey1n1.get()), float(self.Fx2n1.get()), float(self.Ex2n1.get()), float(
            self.Fy2n1.get()), float(self.Ey2n1.get())
        Fxy11, Exy11, Fxy21, Exy21, num1 = float(self.Fxyn1.get()), float(self.Pxyn1.get()), float(
            self.Fxy2n1.get()), float(
            self.Pxy2n1.get()), int(self.numn1.get())
        return Ey21*Fy21*y**(Ey21-1)+Ey11*Fy11*y**(Ey11-1)+Fxy11*x**Exy11+Exy21*Fxy21*x*y**(Exy21-1)
    def despejefx(self,x,y):
        Fx1, Ex1, Fy1, Ey1, Fx2, Ex2, Fy2, Ey2 = int(self.Fx1n.get()), int(self.Ex1n.get()), int(
            self.Fy1n.get()), int(self.Ey1n.get()), int(self.Fx2n.get()), int(self.Ex2n.get()), int(
            self.Fy2n.get()), int(self.Ey2n.get())
        Fxy1, Exy1, Fxy2, Exy2, num = int(self.Fxyn.get()), int(self.Pxyn.get()), int(self.Fxy2n.get()), int(
            self.Pxy2n.get()), int(self.numn.get())
        if Fx1!=0:
            despx=(((-Fx2*x**Ex2-Fy2*y**Ey2-Fy1*y**Ey1-Fxy1*y*x**Exy1-Fxy2*x*y**Exy2-num)/Fx1))**(1/Ex1)
        if Fxy1!=0:
            despx=((-Fx1*x**Ex1-Fx2*x**Ex2-Fy2*y**Ey2-Fy1*y**Ey1-Fxy2*x*y**Exy2-num)/(Fxy1*y))**(1/Exy1)
        return despx
    def despejefy(self,x,y):
        Fx1, Ex1, Fy1, Ey1, Fx2, Ex2, Fy2, Ey2 = int(self.Fx1n1.get()), int(self.Ex1n1.get()), int(
            self.Fy1n1.get()), int(self.Ey1n1.get()), int(self.Fx2n1.get()), int(self.Ex2n1.get()), int(
            self.Fy2n1.get()), int(self.Ey2n1.get())
        Fxy1, Exy1, Fxy2, Exy2, num = int(self.Fxyn1.get()), int(self.Pxyn1.get()), int(self.Fxy2n1.get()), int(
            self.Pxy2n1.get()), int(self.numn1.get())
        if Fy1!=0:
            despx=(((-Fx2*x**Ex2-Fy2*y**Ey2-Fx1*x**Ex1-Fxy1*y*x**Exy1-Fxy2*x*y**Exy2-num)/Fy1))**(1/Ey1)
        if Fxy2!=0:
            despx=(((-Fx1*x**Ex1-Fx2*x**Ex2-Fy2*y**Ey2-Fy1*y**Ey1-Fxy1*y*x**Exy1-num)/(Fxy2*x))**(1/Exy2))
        return despx
    def punto_fijo(self):
        x1, y1 = float(self.x1.get()), float(self.y1.get())
        tol = float(self.IntTole.get())
        niter=0
        imax=100
        error=100
        while error>tol or niter>imax or error>500:
            ea=x1
            x1=self.despejefx(x1,y1)
            print (x1)
            y1=self.despejefy(x1,y1)
            print (y1)
            print (x1,y1)
            error = abs((x1 - ea) / x1) * 100
            niter+=1
        lblx = Label(self.venUser, text=("Iteraciones=", niter), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(407))
        lblx = Label(self.venUser, text=("Raices x=", x1), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(437))
        lblx = Label(self.venUser, text=("Raices y=", y1), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(457))

    def newton(self):
        x1,y1=float(self.x1.get()),float(self.y1.get())
        tol = float(self.IntTole.get())
        niter = 0
        imax = 1
        error = 100
        while error>tol or niter>imax or error>500:
            ea = x1
            dux=self.dux(x1,y1)
            dvx=self.dvx(x1,y1)
            duy=self.duy(x1,y1)
            dvy=self.dvy(x1,y1)
            print (dux,dvx,duy,dvy)
            niter+=1
            dtj=dux*dvy-duy*dvx
            u=self.ufx(x1,y1)
            v=self.vfx(x1,y1)
            print (u,v,dtj)
            x1=x1-((u*dvy-v*duy)/dtj)
            y1=y1-((v*dux-u*dvy)/dtj)
            print (x1,y1)
            error = abs((x1 - ea) / x1) * 100
            niter += 1
            if error<tol:
                break
        lblx = Label(self.venUser, text=("Iteraciones=", niter), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(407))
        lblx = Label(self.venUser, text=("Raices x=", x1), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(437))
        lblx = Label(self.venUser, text=("Raices y=", y1), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(457))
    def jacobi(self):
        n = int(self.xn.get())
        x1, y1 = float(self.x1.get()), float(self.y1.get())
        b=np.zeros(n)
        A=np.zeros((n,n))
        A[0][0]=int(self.x11.get())
        A[0][1]=int(self.x12.get())
        b[0]=int(self.xo1.get())
        A[1][0] = int(self.x21.get())
        A[1][1] = int(self.x22.get())
        b[1]= int(self.xo2.get())
        if n>2:
            A[2][0] = int(self.x31.get())
            A[2][1] = int(self.x32.get())
            A[2][2] = int(self.x33.get())
            b[2] = int(self.xo3.get())
            A[0][2] = int(self.x13.get())
            A[1][2] = int(self.x23.get())
            if n>3:
                A[3][0] = int(self.x41.get())
                A[3][1] = int(self.x42.get())
                A[3][2] = int(self.x43.get())
                A[3][3] = int(self.x44.get())
                b[3] = int(self.xo4.get())
                A[2][3] = int(self.x34.get())
                A[0][3] = int(self.x14.get())
                A[1][3] = int(self.x24.get())
        tol=float(self.IntTole.get())
        error=100000
        nitermax=200
        print(n)
        #A=np.random.rand(n,n)
        #b=np.random.rand(n,)
        alpha=3*n
        ADD=np.dot(A,A.T)+alpha*np.identity(n)
        A=ADD
        print (A)
        determ=np.linalg.det(A)
        print (determ)
        n=len(b)
        count=0
        for i in range(n):
            Aii=A[i][i]
            suma=0
            for j in range(n):
                if i!=j:
                    suma=suma+abs(A[i][j])
            if Aii>suma:
                print("la fila",i,"es Diagonal Dominante")
                count += 1
            else:
                print("La fila",i,"No es diagonal domiante")
                break
        if count==n:
            print("La matriz es diagonal dominante y el metodo iterativo convergira")
        else:
            print("La matriz no es diagonal dominante y el metodo iterativo no puede convergir")
        n=len(A)
        x=np.zeros(n)
        x1=np.zeros(n)
        niter=0
        Niter=[]
        Error=[]

        while niter<nitermax and error>tol:
            for i in range(n):
                d=b[i]
                for j in range(n):
                    if i!=j:
                        d=d-A[i][j]*x[j]
                x[i]=d/A[i][j]
            error=np.linalg.norm(x-x1)
            x1=np.copy(x)
            print("Iteracion: ",niter)
            print(x)
            print ("Error en la iteracion ", niter, "es:",error)
            niter+=1
            Niter.append(niter)
            Error.append(error)
        print (Niter)
        print (Error)
        lblx = Label(self.venUser, text=("Raices", x), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(107))
        lblx = Label(self.venUser, text=("NumeroIteraciones",Niter), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(157))
        lblx = Label(self.venUser, text=("Errores: ",Error), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(177))
        x=Niter
        y=Error
        plt.plot(x,y, label="Variacion del Error")
        plt.plot()
        plt.xlabel("No. Iteraciones")
        plt.ylabel("Error Calculado")
        plt.legend()
        plt.grid(True)
        plt.show()
    def gaussseidel(self):
        n = int(self.xn.get())
        b = np.zeros(n)
        A = np.zeros((n, n))
        A[0][0] = int(self.x11.get())
        A[0][1] = int(self.x12.get())
        b[0] = int(self.xo1.get())
        A[1][0] = int(self.x21.get())
        A[1][1] = int(self.x22.get())
        b[1] = int(self.xo2.get())
        if n > 2:
            A[2][0] = int(self.x31.get())
            A[2][1] = int(self.x32.get())
            A[2][2] = int(self.x33.get())
            b[2] = int(self.xo3.get())
            A[0][2] = int(self.x13.get())
            A[1][2] = int(self.x23.get())
            if n > 3:
                A[3][0] = int(self.x41.get())
                A[3][1] = int(self.x42.get())
                A[3][2] = int(self.x43.get())
                A[3][3] = int(self.x44.get())
                b[3] = int(self.xo4.get())
                A[2][3] = int(self.x34.get())
                A[0][3] = int(self.x14.get())
                A[1][3] = int(self.x24.get())
        tol = float(self.IntTole.get())
        tol=float(self.IntTole.get())
        imax=200
        error=100

        x=np.zeros(n+1)
        iteraciones=0
        x0, y0,z0,w0 = float(self.x1.get()), float(self.y1.get()),float(self.z1.get()),float(self.w1.get())
        for i in range(n):
            inc=A[i][i]
            b[i]=b[i]/inc
            for j in range(n):
                if j!=i:
                    A[i][j]=-A[i][j]/inc
                else:
                    A[i][j]=0
        while error>tol or iteraciones>=imax:
            errorA=x0
            for i in range(n):
                if i==0:
                    x0=b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                    print (x0,y0,z0)
                if i==1:
                    y0= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                    #print y0
                if i==2:
                    z0= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                    #print z0
                error=abs((x0-errorA)/x0)*100
            iteraciones+=1
        lblx = Label(self.venUser, text=("Iteraciones=", iteraciones), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(107))
        lblx = Label(self.venUser, text=("Raices x=", x0), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(137))
        lblx = Label(self.venUser, text=("Raices y=", y0), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(157))
        lblx = Label(self.venUser, text=("Raices z=", z0), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(177))
    def Gauss1(self):
        n = int(self.xn.get())
        b = np.zeros(n)
        A = np.zeros((n, n))
        a=np.zeros((100, 10))
        A[0][0] = int(self.x11.get())
        A[0][1] = int(self.x12.get())
        b[0] = int(self.xo1.get())
        A[1][0] = int(self.x21.get())
        A[1][1] = int(self.x22.get())
        b[1] = int(self.xo2.get())
        if n > 2:
            A[2][0] = int(self.x31.get())
            A[2][1] = int(self.x32.get())
            A[2][2] = int(self.x33.get())
            b[2] = int(self.xo3.get())
            A[0][2] = int(self.x13.get())
            A[1][2] = int(self.x23.get())
            if n > 3:
                A[3][0] = int(self.x41.get())
                A[3][1] = int(self.x42.get())
                A[3][2] = int(self.x43.get())
                A[3][3] = int(self.x44.get())
                b[3] = int(self.xo4.get())
                A[2][3] = int(self.x34.get())
                A[0][3] = int(self.x14.get())
                A[1][3] = int(self.x24.get())
        tol = float(self.IntTole.get())
        imax = 200
        error = 100
        iteraciones = 0
        x0, y0, z0, w0 = float(self.x1.get()), float(self.y1.get()), float(self.z1.get()), float(self.w1.get())
        for i in range(n):
            inc = A[i][i]
            b[i] = b[i] / inc
            for j in range(n):
                if j != i:
                    A[i][j] = -A[i][j] / inc
                else:
                    A[i][j] = 0
        while error>tol and iteraciones<=imax:
            ea=x0
            a[iteraciones][0]=iteraciones
            a[iteraciones][1] = x0
            a[iteraciones][2] = y0
            if n>2:
                a[iteraciones][3] = z0
                if n>3:
                    a[iteraciones][4] = w0
            if n==2:
                for i in range(n):
                    if i==0:
                        x0=b[i]+A[i][0]*x0+A[i][1]*y0

                    if i==1:
                        y0= b[i]+A[i][0]*x0+A[i][1]*y0
                a[iteraciones][5] = x0
                a[iteraciones][6] = y0
                #print(x0, y0)
            elif n==3:
                for i in range(n):
                    if i==0:
                        x0=b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                        #print (x0,y0,z0)
                    if i==1:
                        y0= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                        #print y0
                    if i==2:
                        z0= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                        #print z0
                a[iteraciones][5] = x0
                a[iteraciones][6] = y0
                a[iteraciones][7] = z0
            elif n==4:
                for i in range(n):
                    if i==0:
                        x0=b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0+A[i][3]*w0
                        print (x0,y0,z0)
                    if i==1:
                        y0= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0+A[i][3]*w0
                        #print y0
                    if i==2:
                        z0= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0+A[i][3]*w0
                        #print z0
                    if i==3:
                        w0 = b[i] + A[i][0] * x0 + A[i][1] * y0 + A[i][2] * z0 + A[i][3] * w0
                a[iteraciones][5] = x0
                a[iteraciones][6] = y0
                a[iteraciones][7] = z0
                a[iteraciones][8] = w0
            error = abs((x0 - ea) / x0) * 100
            a[iteraciones][9] = y0
            iteraciones+=1
        tabla = Frame(self.venUser, width=480, height=235)
        tabla.place(x=3, y=310)
        tabla.grid_propagate(False)
        tree = ttk.Treeview(tabla, columns=(1, 2, 3, 4, 5, 6,7,8,9,10), height=10, show="headings")
        tree.pack(side='left')
        tree.heading(1, text="Iteracion")
        tree.heading(2, text="Xi")
        tree.heading(3, text="Yi")
        tree.heading(4, text="Zi")
        tree.heading(5, text="Wi")
        tree.heading(6, text="Xi+1")
        tree.heading(7, text="Yi+1")
        tree.heading(8, text="Zi+1")
        tree.heading(9, text="Wi+1")
        tree.heading(10, text="Di")
        scroll = ttk.Scrollbar(tabla, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        for val in a:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5]))
        lblx = Label(self.venUser, text=("Iteraciones=", iteraciones), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(107))
        lblx = Label(self.venUser, text=("Raices x=", x0), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(127))
        lblx = Label(self.venUser, text=("Raices y=", y0), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(147))
        if n > 2:
            lblx = Label(self.venUser, text=("Raices z=", z0), fg="navy", bg="SkyBlue2",
                         font=("Arial", 12))
            lblx.place(x=500, y=(167))
            if n > 3:
                lblx = Label(self.venUser, text=("Raices w=", w0), fg="navy", bg="SkyBlue2",
                             font=("Arial", 12))
                lblx.place(x=500, y=(187))
    def jacobi1(self):
        n = int(self.xn.get())
        b = np.zeros(n)
        A = np.zeros((n, n))
        a=np.zeros((100, 10))
        A[0][0] = int(self.x11.get())
        A[0][1] = int(self.x12.get())
        b[0] = int(self.xo1.get())
        A[1][0] = int(self.x21.get())
        A[1][1] = int(self.x22.get())
        b[1] = int(self.xo2.get())
        if n > 2:
            A[2][0] = int(self.x31.get())
            A[2][1] = int(self.x32.get())
            A[2][2] = int(self.x33.get())
            b[2] = int(self.xo3.get())
            A[0][2] = int(self.x13.get())
            A[1][2] = int(self.x23.get())
            if n > 3:
                A[3][0] = int(self.x41.get())
                A[3][1] = int(self.x42.get())
                A[3][2] = int(self.x43.get())
                A[3][3] = int(self.x44.get())
                b[3] = int(self.xo4.get())
                A[2][3] = int(self.x34.get())
                A[0][3] = int(self.x14.get())
                A[1][3] = int(self.x24.get())
        tol = float(self.IntTole.get())
        imax = 200
        error = 100
        iteraciones = 0
        x0, y0, z0, w0 = float(self.x1.get()), float(self.y1.get()), float(self.z1.get()), float(self.w1.get())
        for i in range(n):
            inc = A[i][i]
            b[i] = b[i] / inc
            for j in range(n):
                if j != i:
                    A[i][j] = -A[i][j] / inc
                else:
                    A[i][j] = 0
        while error>tol and iteraciones<=imax:
            ea=x0
            a[iteraciones][0]=iteraciones
            a[iteraciones][1] = x0
            a[iteraciones][2] = y0
            if n>2:
                a[iteraciones][3] = z0
                if n>3:
                    a[iteraciones][4] = w0
            if n==2:
                for i in range(n):
                    if i==0:
                        x1=b[i]+A[i][0]*x0+A[i][1]*y0

                    if i==1:
                        y1= b[i]+A[i][0]*x0+A[i][1]*y0
                a[iteraciones][5] = x1
                a[iteraciones][6] = y1
                #print(x0, y0)
            elif n==3:
                for i in range(n):
                    if i==0:
                        x1=b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                        #print (x0,y0,z0)
                    if i==1:
                        y1= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                        #print y0
                    if i==2:
                        z1= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0
                        #print z0
                a[iteraciones][5] = x1
                a[iteraciones][6] = y1
                a[iteraciones][7] = z1
            elif n==4:
                for i in range(n):
                    if i==0:
                        x1=b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0+A[i][3]*w0
                        #print (x0,y0,z0)
                    if i==1:
                        y1= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0+A[i][3]*w0
                        #print y0
                    if i==2:
                        z1= b[i]+A[i][0]*x0+A[i][1]*y0+A[i][2]*z0+A[i][3]*w0
                        #print z0
                    if i==3:
                        w1 = b[i] + A[i][0] * x0 + A[i][1] * y0 + A[i][2] * z0 + A[i][3] * w0
                a[iteraciones][5] = x1
                a[iteraciones][6] = y1
                a[iteraciones][7] = z1
                a[iteraciones][8] = w1


            error = abs((x1 - ea) / x1) * 100
            a[iteraciones][9] = error
            iteraciones+=1
            x0 = x1
            y0 = y1
            if n > 2:
                z0 = z1
                if n > 3:
                    w0 = w1
        tabla = Frame(self.venUser, width=480, height=235)
        tabla.place(x=3, y=310)
        tabla.grid_propagate(False)
        tree = ttk.Treeview(tabla, columns=(1, 2, 3, 4, 5, 6,7,8,9,10), height=5, show="headings")
        tree.pack(side='left')
        tree.heading(1, text="Iteracion")
        tree.heading(2, text="Xi")
        tree.heading(3, text="Yi")
        tree.heading(4, text="Zi")
        tree.heading(5, text="Wi")
        tree.heading(6, text="Xi+1")
        tree.heading(7, text="Yi+1")
        tree.heading(8, text="Zi+1")
        tree.heading(9, text="Wi+1")
        tree.heading(10, text="Di")
        scroll = ttk.Scrollbar(tabla, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scroll.set)
        for val in a:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5]))
        lblx = Label(self.venUser, text=("Iteraciones=", iteraciones), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(107))
        lblx = Label(self.venUser, text=("Raices x=", x0), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(127))
        lblx = Label(self.venUser, text=("Raices y=", y0), fg="navy", bg="SkyBlue2",
                     font=("Arial", 12))
        lblx.place(x=500, y=(147))
        if n > 2:
            lblx = Label(self.venUser, text=("Raices z=", z0), fg="navy", bg="SkyBlue2",
                         font=("Arial", 12))
            lblx.place(x=500, y=(167))
            if n > 3:
                lblx = Label(self.venUser, text=("Raices w=", w0), fg="navy", bg="SkyBlue2",
                             font=("Arial", 12))
                lblx.place(x=500, y=(187))

    def pafuera(self):
        sys.exit(1)

#s=MenuUnidad3()