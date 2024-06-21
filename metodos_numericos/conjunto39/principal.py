# -*- coding: utf-8 -*-�
# #!/usr/bin/env python

#SE IMPORTAN LOS ARCHIVOS

from tkinter import *
#import ttk
#import tkMessageBox
#from ttk import *
import tkinter as tk
import cincopuntos as cp
import trespuntos as tp
import simpson13 as s1
import simpson38 as s3
import metodotrapecio as tra
import cuadraturagaussiana as cg
import internewton as ine
import lagrange as la
import regresion_lineal as rl
import minimos_cuadrados as mc
import igualacion as ig
import reduccion as re
import sustitucion as st
import puntofijo as pf
import biseccion as bi
import falsaposicion as fp
import grafico
import jacobi as ja
import gaussseidel as gs
import newton_ramphson as nr
import fijo as fi
import metodo_de_euler as me
import metodo_heun as mh
import metodo_taylor as mt
import runge_kutta as rk
#SE CREA UNA CLASE PRINCIPAL
class metodos:
    #SE EJECUTA LA VENTANA PRINCIPAL
    def interfaz(self):
        #SE CREA LA VENTANA Y UN MENU
        self.window = Tk()
        self.window.geometry("420x300")
        menu=tk.Menu(self.window)
        self.window.config(bg="blue")
        menu.add_command(label='unidad 1')
        #menu.add_command(label='unidad 2')
        #menu.add_command(label='unidad 3')

        desplegable=tk.Menu(menu,tearoff=0)
        #desplegable.add_command(label='punto fijo')
        #desplegable.add_command(label='newton - ramphson')

        #SE AGREGAN LOS APARTADOS QUE CONTENDRA LA FUNCION

        otro=tk.Menu(menu,tearoff=0)
        otro.add_command(label='metodo de reduccion',command=self.redu)
        otro.add_command(label='metodo de sustitucion',command=self.sus)
        otro.add_command(label='metodo de igualacion',command=self.igua)
        otromas=tk.Menu(menu,tearoff=0)
        otromas.add_command(label='biseccion',command=self.bis)
        otromas.add_command(label='falsa pocision',command=self.falsap)
        otromas.add_command(label='metodo de punto fijo',command=self.ejecutar)
        otromas.add_command(label='metodo grafico',command=self.graficos)
        unidad3 = tk.Menu(menu, tearoff=0)
        unidad3.add_command(label='punto fijo',command=self.fijo)
        unidad3.add_command(label='jacobi',command=self.jacobi)
        unidad3.add_command(label='newton - ramphson',command=self.rampson)
        unidad3.add_command(label='gauss - saidel',command=self.gauss)
        unidad4 = tk.Menu(menu, tearoff=0)
        unidad4.add_command(label='tres puntos',command=self.ventana_tes)
        unidad4.add_command(label='cinco puntos',command=self.ventana_cinco)
        unidad4.add_command(label='trapecio',command=self.ventana_trapecio)
        unidad4.add_command(label='simpson 1/3',command=self.ventana_simpson13)
        unidad4.add_command(label='simpson 3/8',command=self.ventana_simpson38)
        unidad4.add_command(label='cuadratura gaussiana',command=self.ventana_cuadratura_gaussiana)
        unidad5 = tk.Menu(menu, tearoff=0)
        unidad5.add_command(label='interpolacion de newton',command=self.newt)
        unidad5.add_command(label='interpolacion de lagrange',command=self.lagr)
        unidad5.add_command(label='regresion lineal', command=self.regre)
        unidad5.add_command(label='regresion minimos cuadrados',command=self.minimos)
        unidad6 = tk.Menu(menu, tearoff=0)
        unidad6.add_command(label='metodo de euler',command=self.euler)
        unidad6.add_command(label='error por taylor',command=self.taylor)
        unidad6.add_command(label='metodo de heun',command=self.eun)
        unidad6.add_command(label='metodo de runge - kutta', command=self.kutta)

        self.eti = Label(self.window, font=("ROCKWELL", 16), text="Instituto Tecnologico Superior").place(x=0, y=50)
        self.eti = Label(self.window, font=("ROCKWELL", 16), text="Zacarcas Sur").place(x=100, y=90)
        self.eti=Label(self.window, font=("ROCKWELL", 18), text="METODOS NUMERICOS").place(x=20,y=170)
        menu.add_cascade(label='unidad 2',menu=desplegable)
        menu.add_cascade(label='unidad 3', menu=unidad3)
        menu.add_cascade(label='unidad 4', menu=unidad4)
        menu.add_cascade(label='unidad 5', menu=unidad5)
        menu.add_cascade(label='unidad 6', menu=unidad6)
        desplegable.add_cascade(label='sistemas de ecuaciones', menu=otro)

        desplegable.add_cascade(label='metodos iterativos', menu=otromas)
        self.window.config(menu=menu)

        menu.add_command(label= 'salir')

        self.window = mainloop()
    #PROGRAMAS UNIDAD 6
    #METODO DE RUNGE - KUTTA
    def kutta(self):
        self.b = Toplevel()
        self.b.geometry("300x350")
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="funcion").place(x=50, y=25)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="punto inicial de x").place(x=50, y=75)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="numero de iteraciones").place(x=50, y=125)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="valor de paso").place(x=50, y=175)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="valor de y(0)").place(x=50, y=225)

        self.val = StringVar()
        v1 = Entry(self.b, textvariable=self.val).place(x=50, y=50)
        self.val1 = DoubleVar()
        v2 = Entry(self.b, textvariable=self.val1).place(x=50, y=100)
        self.val2 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val2).place(x=50, y=150)
        self.val3 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val3).place(x=50, y=200)
        self.val4 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val4).place(x=50, y=250)

        Button(self.b, text="resolver", command=self.runge).place(x=100, y=300)

        self.b = mainloop()
    def runge(self):
        rk.diferencial().kutta(self.val.get(),self.val1.get(),self.val2.get(),self.val3.get(),self.val4.get())
    #METODO DEL ERROR DE TAYLOR
    def taylor(self):
        self.b = Toplevel()
        self.b.geometry("300x350")
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="funcion de grado 2").place(x=50, y=25)


        self.val = StringVar()
        v1 = Entry(self.b, textvariable=self.val).place(x=50, y=50)


        Button(self.b, text="resolver", command=self.tay).place(x=100, y=300)

        self.b = mainloop()
    def tay(self):
        mt.diferencial().taylor(self.val.get())
    #METODO DE HEUN
    def eun(self):
        mh.diferencial().heun()

    #VENTANA DEL METODO DE EULER
    def euler(self):
        self.b = Toplevel()
        self.b.geometry("900x350")
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="funcion").place(x=50, y=25)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="punto inicial").place(x=50, y=75)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="punto final").place(x=50, y=125)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="valor de paso").place(x=50, y=175)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="valor de y(0)").place(x=50, y=225)

        self.val = StringVar()
        v1 = Entry(self.b, textvariable=self.val).place(x=50, y=50)
        self.val1 = DoubleVar()
        v2 = Entry(self.b, textvariable=self.val1).place(x=50, y=100)
        self.val2 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val2).place(x=50, y=150)
        self.val3 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val3).place(x=50, y=200)
        self.val4 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val4).place(x=50, y=250)

        Button(self.b, text="resolver", command=self.eul).place(x=100, y=300)

        self.b = mainloop()
    def eul(self):
        me.diferencial().euler(self.val.get(),self.val1.get(),self.val2.get(),self.val3.get(),self.val4.get())
    #VENTANAS DE LA UNIDAD 3
    def fijo(self):
        fi.jacob().ventana()
    def rampson(self):
        nr.ne().ventana()
    def jacobi(self):
        ja.jacob().ventana()
    def gauss(self):
        gs.jacob().ventana()

    #VENTANAS DE GRAFICO, FALSA POSICION, BISECCION Y PUNTO FIJO
    def graficos(self):
        self.g = Toplevel()

        self.g.geometry('350x200')
        # self.combo = ttk.Combobox(self.g)
        # self.combo['values'] = ("sen()", "cos()", "tan()", "cot()", "ln()", "e**x")
        # self.combo.current(1)  # set the selected item
        # self.combo.grid(column=0, row=0)

        self.g.geometry("350x300")
        self.eti = Label(self.g, font=("ROCKWELL", 14), text="punto inferior del intervalo").place(x=50, y=25)
        self.eti = Label(self.g, font=("ROCKWELL", 14), text="punto superior del intervalo").place(x=50, y=75)
        self.va = DoubleVar()
        v1 = Entry(self.g, textvariable=self.va).place(x=50, y=50)
        self.va1 = DoubleVar()
        v2 = Entry(self.g, textvariable=self.va1).place(x=50, y=100)
        Button(self.g, text="graficar", command=self.gra).place(x=50, y=150)

        # a=LabelFrame(self.g).place()
        # self.eti = Label(a, font=("ROCKWELL", 14), text="punto inferior del intervalo").place(x=50, y=150)
        # for widget in a.winfo_children():
        #   widget.destroy()
        # a.destroy()
        self.gr = mainloop()

    def gra(self):
        #        print self.combo.get()
        grafico.grafic().intervalo(self.va.get(), self.va1.get())
    #BISECCION
    def bis(self):
        self.b = Toplevel()
        self.b.geometry("900x350")
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="valor de xl").place(x=50, y=25)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="valor de xu").place(x=50, y=75)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="valor tolerancia de error").place(x=50, y=125)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="intervalo inferior").place(x=50, y=175)
        self.eti = Label(self.b, font=("ROCKWELL", 14), text="intervalo superior").place(x=50, y=225)

        self.val = DoubleVar()
        v1 = Entry(self.b, textvariable=self.val).place(x=50, y=50)
        self.val1 = DoubleVar()
        v2 = Entry(self.b, textvariable=self.val1).place(x=50, y=100)
        self.val2 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val2).place(x=50, y=150)
        self.val3 =  DoubleVar()
        v3 = Entry(self.b, textvariable=self.val3).place(x=50, y=200)
        self.val4 = DoubleVar()
        v3 = Entry(self.b, textvariable=self.val4).place(x=50, y=250)

        Button(self.b, text="resolver", command=self.bismu).place(x=100, y=300)

        self.b = mainloop()
    def bismu(self):
        fp.falso().falsaposicion(self.val.get(),self.val1.get(),self.val2.get(),self.val3.get(),self.val4.get(),self.b)

    #FALSA POSICION
    def falsap(self):
        self.f = Toplevel()
        self.f.geometry("1000x400")
        self.eti = Label(self.f, font=("ROCKWELL", 14), text="valor de xl").place(x=50, y=25)
        self.eti = Label(self.f, font=("ROCKWELL", 14), text="valor de xu").place(x=50, y=75)
        self.eti = Label(self.f, font=("ROCKWELL", 14), text="valor de tolerancia").place(x=50, y=125)
        self.eti = Label(self.f, font=("ROCKWELL", 14), text="intervalo inferior").place(x=50, y=175)
        self.eti = Label(self.f, font=("ROCKWELL", 14), text="intervalo superior").place(x=50, y=225)

        self.val = DoubleVar()
        v1 = Entry(self.f, textvariable=self.val).place(x=50, y=50)
        self.val1 = DoubleVar()
        v2 = Entry(self.f, textvariable=self.val1).place(x=50, y=100)
        self.val2 = IntVar()
        v3 = Entry(self.f, textvariable=self.val2).place(x=50, y=150)
        self.val3 =  DoubleVar()
        v3 = Entry(self.f, textvariable=self.val3).place(x=50, y=200)
        self.val4 = DoubleVar()
        v3 = Entry(self.f, textvariable=self.val4).place(x=50, y=250)

        Button(self.f, text="resolver", command=self.fpo).place(x=100, y=300)

        self.f = mainloop()
    def fpo(self):
        bi.bisecccion().bise(self.val.get(),self.val1.get(),self.val2.get(),self.val3.get(),self.val4.get(),self.f)

    #PUNTO FIJO
    def ejecutar(self):
        self.fi = Toplevel()
        self.fi.geometry("900x350")
        self.eti = Label(self.fi, font=("ROCKWELL", 14), text="valor de xi").place(x=50, y=25)
        self.eti = Label(self.fi, font=("ROCKWELL", 14), text="valor de tolerancia").place(x=50, y=125)
        self.eti = Label(self.fi, font=("ROCKWELL", 14), text="intervalo inferior").place(x=50, y=175)
        self.eti = Label(self.fi, font=("ROCKWELL", 14), text="intervalo superior").place(x=50, y=225)

        self.val = DoubleVar()
        v1 = Entry(self.fi, textvariable=self.val).place(x=50, y=50)
        self.val2 = DoubleVar()
        v3 = Entry(self.fi, textvariable=self.val2).place(x=50, y=150)
        self.val3 = DoubleVar()
        v3 = Entry(self.fi, textvariable=self.val3).place(x=50, y=200)
        self.val4 = DoubleVar()
        v3 = Entry(self.fi, textvariable=self.val4).place(x=50, y=250)

        Button(self.fi, text="resolver", command=self.ejecutar1).place(x=100, y=300)

        self.fi = mainloop()
    def ejecutar1(self):
        pf.iteraciones().itera(self.val.get(), self.val2.get(), self.val3.get(),self.val4.get(),self.fi)

    #VENTANAS DE SISTEMAS DE ECUACIONES
    #igualacion
    def igua(self):
        self.ig = Toplevel()
        self.ig.geometry("350x500")
        self.eti = Label(self.ig, font=("ROCKWELL", 18), text="ax+by=e").place(x=50, y=50)
        self.eti = Label(self.ig, font=("ROCKWELL", 18), text="cx+dy=f").place(x=50, y=100)

        self.eti = Label(self.ig, font=("ROCKWELL", 14), text="valor de a").place(x=50, y=175)
        self.eti = Label(self.ig, font=("ROCKWELL", 14), text="valor de b").place(x=50, y=225)
        self.eti = Label(self.ig, font=("ROCKWELL", 14), text="valor de e").place(x=50, y=275)
        self.eti = Label(self.ig, font=("ROCKWELL", 14), text="valor de c").place(x=50, y=325)
        self.eti = Label(self.ig, font=("ROCKWELL", 14), text="valor de d").place(x=50, y=375)
        self.eti = Label(self.ig, font=("ROCKWELL", 14), text="valor de f").place(x=50, y=425)

        self.val = DoubleVar()
        v1 = Entry(self.ig, textvariable=self.val).place(x=50, y=200)
        self.val1 = DoubleVar()
        v2 = Entry(self.ig, textvariable=self.val1).place(x=50, y=250)
        self.val2 = DoubleVar()
        v3 = Entry(self.ig, textvariable=self.val2).place(x=50, y=300)
        self.val3 = DoubleVar()
        v4 = Entry(self.ig, textvariable=self.val3).place(x=50, y=350)
        self.val4 = DoubleVar()
        v5 = Entry(self.ig, textvariable=self.val4).place(x=50, y=400)
        self.val5 = DoubleVar()
        v6 = Entry(self.ig, textvariable=self.val5).place(x=50, y=450)

        Button(self.ig, text="resolver", command=self.muesigua).place(x=200, y=300)

        self.ig = mainloop()

    def muesigua(self):
        y, x = ig.igualacion().iguala(self.val.get(), self.val1.get(), self.val2.get(), self.val3.get(),
                                      self.val4.get(), self.val5.get())
        # self.pon=IntVar()
        self.x = Label(self.ig, font=("ROCKWELL", 14), text=str("x = " + str(x))).place(x=200, y=50)
        # self.pon1 = IntVar()
        self.y = Label(self.ig, font=("ROCKWELL", 14), text=str("y = " + str(y))).place(x=200, y=100)
        # self.pon.set(x)
        # self.pon1.set(y)
    #reduccion
    def redu(self):
        self.red = Toplevel()
        self.red.geometry("350x500")
        self.eti = Label(self.red, font=("ROCKWELL", 18), text="ax+by=e").place(x=50, y=50)
        self.eti = Label(self.red, font=("ROCKWELL", 18), text="cx+dy=f").place(x=50, y=100)

        self.eti = Label(self.red, font=("ROCKWELL", 14), text="valor de a").place(x=50, y=175)
        self.eti = Label(self.red, font=("ROCKWELL", 14), text="valor de b").place(x=50, y=225)
        self.eti = Label(self.red, font=("ROCKWELL", 14), text="valor de e").place(x=50, y=275)
        self.eti = Label(self.red, font=("ROCKWELL", 14), text="valor de c").place(x=50, y=325)
        self.eti = Label(self.red, font=("ROCKWELL", 14), text="valor de d").place(x=50, y=375)
        self.eti = Label(self.red, font=("ROCKWELL", 14), text="valor de f").place(x=50, y=425)

        self.val = DoubleVar()
        v1 = Entry(self.red, textvariable=self.val).place(x=50, y=200)
        self.val1 = DoubleVar()
        v2 = Entry(self.red, textvariable=self.val1).place(x=50, y=250)
        self.val2 = DoubleVar()
        v3 = Entry(self.red, textvariable=self.val2).place(x=50, y=300)
        self.val3 = DoubleVar()
        v4 = Entry(self.red, textvariable=self.val3).place(x=50, y=350)
        self.val4 = DoubleVar()
        v5 = Entry(self.red, textvariable=self.val4).place(x=50, y=400)
        self.val5 = DoubleVar()
        v6 = Entry(self.red, textvariable=self.val5).place(x=50, y=450)

        Button(self.red, text="resolver", command=self.mueredu).place(x=200, y=300)

        self.red = mainloop()

    def mueredu(self):
        # re.red().proceso()
        y, x = re.red().proceso(self.val.get(), self.val1.get(), self.val2.get(), self.val3.get(), self.val4.get(),
                                self.val5.get())

        self.x = Label(self.red, font=("ROCKWELL", 14), text=str("x = " + str(x))).place(x=200, y=50)
        self.y = Label(self.red, font=("ROCKWELL", 14), text=str("y = " + str(y))).place(x=200, y=100)
    #sustitucion
    def sus(self):
        self.suz = Toplevel()
        self.suz.geometry("350x500")
        self.eti = Label(self.suz, font=("ROCKWELL", 18), text="ax+by=e").place(x=50, y=50)
        self.eti = Label(self.suz, font=("ROCKWELL", 18), text="cx+dy=f").place(x=50, y=100)

        self.eti = Label(self.suz, font=("ROCKWELL", 14), text="valor de a").place(x=50, y=175)
        self.eti = Label(self.suz, font=("ROCKWELL", 14), text="valor de b").place(x=50, y=225)
        self.eti = Label(self.suz, font=("ROCKWELL", 14), text="valor de e").place(x=50, y=275)
        self.eti = Label(self.suz, font=("ROCKWELL", 14), text="valor de c").place(x=50, y=325)
        self.eti = Label(self.suz, font=("ROCKWELL", 14), text="valor de d").place(x=50, y=375)
        self.eti = Label(self.suz, font=("ROCKWELL", 14), text="valor de f").place(x=50, y=425)

        self.val = DoubleVar()
        v1 = Entry(self.suz, textvariable=self.val).place(x=50, y=200)
        self.val1 = DoubleVar()
        v2 = Entry(self.suz, textvariable=self.val1).place(x=50, y=250)
        self.val2 = DoubleVar()
        v3 = Entry(self.suz, textvariable=self.val2).place(x=50, y=300)
        self.val3 = DoubleVar()
        v4 = Entry(self.suz, textvariable=self.val3).place(x=50, y=350)
        self.val4 = DoubleVar()
        v5 = Entry(self.suz, textvariable=self.val4).place(x=50, y=400)
        self.val5 = DoubleVar()
        v6 = Entry(self.suz, textvariable=self.val5).place(x=50, y=450)

        Button(self.suz, text="resolver", command=self.muessus).place(x=200, y=300)

        self.suz = mainloop()

    def muessus(self):
        # st.susti().proceso()
        y, x = st.susti().proceso(self.val.get(), self.val1.get(), self.val2.get(), self.val3.get(),
                                  self.val4.get(), self.val5.get())

        self.x = Label(self.suz, font=("ROCKWELL", 14), text=str("x = " + str(x))).place(x=200, y=50)
        self.y = Label(self.suz, font=("ROCKWELL", 14), text=str("y = " + str(y))).place(x=200, y=100)

    # VENTANA DE LA MINIMOS CUADRADOS
    def minimos(self):
        self.v = Toplevel()
        self.v.geometry("600x600")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x0", bg='gray').place(x=10, y=0)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x1", bg='gray').place(x=10, y=100)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x2", bg='gray').place(x=10, y=200)
        self.dat3 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat3).place(x=10, y=250)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x3", bg='gray').place(x=10, y=300)
        self.dat4 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat4).place(x=10, y=350)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x4", bg='gray').place(x=10, y=400)
        self.dat5 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat5).place(x=10, y=450)


        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y0", bg='gray').place(x=300, y=0)
        self.dat7 = DoubleVar()
        Entry(self.v, textvariable=self.dat7).place(x=300, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y1", bg='gray').place(x=300, y=100)
        self.dat8 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat8).place(x=300, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y2", bg='gray').place(x=300, y=200)
        self.dat9 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat9).place(x=300, y=250)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y3", bg='gray').place(x=300, y=300)
        self.dat10 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat10).place(x=300, y=350)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y4", bg='gray').place(x=300, y=400)
        self.dat11 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat11).place(x=300, y=450)


        Button(self.v, font=("INK FREE", 18), fg='black', text="calcular", bg='gray',
               command=self.mandar_minimos, relief=FLAT).place(x=500, y=50)
        self.v = mainloop()

    # VENTANA DE PROCESO DE MINIMOS CUADRADOS
    def mandar_minimos(self):
        mc.ajuste().cuadrados(self.dat1.get(), self.dat2.get(), self.dat3.get(),
                              self.dat4.get(), self.dat5.get(),  self.dat7.get(), self.dat8.get(),
                              self.dat9.get(), self.dat10.get(), self.dat11.get())

    # VENTANA DE LA regresion lineal
    def regre(self):
        self.v = Toplevel()
        self.v.geometry("600x600")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")


        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x0", bg='gray').place(x=10, y=0)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x1", bg='gray').place(x=10, y=100)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x2", bg='gray').place(x=10, y=200)
        self.dat3 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat3).place(x=10, y=250)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x3", bg='gray').place(x=10, y=300)
        self.dat4 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat4).place(x=10, y=350)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x4", bg='gray').place(x=10, y=400)
        self.dat5 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat5).place(x=10, y=450)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto x5", bg='gray').place(x=10, y=500)
        self.dat6 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat6).place(x=10, y=550)


        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y0", bg='gray').place(x=300, y=0)
        self.dat7 = DoubleVar()
        Entry(self.v, textvariable=self.dat7).place(x=300, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y1", bg='gray').place(x=300, y=100)
        self.dat8 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat8).place(x=300, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y2", bg='gray').place(x=300, y=200)
        self.dat9 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat9).place(x=300, y=250)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y3", bg='gray').place(x=300, y=300)
        self.dat10 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat10).place(x=300, y=350)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y4", bg='gray').place(x=300, y=400)
        self.dat11 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat11).place(x=300, y=450)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto y5", bg='gray').place(x=300, y=500)
        self.dat12 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat12).place(x=300, y=550)

        Button(self.v, font=("INK FREE", 18), fg='black', text="calcular", bg='gray',
               command=self.mandar_regresion, relief=FLAT).place(x=500, y=50)
        self.v = mainloop()

    # VENTANA DE PROCESO DE regresion lineal
    def mandar_regresion(self):
        rl.ajuste().regresion(self.dat1.get(), self.dat2.get(), self.dat3.get(),
                                   self.dat4.get(),self.dat5.get(),self.dat6.get(),self.dat7.get(),self.dat8.get(),self.dat9.get(),self.dat10.get(),self.dat11.get(),self.dat12.get())

    #VENTANA DE LA INTERPOLACION DE NEWTON
    def newt(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10, y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto a", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto b", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=250)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto c", bg='gray').place(x=10, y=300)
        self.dat3 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat3).place(x=10, y=350)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto d", bg='gray').place(x=10, y=400)
        self.dat4 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat4).place(x=10, y=450)

        Button(self.v, font=("INK FREE", 18), fg='black', text="calcular", bg='gray',
               command=self.mandar, relief=FLAT).place(x=300, y=50)
        self.v = mainloop()

    #VENTANA DE PROCESO DE INTERPOLACION DE NEWTON
    def mandar(self):
        ine.interpolacion().newton(self.dat.get(),self.dat1.get(),self.dat2.get(),self.dat3.get(),self.dat4.get())

    # VENTANA DE LA INTERPOLACION DE LAGRANGE
    def lagr(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10, y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto a", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto b", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=250)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto c", bg='gray').place(x=10, y=300)
        self.dat3 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat3).place(x=10, y=350)

        Button(self.v, font=("INK FREE", 18), fg='black', text="calcular", bg='gray',
               command=self.mandar_lagrange, relief=FLAT).place(x=300, y=50)
        self.v = mainloop()

    # VENTANA DE PROCESO DE INTERPOLACION DE LAGRANGE
    def mandar_lagrange(self):
        la.interpolacion().lagrange(self.dat.get(), self.dat1.get(), self.dat2.get(), self.dat3.get() )



    #VENTANA QUE SE DESPLEGARA AL USAR EL METODO DE LOS TRES PUNTOS
    def ventana_tes(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10, y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto a evaluar", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de h", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=250)

        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar en centro", bg='gray',
               command=self.tres_puntos, relief=FLAT).place(x=300, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar por izquierda", bg='gray',
               command=self.tres_izq, relief=FLAT).place(x=300, y=100)
        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar por derecha", bg='gray',
               command=self.tres_der, relief=FLAT).place(x=300, y=150)
        self.v = mainloop()
    #EN LAS TRES FUNCIONES SIGUIENTES SE TOMAN VALORES DE CAJA DETEXTO Y SE MANDAN A LA FUNCION CORRESPONDIENTE
    def tres_der(self):
        a = str(self.dat.get())
        b = (self.dat1.get())
        c = (self.dat2.get())
        tp.tres().derecha(a, b, c)
    def tres_izq(self):
        a = str(self.dat.get())
        b = (self.dat1.get())
        c = (self.dat2.get())
        tp.tres().izquierda(a, b, c)
    def tres_puntos(self):
        a = str(self.dat.get())
        b = (self.dat1.get())
        c = (self.dat2.get())
        tp.tres().primera(a, b, c)
    #SE LLAMA A LA VENTANA DE LOS CINCO PUNTOS
    def ventana_cinco(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10,y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="punto a evaluar", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de h", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja  =Entry(self.v, textvariable=self.dat2).place(x=10, y=250)

        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar", bg='gray',
               command=self.cinco_puntos, relief=FLAT).place(x=300, y=150)
        self.v = mainloop()
    #SE EJECUTA LA FUNCION DEL METODO DE CINCO PUNTOS
    def cinco_puntos(self):
        a=str(self.dat.get())
        b=(self.dat1.get())
        c=(self.dat2.get())
        cp.cinco().proceso(a,b,c)
    #VENTANA DEL METODO DEL TRAPECIO
    def ventana_trapecio(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10, y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de a", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de b", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=250)

        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar", bg='gray',
               command=self.trapecio, relief=FLAT).place(x=300, y=150)
        self.v = mainloop()
    #SE MANDAN PARAMETROS A LA FUNCION DEL METODO DEL TRAPECIO
    def trapecio(self):
        a = str(self.dat.get())
        b = (self.dat1.get())
        c = (self.dat2.get())
        tra.trapecio().proceso(a,b,c)
    #VENTANA DEL METODO SIMPSON 1/3
    def ventana_simpson13(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10, y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de a", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de b", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=250)

        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar", bg='gray',
               command=self.simpson13, relief=FLAT).place(x=300, y=150)
        self.v = mainloop()
    #EJECUCION DE METODO SIMPSON 1/3 CON VALORES RECIBIDOS
    def simpson13(self):
        a = str(self.dat.get())
        b = (self.dat1.get())
        c = (self.dat2.get())
        s1.simpson().proceso(a,b,c)
    #VENTANA DEL METODO SIMPSON 3/8
    def ventana_simpson38(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10, y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de a", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de b", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=250)

        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar", bg='gray',
               command=self.simpson38, relief=FLAT).place(x=300, y=150)
        self.v = mainloop()
    #EJECUCUION DEL METODO SIMPSON 3/8
    def simpson38(self):
        a = str(self.dat.get())
        b = (self.dat1.get())
        c = (self.dat2.get())
        s3.simpson2().proceso(a,b,c)
    #VENTANA DE LA CUADRATURA GAUSSIANA
    def ventana_cuadratura_gaussiana(self):
        self.v = Toplevel()
        self.v.geometry("600x500")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="funcion", bg='gray').place(x=10, y=0)
        self.dat = StringVar()
        Entry(self.v, textvariable=self.dat).place(x=10, y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de a", bg='gray').place(x=10, y=100)
        self.dat1 = DoubleVar()
        Entry(self.v, textvariable=self.dat1).place(x=10, y=150)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de b", bg='gray').place(x=10, y=200)
        self.dat2 = DoubleVar()
        self.caja = Entry(self.v, textvariable=self.dat2).place(x=10, y=250)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor de n", bg='gray').place(x=10, y=300)
        self.dat3 = IntVar()
        self.caja = Entry(self.v, textvariable=self.dat3).place(x=10, y=350)
        Button(self.v, font=("INK FREE", 18), fg='black', text="evaluar", bg='gray',
               command=self.cuadratura_gaussiana, relief=FLAT).place(x=300, y=150)
        self.v = mainloop()
    #EJECUCUION DEL METODO DE CUADRATURA GAUSSIANA
    def cuadratura_gaussiana(self):
        a = str(self.dat.get())
        b = (self.dat1.get())
        c = (self.dat2.get())
        d = (self.dat3.get())
        cg.cuadratura().proceso(a,b,c,d)

m=metodos()
m.interfaz()