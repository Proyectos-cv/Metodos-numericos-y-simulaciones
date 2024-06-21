# -*- coding: utf-8 -*-�
# #!/usr/bin/env python
from Tkinter import *
import grafico
import ttk
import tkMessageBox
from ttk import *
import Tkinter as tk
import puntofijo as pf
import sustitucion as st
import reduccion as re
import igualacion as ig
import biseccion as bi
import falsapocision as fp
import jacobi as ja
class metodos:
    def interfaz(self):
        self.window = Tk()
        self.window.geometry("350x300")
        menu=tk.Menu(self.window)
        self.window.config(bg="blue")
        menu.add_command(label='unidad 1')
        #menu.add_command(label='unidad 2')
        #menu.add_command(label='unidad 3')

        desplegable=tk.Menu(menu,tearoff=0)
        #desplegable.add_command(label='punto fijo')
        #desplegable.add_command(label='newton - ramphson')

        otro=tk.Menu(menu,tearoff=0)
        otro.add_command(label='metodo de reduccion',command=self.redu)
        otro.add_command(label='metodo de sustitucion', command=self.sus)
        otro.add_command(label='metodo de igualacion',command=self.igua)
        otromas=tk.Menu(menu,tearoff=0)
        otromas.add_command(label='biseccion',command=self.bis)
        otromas.add_command(label='falsa pocision',command=self.falsap)
        otromas.add_command(label='metodo de punto fijo', command=self.ejecutar)
        otromas.add_command(label='metodo grafico', command=self.graficos)
        unidad3 = tk.Menu(menu, tearoff=0)
        unidad3.add_command(label='punto fijo', command=self.puntofijou2)
        unidad3.add_command(label='jacobi', command=self.jacobi)
        unidad3.add_command(label='newton - ramphson', command=self.newtonramphon)
        unidad3.add_command(label='gauss - saidel', command=self.gausssidel)

        self.eti = Label(self.window, font=("ROCKWELL", 16), text="Instituto Tecnologico Superior").place(x=0, y=50)
        self.eti = Label(self.window, font=("ROCKWELL", 16), text="Zacarcas Sur").place(x=100, y=90)
        self.eti=Label(self.window, font=("ROCKWELL", 18), text="METODOS NUMERICOS").place(x=20,y=170)
        menu.add_cascade(label='unidad 2',menu=desplegable)
        menu.add_cascade(label='unidad 3', menu=unidad3)
        desplegable.add_cascade(label='sistemas de ecuaciones', menu=otro)

        desplegable.add_cascade(label='metodos iterativos', menu=otromas)
        self.window.config(menu=menu)

        menu.add_command(label= 'salir',command=self.salir)

        self.window = mainloop()
    def puntofijou2(self):
        print "punto fijo"
    def gausssidel(self):
        print "gauss saidel"
    def jacobi(self):
        ja.jacob().ventana()
    def newtonramphon(self):
        self.nr = Toplevel()
        self.nr.geometry("1000x400")
        self.eti = Label(self.nr, font=("ROCKWELL", 14), text="valor de xl").place(x=50, y=25)
        self.eti = Label(self.nr, font=("ROCKWELL", 14), text="valor de xu").place(x=50, y=75)
        self.eti = Label(self.nr, font=("ROCKWELL", 14), text="valor de tolerancia").place(x=50, y=125)
        self.eti = Label(self.nr, font=("ROCKWELL", 14), text="intervalo inferior").place(x=50, y=175)
        self.eti = Label(self.nr, font=("ROCKWELL", 14), text="intervalo superior").place(x=50, y=225)

        self.val = DoubleVar()
        v1 = Entry(self.nr, textvariable=self.val).place(x=50, y=50)
        self.val1 = DoubleVar()
        v2 = Entry(self.nr, textvariable=self.val1).place(x=50, y=100)
        self.val2 = IntVar()
        v3 = Entry(self.nr, textvariable=self.val2).place(x=50, y=150)
        self.val3 = DoubleVar()
        v3 = Entry(self.nr, textvariable=self.val3).place(x=50, y=200)
        self.val4 = DoubleVar()
        v3 = Entry(self.nr, textvariable=self.val4).place(x=50, y=250)

        Button(self.nr, text="resolver", command=self.fpo).place(x=100, y=300)

        self.nr = mainloop()
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
    def igua(self):

        self.ig=Toplevel()
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

        Button(self.ig, text="resolver",command=self.muesigua).place(x=200, y=300)

        self.ig=mainloop()
    def muesigua(self):
        y,x=ig.igualacion().iguala(self.val.get(),self.val1.get(),self.val2.get(),self.val3.get(),self.val4.get(),self.val5.get())
        #self.pon=IntVar()
        self.x = Label(self.ig, font=("ROCKWELL", 14),text=str("x = "+str(x))).place(x=200, y=50)
        #self.pon1 = IntVar()
        self.y = Label(self.ig, font=("ROCKWELL", 14),text=str("y = "+str(y))).place(x=200, y=100)
        #self.pon.set(x)
        #self.pon1.set(y)
    def graficos(self):
        self.g = Toplevel()

        self.g.geometry('350x200')
        #self.combo = ttk.Combobox(self.g)
        #self.combo['values'] = ("sen()", "cos()", "tan()", "cot()", "ln()", "e**x")
        #self.combo.current(1)  # set the selected item
        #self.combo.grid(column=0, row=0)

        self.g.geometry("350x300")
        self.eti = Label(self.g, font=("ROCKWELL", 14), text="punto inferior del intervalo").place(x=50, y=25)
        self.eti = Label(self.g, font=("ROCKWELL", 14), text="punto superior del intervalo").place(x=50, y=75)
        self.va = DoubleVar()
        v1 = Entry(self.g, textvariable=self.va).place(x=50, y=50)
        self.va1 = DoubleVar()
        v2 = Entry(self.g, textvariable=self.va1).place(x=50, y=100)
        Button(self.g, text="graficar", command=self.gra).place(x=50, y=150)

        #a=LabelFrame(self.g).place()
        #self.eti = Label(a, font=("ROCKWELL", 14), text="punto inferior del intervalo").place(x=50, y=150)
        #for widget in a.winfo_children():
         #   widget.destroy()
        #a.destroy()
        self.gr=mainloop()
    def gra(self):
