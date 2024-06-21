from sympy import *
from tkinter import messagebox
class trapecio:
    def proceso(self,expr,a,b):
        #se inicializan variables y se ingresan datos iniciales
        x, y = symbols("x y")
        expr = eval(expr)
        #se evaluan puntos
        fx=(expr.evalf(subs={x:a}))
        fx1=(expr.evalf(subs={x:b}))
        #por formula se consigue una aproximacion
        integracion_aproximada = ((b-a)*((fx+fx1)/2))
        #se consiguen datos reales
        int=integrate(expr,x)
        inte=integrate(expr,(x,a,b))
        #se calcula el error
        error = abs((inte - integracion_aproximada) / inte) * 100
        #SE MANDA VENTANA DE RESULTADOS
        messagebox.showinfo("resultados", "aproximacion: " + str(integracion_aproximada) + '\n'
                            + "integral de la funcion: " + str(int) + '\n'
                            + "integral real: " + str(inte) + '\n'
                            + "error: " + str(error))
#t=trapecio()
#t.proceso()