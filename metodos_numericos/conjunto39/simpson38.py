from sympy import *
from tkinter import messagebox
class simpson2:
    def proceso(self,expr,a,b):
        #se inicializan variables con datos de entrada y se calculan incremetnos
        x, y = symbols("x y")
        h=(b-a)/3
        medio1=a+h
        medio2 = medio1 + h
        expr = eval(expr)
        #se evaluan puntos en la funcion
        fx = (expr.evalf(subs={x: a}))
        fx1 = (expr.evalf(subs={x: medio1}))
        fx2 = (expr.evalf(subs={x: medio2}))
        fx3 = (expr.evalf(subs={x: b}))
        #se consigue la aproximacion
        integracion_aproximada = ((3*h/8)*(fx+3*fx1+3*fx2+fx3))
        #se obtienen los valores reales
        integ=integrate(expr, x)
        inte = integrate(expr, (x, a, b))
        #se calcula el error
        error = abs((inte - integracion_aproximada) / inte) * 100
        #SE MANDA VENTANA DE RESULTADOS
        messagebox.showinfo("resultados", "aproximacion: " + str(integracion_aproximada) + '\n'
                            + "derivada de la funcion: " + str(integ) + '\n'
                            + "derivada real: " + str(inte) + '\n'
                            + "error: " + str(error))
#s=simpson2()#
#s.proceso()