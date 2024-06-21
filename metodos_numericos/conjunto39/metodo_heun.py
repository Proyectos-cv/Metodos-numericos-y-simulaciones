from sympy import *
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import messagebox
class diferencial:
    #def heun(self,expr,inicio,final,paso,yr):
    def heun(self):
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

        Button(self.b, text="resolver", command=self.eun).place(x=100, y=300)

        self.b = mainloop()
    def eun(self):
        #definicion de variables iniciales y variables
        x, y = symbols("x y")
        expr = self.val.get()
        inicio = self.val1.get()
        final = self.val2.get()
        paso = self.val3.get()
        yr = self.val4.get()

        #x, y = symbols("x y")
        #expr = (input("funcion: "))
        #inicio=float(input("punto de inicio: "))
        #final = float(input("punto final: "))
        #paso = float(input("valor de paso: "))
        #yr = float(input("condicion inicial en y(0): "))

        #creacion de una ventana y unas variables para utilizar en el ciclo
        self.v = Toplevel()
        self.v.geometry("350x300")
        entra= "x= ",inicio," y= ",yr
        expr = eval(expr)
        listbox = Listbox(self.v, width=175, height=50)
        listbox.insert(0, entra)
        x1 = 0.0
        y1 = 0.0
        sum=0.0
        x0=inicio
        y0=yr


        #iteraciones del metodo para conseguir los valores
        while x0<final:
            punto2 = y0 + paso * ((expr.evalf(subs={x: x0, y: y0})))
            ##print (punto2)

            o = expr.evalf(subs={x: x0, y: y0})
            ##print(o)
            f = expr.evalf(subs={x: x0 + paso, y: punto2})
            ##print(f)
            ye = y0 + ((expr.evalf(subs={x: x0, y: y0}) + expr.evalf(subs={x: x0 + paso, y: punto2})) / 2) * paso
            x0=x0+paso
            y0=ye

            #print("ye", (ye))
            entra="x: ", x0," y: ", (ye)
            listbox.insert(0, entra)
            auxx = (expr.evalf(subs={x: sum, y: y0}))
            ye = y0 + auxx * paso
        listbox.place(x=0, y=0)
        self.v=mainloop()
    def heun1(self):
        x, y = symbols("x y")
        expr = (input("funcion: "))
        inicio = float(input("punto de inicio: "))
        final = float(input("punto final: "))
        paso = float(input("valor de paso: "))
        yr = float(input("condicion inicial en y(0): "))

        self.v = Tk()
        self.v.geometry("350x300")
        entra = "x= ", inicio, " y= ", yr
        expr = eval(expr)
        listbox = Listbox(self.v, width=175, height=50)
        listbox.insert(0, entra)
        x1 = 0.0
        y1 = 0.0
        sum = 0.0
        x0 = inicio
        y0 = yr

        punto2 = y0 + paso * ((expr.evalf(subs={x: x0, y: y0})))
        print (punto2)
        o = expr.evalf(subs={x: x0, y: y0})
        print(o)
        f = expr.evalf(subs={x: 1, y: 5})
        print(f)
#d=diferencial()
#d.heun()