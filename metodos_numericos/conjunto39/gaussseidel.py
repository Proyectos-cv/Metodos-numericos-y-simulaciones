from tkinter import *
import numpy as n
import matplotlib.pyplot as plt
from tkinter import messagebox

class jacob:
    def ventana(self):
        self.v = Toplevel()
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

        #print a,b,c,d,e,f,g,h,i,j,k,l
        x = lambda yo, zo: float(d / a) - (float(b / a) * yo) - (float(c / a) * zo)
        y = lambda xo, zo: float(h / f) - (float(e / f) * xo) - (float(g / f) * zo)
        z = lambda xo, yo: float(l / k) - (float(i / k) * xo) - (float(j / k) * yo)
        if self.u1.get()+self.u2.get()<abs(self.u.get()) and self.u4.get()+self.u6.get()<abs(self.u5.get()) and self.u8.get()+self.u9.get()<abs(self.u10.get()):

            xo = x(0, 0)
            yo = y(xo, 0)
            zo = z(xo, yo)
            f1 = 0
            g1 = 20
            auxx=0.0
            self.vl = Tk()
            self.vl.geometry("600x800")
            listbox = Listbox(self.vl, width=100, height=50)
            while f1 < g1:

                #j=xo, yo, zo
                auxx = float(xo)
                auxy = float(yo)
                auxz = float(zo)
                #print xo, yo, zo
                ll = "x: ",xo,"y: ", yo,"z: ", zo
                xo = x(auxy, auxz)
                yo = y(auxx, auxz)
                zo = z(auxx, auxy)
                f1 = f1 + 1
                listbox.insert(0, ll)
            listbox.place(x=250, y=0)
            self.vl = mainloop()


        else:
            messagebox.showinfo("advertencia", "reordena la matriz")
#g=jacob()
#g.ventana()