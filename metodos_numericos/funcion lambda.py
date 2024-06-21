import numpy as np
import matplotlib.pyplot as plt
from Tkinter import *

#x = np.linspace(-20, 20, 5)
#y = np.linspace(-200, 200, 5)

class evalua:
    def ven(self):
        self.ventana = Tk()

        self.ventana.geometry("370x250")
        self.ventana.config(bg="gray")

        Label(self.ventana, font=("ROCKWELL", 18), fg='black', text="metodos", bg='gray').place(x=10, y=0)
        self.dat = IntVar()
        self.caja1=Entry(self.ventana, textvariable=self.dat).place(x=70, y=50)
        Button(self.ventana, font=("INK FREE", 18), fg='black', text="punto fijo", bg='gray', command=self.asigna1,relief=FLAT).place(x=70, y=150)
        self.ventana = mainloop()
    def asigna1(self):
        #a=self.dat.get()
        #s=lambda x: a
        p=lambda x: (x**2)+1
        print p(2)
        #print s(1)
    def asigna(self):
        x = np.linspace(-1.5, 1.5, 100)
        e = (x ** 3)
        f = (2 * (np.exp(x ** 2))) / 5
        fx = lambda x: e
        gx = lambda x: f


        a = lambda base, area: (base * area) / 2
        print (a(7, 5))

        aa = fx(x)
        bb = gx(x)

        # l = [-200, 200, -200, 200]

        plt.plot(x, aa, color="red")
        plt.plot(x, bb, color="green")

        plt.grid()
        plt.show()
e=evalua()
e.ven()