from sympy import *
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import messagebox
class diferencial:
    def euler(self,expr,inicio,final,paso,yr):
        #definicion de variables
        x, y = symbols("x y")
        #expr = (input("funcion: "))
        #inicio=float(input("punto de inicio: "))
        #final = float(input("punto final: "))
        #paso = float(input("valor de paso: "))
        #y = float(input("condicion inicial en y(0): "))
        #definicion de una ventana y variables para el ciclo
        self.v = Toplevel()
        self.v.geometry("350x300")
        entra= "x= ",inicio," y= ",yr
        expr = eval(expr)
        listbox = Listbox(self.v, width=175, height=50)
        listbox.insert(0, entra)
        x1 = 0.0
        y1 = 0.0
        x0=inicio
        y0=yr
        #ciclo de iteraciones segun las operaciones del metodo
        while x1<final:
            x1=x0+paso
            y1=y0+paso*(expr.evalf(subs={x: x0,y:y0}))
            entra= "x= ",x1," y= ",y1
            listbox.insert(0,entra)
            x0=x1
            y0=y1
        listbox.place(x=0, y=0)
        self.v=mainloop()

    def euler1(self):
        l=[]
        x, y = symbols("x y")
        expr = (input("funcion: "))

        expr = eval(expr)
        y1 = (expr.evalf(subs={x:2,y:3 }))
        print (y1)

#((x**2)-1)/y**2, 0,1,0.2,2
        #https: // www.youtube.com / watch?v = trlBFQXGS7A
#d=diferencial()
#d.euler()
#https://www.youtube.com/watch?v=Wcyqs6YAxpo&t=310s,  https://www.youtube.com/watch?v=trlBFQXGS7A
#gradiente sympy
#https://www.youtube.com/watch?v=xDzmQnCPVHY