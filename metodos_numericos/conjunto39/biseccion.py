import numpy as n
import matplotlib.pyplot as plt
from tkinter import *
class bisecccion:
    def bise(self,xl,xu,tolerancia,r,rr,f):
        #x=0
        #self.e=Tk()
        #self.e = mainloop()
        #xl=12
        #xu=16
        xr=0
        error=0
        aux=0
        #tolerancia=0
        #fxl=lambda x:x**2
        #fxu=lambda x:(x**3)+1
        fxl=lambda x:((((9.8)*(68.1))/x)*(1-n.exp(-(x/68.1)*10)))-40
        fxu=lambda x:((((9.8)*(68.1))/x)*(1-n.exp(-(x/68.1)*10)))-40
        xr=xu-((fxu(xu))*(xl-xu)/(fxl(xl)-fxu(xu)))
        error=((xr-aux)/xr)*100
        listbox = Listbox(f,width=100,height=50)
        #gh="     error           xu           xl           raiz aproximada"
        while error>tolerancia:
            #print fxl(xl)
            #print fxu(xu)
            xr=xu-((fxu(xu))*(xl-xu)/(fxl(xl)-fxu(xu)))
            error=abs((xr-aux)/xr)*100
            aux=xr

            #print "error", error, "%"
            #print xr
            #print fxu(xu)*fxl(xl)
            if fxu(xu)*fxl(xl)<0:
                xu=xr
                #print xl
                #print xu
                #print fxu(xu)*fxl(xl)

            elif fxu(xu)*fxl(xl)>0:
                xl = xr
#                print xl
 #               print xu
            #elif fxu(xu)*fxl(xl)==0:
                #print "raiz: ",xr
            li="error:    ",str(error),"xu:    ",str(xu),"xl:    ",str(xl),"raiz aproximada:    ",str(xr)
            #li= error,"     ",xu,"        ",xl,"         ",xr
            listbox.insert(0,li)
        listbox.place(x=250, y=0)
        x = n.linspace(r, rr, 100)
        fx = ((((9.8)*(68.1))/x)*(1-n.exp(-(x/68.1)*10)))-40

        plt.title("metodo de la falsa pocision")
        plt.plot(x, fx, label="f(x)")
        plt.axhline(0, color='k')
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
        #return listbox
#b=bisecccion()
#b.bise()

#
        # 0,5,0,0,20#