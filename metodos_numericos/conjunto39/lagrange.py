# Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
class interpolacion:
    def lagrange(self,expr,x0,x1,x2):
        x, y = symbols("x y")

        #expr = (input("funcion a aproximar: "))

        #x0 = float(input("valor de x0: "))
        #x1 = float(input("valor de x1: "))
        #x2 = float(input("valor de x2: "))


        expr = eval(expr)

        #una vez con los valores de x se consiguen los valores de y

        fx = (expr.evalf(subs={x: x0}))
        fx1 = (expr.evalf(subs={x: x1}))
        fx2 = (expr.evalf(subs={x: x2}))
        #fx3 = (expr.evalf(subs={x: x3}))

        #se aplica la formula de la interpolacion de lagrange para los puntos predeterminados y se consigue el polinomio

        fa=(((x-x1)*(x-x2))/((x0-x1)*(x0-x2)))*fx +(((x-x0)*(x-x2))/((x1-x0)*(x1-x2)))*fx1+(((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))*fx2
        messagebox.showinfo("resultados", ("ecuacion de la funcion: " + str(fa)))
        print("lagrange: ",fa)


    def a(self):
        # INGRESO , Datos de prueba
        xi = np.array([0, 0.2, 0.3, 0.4])
        fi = np.array([1, 1.6, 1.7, 2.0])

        # PROCEDIMIENTO
        # Polinomio de Lagrange
        n = len(xi)
        x = sym.Symbol('x')
        polinomio = 0
        divisorL = np.zeros(n, dtype=float)
        for i in range(0, n, 1):

            # Termino de Lagrange
            numerador = 1
            denominador = 1
            for j in range(0, n, 1):
                if (j != i):
                    numerador = numerador * (x - xi[j])
                    denominador = denominador * (xi[i] - xi[j])
            terminoLi = numerador / denominador

            polinomio = polinomio + terminoLi * fi[i]
            divisorL[i] = denominador

        # simplifica el polinomio
        polisimple = polinomio.expand()

        # para evaluacin numrica
        px = sym.lambdify(x, polisimple)

        # Puntos para la grfica
        muestras = 101
        a = np.min(xi)
        b = np.max(xi)
        pxi = np.linspace(a, b, muestras)
        pfi = px(pxi)

        # SALIDA
        print('    valores de fi: ', fi)
        print('divisores en L(i): ', divisorL)
        print()
        print('Polinomio de Lagrange, expresiones')
        print(polinomio)
        print()
        print('Polinomio de Lagrange: ')
        print(polisimple)

        # Grfica
        plt.plot(xi, fi, 'o', label='Puntos')
        plt.plot(pxi, pfi, label='Polinomio')
        plt.legend()
        plt.xlabel('xi')
        plt.ylabel('fi')
        plt.title('Interpolacin Lagrange')
        plt.show()


        #http://blog.espol.edu.ec/analisisnumerico/interpolacion-de-lagrange/
#i=interpolacion()
#i.lagrange()