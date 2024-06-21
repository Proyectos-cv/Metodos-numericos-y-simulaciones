import numpy as n
import matplotlib.pyplot as plt
class iteraciones():
    def funcion1(self,x):
        #fx= n.exp(-x)-x
        #fx=2 * (n.exp(x ** 2)) - 5 * x
        fx=2*(x**2)-3*x-6
        return fx
    def funcion2(self,x):
        #gx=(2*(n.exp(x**2)))/5
        gx=(6-(2*(x**2)))/-3
        #gx = n.exp(-x)
        return gx
    def itera(self):
        #tolerancia=float(0.000)
        tolerancia = float(0.01)
        xi=float(0)
        #x1=float(0)
        error=n.abs((iteraciones().funcion2(xi)-xi))
        i=0
        #while (error>tolerancia and i<=100):
        while i<=100:
            print (i,'xi=' ,xi, ' f(xi)=', iteraciones().funcion1(xi),' gx(xi)=', iteraciones().funcion2(xi), 'error v= ', error)
            if i>0:
                error=n.abs(iteraciones().funcion2(xi)-xi)
            xi=iteraciones().funcion2(xi)
            i=i+1
        print (i, 'xi=', xi, ' f(xi)=', iteraciones().funcion1(xi), ' gx(xi)=', iteraciones().funcion2(xi), 'error v= ', error)
        print"el valor de x, tal que f(x)=0 es: ", xi
        print"error ", error
        x=n.linspace(-3,1.5,100)
        plt.title("metodo de punto fijo")
        plt.plot(x,iteraciones().funcion1(x),label="f(x)")
        plt.plot(x,iteraciones().funcion2(x),label="f(g)")
        plt.plot(x,x,label="f(x) = x")
        plt.axvline(xi,label="f(x) = 0, x={xi:.6f }",color='k')
        plt.axhline(0,color='k')
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
i=iteraciones()
i.itera()