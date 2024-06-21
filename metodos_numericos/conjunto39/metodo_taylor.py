from sympy import *
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import messagebox
class diferencial:
    def taylor(self,expr):
        #definicion de variables de la funcion
        x, y = symbols("x y")
        #expr = (input("funcion: "))

        #obtener derivada de la funcion
        derivada1 = (diff(expr, x))
        expr = eval(expr)
        #obtener la derivada de la nueva funcion tras una derivada
        derivada2 = (diff(derivada1, x))
        #obtener evaluaciones para conseguir el error
        fx1 = ((expr.evalf(subs={x: 0}))*0.5**2)/2
        fx2=((derivada1.evalf(subs={x:0}))*0.5**3)/6
        fx3 = ((derivada2.evalf(subs={x: 0}))*0.5**4)/24
        ##print (expr)
        ##print(fx1)
        #print (derivada1)
        #print(fx2)
        #print (derivada2)
        #print(fx3)
        #se calcula el error total
        sumatotal=fx1+fx2+fx3
        #print (sumatotal)
        #mandar a pantalla la respuesta del ejercicio
        messagebox.showinfo("resultado", ("error de la funcion: " + str(sumatotal)))

#d=diferencial()
#d.taylor()
