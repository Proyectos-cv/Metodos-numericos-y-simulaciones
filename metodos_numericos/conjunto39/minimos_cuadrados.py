from sympy import *
import numpy as np
from tkinter import *
from tkinter import messagebox
class ajuste:
    def cuadrados(self,x0,x1,x2,x3,x4,y0,y1,y2,y3,y4):
        #se inicializan las variables que se utilizaran
        x, y = symbols("x y")
        a=0
        b=0
        sumx=0
        sumxy=0
        sumxc=0
        sumy=0

        #x0 = float(input("valor de x0: "))
        #x1 = float(input("valor de x1: "))
        #x2 = float(input("valor de x2: "))
        #x3 = float(input("valor de x3: "))
        #x4 = float(input("valor de x4: "))


        #se guardan los puntos en arreglos
        xarre=np.array([x0,x1,x2,x3,x4])
        #y0 = float(input("valor de y0: "))
        #y1 = float(input("valor de y1: "))
        #y2 = float(input("valor de y2: "))
        #y3 = float(input("valor de y3: "))
        #y4 = float(input("valor de y4: "))

        yarre=np.array([y0,y1,y2,y3,y4])

        #se obtienen terminos de sumatoria para utilizarlos en la formula

        for k in range(len(yarre)):
            sumy=sumy+yarre[k]
            sumx=sumx+xarre[k]
        for i in range(len(xarre)):
            sumxy=sumxy+(xarre[i]*yarre[i])
        for j in range(len(xarre)):
            sumxc=sumxc+((xarre[j])**2)
        #print("media x: ",np.mean(xarre))
        #print("media y: ", np.mean(yarre))
        #print("xy: ",sumxy)
        #print("x2: ",sumxc)

        #se obtiene a y b de la formula y=a+bx

        b=((len(xarre)*sumxy)-(sumx*sumy))/((len(xarre)*sumxc)-(sumx)**2)
        a=((sumy*sumxc)-(sumx*sumxy))/((len(xarre)*sumxc)-(sumx)**2)
        #a=(sumy-b*sumx)/len(xarre)

        #se ontiene la ecuacion para los datos
        ecuacion = a+b*(x)
        #print(ecuacion)
        messagebox.showinfo("resultados", ("ecuacion de la funcion: " + str(ecuacion)))


#a=ajuste()
#a.cuadrados()

#valor de x0: 1
#valor de x1: 2
#3valor de x2:
#4valor de x3:
#5valor de x4:
#valor de y0: 220
#valor de y1: 245
#valor de y2: 250
#valor de y3: 258
#valor de y4: 273.5