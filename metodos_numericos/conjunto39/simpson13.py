from sympy import *
from tkinter import messagebox
class simpson:
    def proceso(self,expr,a,b):
        #pedir datos de entrada
        x, y = symbols("x y")
        #se calculan unos incrementos
        h=(b-a)/2
        medio=a+h
        #se expresa la funcion ingresada
        expr = eval(expr)
        #se evaluan puntos en la funcion
        fx = (expr.evalf(subs={x: a}))
        fx1 = (expr.evalf(subs={x: medio}))
        fx2 = (expr.evalf(subs={x: b}))
        #se consigue la aproximacion
        integracion_aproximada = ((h/3)*(fx+4*fx1+fx2))
        #se obtienen los valores reales
        integ=integrate(expr, x)
        inte = integrate(expr, (x, a, b))
        #se calcula el error
        error = abs((inte - integracion_aproximada) / inte) * 100
        #SE MANDA VENTANA DE RESULTADOS
        messagebox.showinfo("resultados", "aproximacion: " + str(integracion_aproximada) + '\n'
                            + "integral de la funcion: " + str(integ) + '\n'
                            + "integral real: " + str(inte) + '\n'
                            + "error: " + str(error))
#s=simpson()
#s.proceso()