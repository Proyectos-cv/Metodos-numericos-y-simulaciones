import numpy as n
import matplotlib.pyplot as plt
from tkinter import *
class falso:
    def falsaposicion(self,xl,xu,tolerancia,r,rr,b):
    #def falsaposicion(self):
        #xl = float(0)
        #xu = float(1)
        aux = 0
        #tolerancia = 0
        #fxl = lambda x: ((((9.8) * (68.1)) / x) * (1 - n.exp(-(x / 68.1) * 10))) - 40
        #fxu = lambda x: ((((9.8) * (68.1)) / x) * (1 - n.exp(-(x / 68.1) * 10))) - 40
        fxu = lambda x: (x**4)+(3*(x**3))-2
        fxl = lambda x: (x**4)+(3*(x**3))-2

        xr =float((xl+xu)/2)
        error = ((xr - aux) / xr) * 100

        listbox = Listbox(b, width=175, height=50)
        while error > tolerancia:
            #print fxl(xl)
            #print fxu(xu)
            xr = float((xl+xu)/2)
            error = abs((xr - aux) / xr) * 100
            aux = xr
#            print "error", error, "%"
 #           print xl
  #          print xu
   #         print xr
            #print fxu(xu) * fxl(xr)
            if fxu(xu) * fxl(xr) < 0:
                #xu = xr
                xl = xr
                #print xl
                #print xu
                #print fxu(xu) * fxl(xr)
                #print "xr= ",xr
            elif fxu(xu) * fxl(xr) > 0:
                #xl = xr
                xu = xr
                #print xl
                #print xu
               # print "xr= ", xr
            #elif fxu(xu) * fxl(xr) == 0:
                #print "raiz: ", xr
                #print xu
                #print xl
            li = "error:    ", error, "xu:    ", xu, "xl:    ", xl, "raiz aproximada:    ", xr
            listbox.insert(0, li)
        listbox.place(x=300, y=0)
        x = n.linspace(r, rr, 100)
        fx = (x**4)+(3*(x**3))-2

        plt.title("metodo de biseccion")
        plt.plot(x, fx, label="f(x)")
        plt.axhline(0, color='k')
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
#f=falso()
#f.falsaposicion()

#x1=2
    #xl=4
    #toler=0
    #lim inf=0
    #lim sup=30    #