from sympy import *
import numpy
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

class interpolacion:
    def newton(self,expr,x0,x1,x2,x3):
        x, y = symbols("x y")

        #expr = (input("funcion a aproximar: "))

        #x0=float(input("valor de x0: "))
        #x1 = float(input("valor de x1: "))
        #x2 = float(input("valor de x2: "))
        #x3 = float(input("valor de x3: "))

        expr = eval(expr)

        #una vez con los puntos en x se consigun los puntos en y con la funcion dada

        fx = (expr.evalf(subs={x: x0}))
        fx1 = (expr.evalf(subs={x: x1}))
        fx2 = (expr.evalf(subs={x: x2}))
        fx3 = (expr.evalf(subs={x: x3}))

        #se ponen los datos en arreglos para una manipulacion mas sencilla

        arr=numpy.array([x0,x1,x2,x3])
        arre=numpy.array([fx,fx1,fx2,fx3])
        arre1 = numpy.zeros(3)
        arre2 = numpy.zeros(2)

        #con cilos se consiguen los datos para sustituir en el polinomio de newton

        for i in range((len(arre))-1):
            f=(arre[i+1]-arre[i])/(arr[i+1]-arr[i])
            #print (f)
            arre1[i]=f

        for j in range((len(arre1))-1):
            f1=(arre1[j+1]-arre1[j])/(arr[j+2]-arr[j])
            arre2[j]=f1

        fs=(arre2[0]-arre2[1])/(arr[0]-arr[3])

        #se sustituyen los datos anteriores en el polinomio de newton

        fa= arre[0]+(arre1[0]*(x-arr[0]))+(arre2[0]*(x-arr[0])*(x-arr[1]))+(fs*(x-arr[0])*(x-arr[1])*(x-arr[2]))
        messagebox.showinfo("resultados", ("ecuacion de la funcion: " + str(fa)))
        #print (fa)
        #fa = eval(fa)

        #x = numpy.linspace(0, 10, 10)
        #plt.plot(x, expr.evalf(subs={x: x}))
        #plt.plot(x, fa.evalf(subs={x: x}))
        #plt.show()

   # https: // www.youtube.com / watch?v = AISHH6goWUs
    def a(self):
        x=numpy.linspace(0,10,100)
        f=numpy.sin(x)
        plt.plot(x,expr)
        plt.show()
#i=interpolacion()
#i.newton()
#i.a()