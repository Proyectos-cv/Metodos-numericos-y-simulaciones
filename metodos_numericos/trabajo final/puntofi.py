from Tkinter import *
import numpy as n
import matplotlib.pyplot as plt
import math
class jacob:
    def ventana(self):
        self.v = Tk()

        self.v.geometry("600x800")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="AX**2 + BY**2 + C", bg='gray').place(x=10,
                                                                                                                 y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="DX**2 + EY**2 + F", bg='gray').place(x=10,
                                                                                                                 y=50)

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor A", bg='gray').place(x=400,y=25)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor B", bg='gray').place(x=400, y=75)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor C", bg='gray').place(x=400, y=125)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor D", bg='gray').place(x=400, y=175)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor E", bg='gray').place(x=400, y=225)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor F", bg='gray').place(x=400, y=275)


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


        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.lamb, relief=FLAT).place(x=70, y=200)
        self.v=mainloop()


    def lamb(self):
        #x2+y2=25, 2x2+3y2=59
        x = lambda yo: math.sqrt((25.0) - (yo**2))
        y = lambda xo: math.sqrt((59.0 / 3.0) - ((2.0 / 3.0) * (xo**2)))
        xo = 0.0
        yo = 0.0

        f=0
        g=20
        self.vl = Tk()
        self.vl.geometry("600x800")
        listbox = Listbox(self.vl, width=100, height=50)
        while f<g:
            auxx=xo
            auxy=yo
            ll="x= ", xo,"y= ",yo
            listbox.insert(0, ll)
            xo=x(auxy)
            yo=y(auxx)
            f=f+1
        listbox.place(x=250, y=0)
        self.vl = mainloop()






j=jacob()
j.ventana()
#j.lamb()
#j.ejercicio()
#j.iterar()

