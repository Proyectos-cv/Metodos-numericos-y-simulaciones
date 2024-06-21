from sympy import *
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import messagebox
class diferencial:
    def kutta(self,expr,xr,iteraciones,paso,yr):
        #definicion de variables iniciales
        x, y = symbols("x y")

        #expr = (input("funcion: "))
        #xr = float(input("punto de x: "))
        #yr = float(input("condicion inicial en y(0): "))
        #iteraciones = float(input("numero de iteraciones: "))
        #paso = float(input("valor de paso: "))
        #creacion de una ventana y variables para el ciclo
        expr = eval(expr)

        self.v = Toplevel()
        self.v.geometry("350x300")
        entra= "x= ",xr," y= ",yr
        listbox = Listbox(self.v, width=175, height=50)
        listbox.insert(0, entra)
        conta=0
        #ciclo con calculos para las iteraciones segun el mettodo
        while conta<iteraciones:
            k1 = (expr.evalf(subs={x: xr, y: yr}))
            #print(k1)
            k2 = (expr.evalf(subs={x: (xr + (1.0 / 2.0) * paso), y: yr + (1.0 / 2.0) * k1 * paso}))
            #print(k2)
            k3 = (expr.evalf(subs={x: (xr + (1.0 / 2.0) * paso), y: yr + (1.0 / 2.0) * k2 * paso}))
            #print(k3)
            k4 = (expr.evalf(subs={x: (xr + paso), y: yr + (k3 * paso)}))
            #print(k4)
            y1 = yr + (1.0 / 6.0) * ((k1 + 2 * k2 + 2 * k3 + k4) * paso)
            #print(y1)
            #print("")
            xr=xr+paso
            yr=y1
            conta=conta+1
            entra = "x= ", xr, " y= ", yr
            listbox.insert(0, entra)
        listbox.place(x=0, y=0)
        self.v=mainloop()

#d=diferencial()
#d.kutta()
#https://www.youtube.com/watch?v=Wwf7HrjPcTM
#(y+1)*(x+1)*cos(x**2+2*x)