#        print self.combo.get()
        grafico.grafic().intervalo(self.va.get(),self.va1.get())

    def loc(self):
        print self.val.get()
        print self.val1.get()
        print self.val2.get()
        print self.val3.get()
        print self.val4.get()
        print self. val5.get()
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
        #re.red().proceso()
        y, x = re.red().proceso(self.val.get(), self.val1.get(), self.val2.get(), self.val3.get(),self.val4.get(), self.val5.get())

        self.x = Label(self.red, font=("ROCKWELL", 14), text=str("x = " + str(x))).place(x=200, y=50)
        self.y = Label(self.red, font=("ROCKWELL", 14), text=str("y = " + str(y))).place(x=200, y=100)

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
        #st.susti().proceso()
        y, x = st.susti().proceso(self.val.get(), self.val1.get(), self.val2.get(), self.val3.get(),
                                      self.val4.get(), self.val5.get())

        self.x = Label(self.suz, font=("ROCKWELL", 14), text=str("x = " + str(x))).place(x=200, y=50)
        self.y = Label(self.suz, font=("ROCKWELL", 14), text=str("y = " + str(y))).place(x=200, y=100)
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
    def cambiar(self):
        self.window['bg']= 'red'
    def salir(self):
        answer=tkMessageBox.askyesno("Salir",message="¿Desea Salir?")
        if (answer):
            answer1 = tkMessageBox.askyesno("Salir", message="¿Seguro?")
            if answer1:
                answer1 = tkMessageBox.askyesno("Salir", message="¿de verdad?")
                if answer1:
                    answer1 = tkMessageBox.askyesno("Salir", message="ultima oprtunidad")
                    if answer1:
                        answer1 = tkMessageBox.askyesno("Salir", message="esta bien cierre")
                        if answer1:
                            self.window.destroy()
m=metodos()
m.interfaz()