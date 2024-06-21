from sympy import *
from tkinter import *
from tkinter import messagebox
class cinco:
    def proceso(self,expr,inco,h):
        x, y = symbols("x y")
        #se emplea una funcion para poder tomar la cadena como funcion
        expr = eval(expr)
        #se evaluan algunos puntos en la funcion
        fx = (expr.evalf(subs={x:inco-2*h}))
        fx1 = (expr.evalf(subs={x: inco-h}))
        fx2 = (expr.evalf(subs={x: inco+h}))
        fx3 = (expr.evalf(subs={x: inco+2*h}))
        #por medio de la formula se consigue un resultado aproximado
        derivada_aproximada= (fx-8*fx1+8*fx2-fx3) / (12*h)
        #se obtiene la derivada real en el punto y la derivada real de la funcion
        derivada = (diff(expr,x))
        deri=derivada.evalf(subs={x:inco})
        #se calcula el error
        error=abs((deri-derivada_aproximada)/deri)*100
        #SE MANDA UNA VENTANA DE RESULTADOS
        messagebox.showinfo("resultados", "aproximacion: " + str(derivada_aproximada) + '\n'
                            + "derivada de la funcion: "+str(derivada)+ '\n'
                            + "derivada real: "+str(deri)+ '\n'
                            + "error: "+str(error))
#c=cinco()
#c.proceso()

