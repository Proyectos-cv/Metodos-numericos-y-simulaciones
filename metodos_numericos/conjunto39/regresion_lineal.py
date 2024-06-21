from sympy import *
import numpy as np
from tkinter import *
from tkinter import messagebox
class ajuste:
    def regresion(self,x0,x1,x2,x3,x4,x5,y0,y1,y2,y3,y4,y5):
        #se inicializan variables
        x, y = symbols("x y")
        a=0
        b=0
        sumxy=0
        sumxc=0

        #se almacenan las variables en arreglos

        #x0 = float(input("valor de x0: "))
        #x1 = float(input("valor de x1: "))
        #x2 = float(input("valor de x2: "))
        #x3 = float(input("valor de x3: "))
        #x4 = float(input("valor de x4: "))
        #x5 = float(input("valor de x5: "))
        xarre=np.array([x0,x1,x2,x3,x4,x5])
        #y0 = float(input("valor de y0: "))
        #y1 = float(input("valor de y1: "))
        #y2 = float(input("valor de y2: "))
        #y3 = float(input("valor de y3: "))
        #y4 = float(input("valor de y4: "))
        #y5 = float(input("valor de y5: "))
        yarre=np.array([y0,y1,y2,y3,y4,y5])

        #se obtienen valores para utilizar la formula

        for i in range(len(xarre)):
            sumxy=sumxy+(xarre[i]*yarre[i])
        for j in range(len(xarre)):
            sumxc=sumxc+((xarre[j])**2)
        #print("media x: ",np.mean(xarre))
        #print("media y: ", np.mean(yarre))
        #print("xy: ",sumxy)
        #print("x2: ",sumxc)

        #se obtienen los valores de a y b de la formula y= a+bx

        b=((sumxy)-(len(xarre)*np.mean(xarre)*np.mean(yarre)))/((sumxc)-(len(xarre)*(np.mean(xarre))**2))
        #print("b= ",b)
        a=np.mean(yarre)-b*np.mean(xarre)
        #print("a= ",a)

        #se obtiene la formula sustituyendo a y b

        ecuacion = a+b*(x)
       # print(ecuacion)
        messagebox.showinfo("resultados", ("ecuacion de la funcion: " + str(ecuacion)))
#a=ajuste()
#a.regresion()

#valor de x0: 1
#valor de x1: 3
#valor de x2: 4
#valor de x3: 2
#1valor de x4:
#valor de x5: 7
#valor de y0: 2
#valor de y1: 3
#valor de y2: 2.5
#valor de y3: 2
#valor de y4: 2
#valor de y5: 3.5

