from sympy import *
from tkinter import messagebox
class tres:
    #se crea esta funcion para una de las tres formulas que se utilizaran
    def primera(self,expr,inco,h):
        #se declaran los valores iniciales
        x, y = symbols("x y")
        #se emplea una funcion para poder tomar la cadena como funcion
        expr = eval(expr)
        #se evaluan algunos puntos para utilizar en la formula
        fx = (expr.evalf(subs={x:inco+h}))
        fx1 = (expr.evalf(subs={x: inco-h}))
        #por medio de la formula se obtiene una aproximacion
        derivada_aproximada=(fx-fx1)*(float(1/(2*h)))
        #se obtiene la derivada verdadera y la derivada de la funcion
        derivada = (diff(expr,x))
        deri=derivada.evalf(subs={x:inco})
        #se calcula el error
        error=abs((deri-derivada_aproximada)/deri)*100
        #SE MANDA UNA VENTANA DE RESULTADOS
        messagebox.showinfo("resultados", "aproximacion: " + str(derivada_aproximada) + '\n'
                            + "derivada de la funcion: " + str(derivada) + '\n'
                            + "derivada real: " + str(deri) + '\n'
                            + "error: " + str(error))

    #esta funcion hace una aproximacion de la derivada por la izquierda
    def izquierda(self,expr,inco,h):
        #se piden los valores iniciales
        x, y = symbols("x y")
        #se declara la funcion
        expr = eval(expr)
        #se evaluan puntos
        fx = (expr.evalf(subs={x: inco}))
        fx1 = (expr.evalf(subs={x: inco - h}))
        fx2 = (expr.evalf(subs={x: inco - 2*h}))
        #se obtiene una aproximacion a la derivada
        derivada_aproximada = (-3*fx + 4*fx1 - fx2)/(-2*h)
        #se obtiene la derivada en el punto y en la funcion
        derivada = (diff(expr, x))
        deri = derivada.evalf(subs={x: inco})
        #se calcula el error
        error = abs((deri - derivada_aproximada) / deri) * 100
        # SE MANDA UNA VENTANA DE RESULTADOS
        messagebox.showinfo("resultados", "aproximacion: " + str(derivada_aproximada) + '\n'
                            + "derivada de la funcion: " + str(derivada) + '\n'
                            + "derivada real: " + str(deri) + '\n'
                            + "error: " + str(error))
    #calcula la derivada por la derecha
    def derecha(self,expr,inco,h):
        #se declaran variables
        x, y = symbols("x y")
        #se declara la funcion
        expr = eval(expr)
        #se evaluan puntos en la funcion
        fx = (expr.evalf(subs={x: inco}))
        fx1 = (expr.evalf(subs={x: inco + h}))
        fx2 = (expr.evalf(subs={x: inco + 2 * h}))
        #se consigue la aproximacion
        derivada_aproximada = (-3 * fx + 4 * fx1 - fx2) / (2 * h)
        #derivada del punto y de la funcion
        derivada = (diff(expr, x))
        deri = derivada.evalf(subs={x: inco})
        #se calcula el error
        error = abs((deri - derivada_aproximada) / deri) * 100
        # SE MANDA UNA VENTANA DE RESULTADOS
        messagebox.showinfo("resultados", "aproximacion: " + str(derivada_aproximada) + '\n'
                            + "derivada de la funcion: " + str(derivada) + '\n'
                            + "derivada real: " + str(deri) + '\n'
                            + "error: " + str(error))
#c=cinco()
#c.primera()
#c.izquierda()
#c.derecha()