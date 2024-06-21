from Tkinter import *
import numpy as n
import matplotlib.pyplot as plt
class jacob:
    def ventana(self):
        self.v = Tk()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("600x800")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="AX + BY + CZ = D", bg='gray').place(x=10,
                                                                                                                 y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="EX + FY + GZ = H", bg='gray').place(x=10,
                                                                                                                 y=50)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="IX + JY + KZ = L", bg='gray').place(x=10,
                                                                                                                 y=100)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor A", bg='gray').place(x=400,y=25)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor B", bg='gray').place(x=400, y=75)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor C", bg='gray').place(x=400, y=125)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor D", bg='gray').place(x=400, y=175)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor E", bg='gray').place(x=400, y=225)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor F", bg='gray').place(x=400, y=275)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor G", bg='gray').place(x=400, y=325)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor H", bg='gray').place(x=400, y=375)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor I", bg='gray').place(x=400, y=425)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor J", bg='gray').place(x=400, y=475)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor K", bg='gray').place(x=400, y=525)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor L", bg='gray').place(x=400, y=575)

        self.u=DoubleVar()
        self.c = Entry(self.v,textvariable=self.u).place(x=400, y=50)
        self.u1 = DoubleVar()
        self.c1 = Entry(self.v,textvariable=self.u1).place(x=400, y=100)
        self.u2 = DoubleVar()
        self.c2 = Entry(self.v,textvariable=self.u2).place(x=400, y=150)
        self.u3 = DoubleVar()
        self.c3 = Entry(self.v,textvariable=self.u3).place(x=400, y=200)
        self.u4 = DoubleVar()
        self.c4 = Entry(self.v,textvariable=self.u4).place(x=400, y=250)
        self.u5 = DoubleVar()
        self.c5 = Entry(self.v,textvariable=self.u5).place(x=400, y=300)
        self.u6 = DoubleVar()
        self.c6 = Entry(self.v,textvariable=self.u6).place(x=400, y=350)
        self.u7 = DoubleVar()
        self.c7 = Entry(self.v,textvariable=self.u7).place(x=400, y=400)
        self.u8 = DoubleVar()
        self.c8 = Entry(self.v,textvariable=self.u8).place(x=400, y=450)
        self.u9 = DoubleVar()
        self.c9 = Entry(self.v,textvariable=self.u9).place(x=400, y=500)
        self.u10 = DoubleVar()
        self.c10 = Entry(self.v,textvariable=self.u10).place(x=400, y=550)
        self.u11 = DoubleVar()
        self.c11 = Entry(self.v,textvariable=self.u11).place(x=400, y=600)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.iterar, relief=FLAT).place(x=70, y=200)
        self.v=mainloop()

    def iterar(self):

        a=self.u.get()
        b=self.u1.get()
        c=self.u2.get()
        d=self.u3.get()
        e=self.u4.get()
        f=self.u5.get()
        g=self.u6.get()
        h=self.u7.get()
        i=self.u8.get()
        j=self.u9.get()
        k=self.u10.get()
        l=self.u11.get()
        #a=float(self.c.get())
        #b=float(self.c1.get())
        #c=float(self.c2.get())
        #d=float(self.c3.get())
        #e=float(self.c4.get())
        #f=float(self.c5.get())
        ##g=float(self.c6.get())
        #h=float(self.c7.get())
        #i=float(self.c8.get())
        #j=float(self.c9.get())
        #k=float(self.c10.get())
        #l=float(self.c11.get())
        print a,b,c,d,e,f,g,h,i,j,k,l
        if self.u1.get()+self.u2.get()<abs(self.u.get()) and self.u4.get()+self.u6.get()<abs(self.u5.get()) and self.u8.get()+self.u9.get()<abs(self.u10.get()):
            x = lambda yo, zo: (d / a) - ((b / a) * yo) - ((c / a) * zo)
            y = lambda xo, zo: (h / f) - ((e / f) * xo) - ((g / f) * zo)
            z = lambda xo, yo: (l / k) - ((i / k) * xo) - ((j / k) * yo)
            xo = 0.0
            yo = 0.0
            zo = 0.0
            f1 = 0
            g1 = 20
            self.vl = Tk()
            self.vl.geometry("600x800")
            listbox = Listbox(self.vl, width=100, height=50)
            while f1 < g1:
                auxx = xo
                auxy = yo
                auxz = zo
                print xo, yo, zo
                ll=xo, yo, zo
                xo = x(auxy, auxz)
                yo = y(auxx, auxz)
                zo = z(auxx, auxy)
                f1 = f1 + 1
                listbox.insert(0, ll)
            listbox.place(x=250, y=0)
            self.vl=mainloop()

        else:
            print "reordena la matriz"

    def lamb(self):
        #x = lambda yo, zo: (5.0/2.0)-((3.0 / 2.0) * yo) - ((7.0 / 2.0) * zo)
        #y = lambda xo, zo: (9.0/2.0)-((3.0 / 2.0) * xo) - ((4.0 / 2.0) * zo)
        #z = lambda xo, yo: (5.0/2.0)-((1.0 / 2.0) * xo) - ((1.0 / 2.0) * yo)
        x = lambda yo, zo: (5.0 / 7.0) - ((2.0 / 7.0) * yo) - ((3.0 / 7.0) * zo)
        y = lambda xo, zo: (7.0 / 8.0) - ((3.0 / 8.0) * xo) - ((1.0 / 8.0) * zo)
        z = lambda xo, yo: (8.0 / 9.0) - ((5.0 / 9.0) * xo) - ((2.0 / 9.0) * yo)
        xo = 0.0
        yo = 0.0
        zo = 0.0
        # 2x+3y+7z=5
        # 3x+2y+4z=9
        # x +y +2z=5
        f=0
        g=20
        while f<g:
            auxx=xo
            auxy=yo
            auxz=zo
            print xo,yo,zo
            xo=x(auxy, auxz)
            yo=y(auxx, auxz)
            zo=z(auxx, auxy)
            f=f+1

            #i = x(xo, yo, zo)
           #print i
    def ejercicio(self):
        x = lambda yo: (1.0 / 5.0) - ((2.0 / 5.0) * yo)
        y = lambda xo: ((1.0 / 4.0) * xo)
        xo = 1.0
        yo = 2.0
        f = 0
        g = 6
        while f < g:
            auxx=xo
            auxy=yo
            xe = x(yo)
            ye = y(xo)
            print xe, ye
            yo = y(auxx)
            xo = x(auxy)
            f = f + 1
            print"r",xo,yo
j=jacob()
j.ventana()
#j.lamb()
#j.ejercicio()
#j.iterar()

def lamb1(self):
    x = lambda yo, zo: (5.0 / 2.0) - ((3.0 / 2.0) * yo) - ((7.0 / 2.0) * zo)
    y = lambda xo, zo: (9.0 / 2.0) - ((3.0 / 2.0) * xo) - ((4.0 / 2.0) * zo)
    z = lambda xo, yo: (5.0 / 2.0) - ((1.0 / 2.0) * xo) - ((1.0 / 2.0) * yo)
    xo = 1.0
    yo = 1.0
    zo = 1.0
    # 2x+3y+7z=5
    # 3x+2y+4z=9
    # x +y +2z=5
    f = 0
    g = 10
    listbox = Listbox(f, width=100, height=50)
    while f < g:
        auxx = xo
        auzy = yo
        auxz = zo
        print xo, yo, zo
        xo = x(yo, zo)
        yo = y(xo, zo)
        zo = z(xo, yo)
        f = f + 1
        listbox.insert(0, li)
    listbox.place(x=250, y=0)

        # i = x(xo, yo, zo)
        # print i
