from sympy import *
class derivada:
    def proceso(self):
        #se piden los valores iniciales
        x, y = symbols("x y")
        expr=(input("funcion: "))
        inco=float(input("valor de x: "))
        h=float(input("valor del incremento: "))
        #se consigue un incremento
        inco1=inco+h
        #se obtiene la funcion para evaluar
        expr = eval(expr)
        #se evaluan puntos en la funcion
        fx=(expr.evalf(subs={x:inco}))
        fx1=(expr.evalf(subs={x:inco1}))
        #se consigue una aproximacion
        derivada_aproximada=(fx1-fx)/h
        print("derivada aproximada: ",derivada_aproximada)
        #se obtienen valores reales para calcular el error
        print ("derivada: ",diff(expr,x))
        derivada = (diff(expr,x))
        deri=derivada.evalf(subs={x:inco})
        print ("derivada real: ",deri)
        #se calcula el error
        error=abs((deri-derivada_aproximada)/deri)*100
        print("error: ",error,"%")

d=derivada()
d.proceso()