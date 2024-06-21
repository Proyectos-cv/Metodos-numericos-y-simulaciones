import matplotlib.pyplot as plt
import numpy as n
from tkinter import *
class iteraciones():
    def funcion1(self,x):
        #fx= n.exp(-x)-x
        fx=2 * (n.exp(x ** 2)) - 5 * x

        return fx
    def funcion2(self,x):
        gx=(2*(n.exp(x**2)))/5
        #gx = n.exp(-x)
        return gx
    def itera(self,xi,tolerancia,r,rr,l):
        #tolerancia=float(0.000)
        #tolerancia = float(0.01)
        #xi=float(0)
        #x1=float(0)
        error=n.abs(iteraciones().funcion2(xi)-xi)
        i=0
        listbox = Listbox(l, width=175, height=50)
        while (error>tolerancia and i<=100):
            a=(i,'xi=' ,xi, ' f(xi)=', iteraciones().funcion1(xi),' gx(xi)=', iteraciones().funcion2(xi), 'error v= ', error)
            listbox.insert(0,a)
            if i>0:
                error=n.abs(iteraciones().funcion2(xi)-xi)
            xi=iteraciones().funcion2(xi)
            i=i+1
        a=(i, 'xi=', xi, ' f(xi)=', iteraciones().funcion1(xi), ' gx(xi)=', iteraciones().funcion2(xi), 'error v= ', error)
        listbox.insert(0,a)
        listbox.place(x=300, y=0)
        #print"el valor de x, tal que f(x)=0 es: ", xi
        #print"error ", error
        #x=n.linspace(r,rr,100)
        #plt.title("metodo de punto fijo")
        #plt.plot(x,iteraciones().funcion1(x),label="f(x)")
        #plt.plot(x,iteraciones().funcion2(x),label="f(g)")
        #plt.plot(x,x,label="f(x) = x")
        #plt.axvline(xi,label="f(x) = 0, x={xi:.6f }",color='k')
        #plt.axhline(0,color='k')
        #plt.legend(loc='upper right')
        #plt.grid()
        #plt.show()
#i=iteraciones()
#i.itera()


#
        #
        # 0,0.01,0,20#