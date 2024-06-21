from sympy import *
import numpy as np
from tkinter import messagebox
class cuadratura:
    def proceso(self,expr,a,b,n):
        #se ingresan valores iniciales y se inicializan variables
        x, y = symbols("x y")
        sumatoria=0
        expr = eval(expr)
        w = np.array([1, 1])
        z = np.array([-0.5773502692, 0.5773502692])
        band=False
        #condicionales para saber cual valor de n es con el que se esta trabajando, y asignar valores predeterminados por el metodo
        if n==2:
            w=np.array([1,1])
            z=np.array([-0.5773502692,0.5773502692])
            band=True
        elif n==3:
            w=np.array([0.5555555555,0.8888888888,0.5555555555])
            z=np.array([-0.7745966692,0,0.7745966692])
            band = True
        elif n==4:
            w = np.array([0.3478548451, 0.6521451549,0.6521451549, 0.3478548451])
            z = np.array([-0.8611363116, -0.3399810436,0.8611363116, 0.3399810436])
            band = True
        elif n==5:
            w = np.array([0.2369268851, 0.4786286705, 0.5688888888, 0.4786286705,0.2369268851])
            z = np.array([-0.9061798459, -0.5384693101,0,0.5384693101,0.9061798459])
            band = True
        elif n==6:
            w = np.array([0.1713244924, 0.3607615730, 0.4679139346,0.4679139346, 0.3607615730,0.1713244924])
            z = np.array([-0.9324695142, -0.6612093865, -0.2386191861, 0.2386191861,0.6612093865,0.9324695142])
            band = True
        else:
            messagebox.showinfo("advertencia","n debe ser un valor entero entre 2 y 6")
        #se hace una sumatoria de acuerdo a n, (solo es una porcion de la formula del metodo)
        if band==True:
            for i in range(0,n):
                sumatoria = sumatoria+(expr.evalf(subs={x: (w[i]*(((b-a)/2)*z[i]+((a+b)/2)))}))
            #se aplica el resto de la formula para obtener la aproximacion
            integracion_aproximada =((b-a)/2)*sumatoria
            #se calculan los valores reales
            integ=integrate(expr, x)
            inte = integrate(expr, (x, a, b))
            #se calcula el error
            error = abs((inte - integracion_aproximada) / inte) * 100
            messagebox.showinfo("resultados", "aproximacion: " + str(integracion_aproximada) + '\n'
                                + "derivada de la funcion: "+str(integ)+ '\n'
                                + "derivada real: "+str(inte)+ '\n'
                                + "error: "+str(error))
#c=cuadratura()
#c.proceso()