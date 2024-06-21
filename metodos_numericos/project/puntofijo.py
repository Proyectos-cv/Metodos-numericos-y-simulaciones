import numpy as n
import matplotlib.pyplot as plt
import numpy as np
class iteraciones():
    def funcion1(self,x):
        #fx= n.exp(-x)-x
        fx=2 * (n.exp(x ** 2)) - 5 * x

        return fx
    def funcion2(self,x):
        gx=(2*(n.exp(x**2)))/5
        #gx = n.exp(-x)
        return gx
    def itera(self,a,b,c,d):
        #e = (-a*x +e)/c
        #f = (-b*x + f)/d
        #fx = lambda x: e
        #gx = lambda x: f
        #x = np.linspace(-200, 200, 5)
        #fx=lambda x: a
        #gx=lambda x: b
        #aa = fx(x)
        #bb = gx(x)
        #cc= hx(x)
        #dd= rx(x)

        #l=[-200,200,-200,200]

        #plt.plot(x, aa, color="red")
        #plt.plot(x, bb, color="green")
        #plt.show()

        #tolerancia=float(0.000)
        tolerancia = float(0.01)
        #tolerancia=c
        xi=float(0)
        #xi=float(d)
        #x1=float(0)
        error=n.abs(iteraciones().funcion2(xi)-xi)
        i=0
        while (error>tolerancia and i<=100):
            print (i,'xi=' ,xi, ' f(xi)=', iteraciones().funcion1(xi),' gx(xi)=', iteraciones().funcion2(xi), 'error v= ', error)
            if i>0:
                error=n.abs(iteraciones().funcion2(xi)-xi)
            xi=iteraciones().funcion2(xi)
            i=i+1
        print (i, 'xi=', xi, ' f(xi)=', iteraciones().funcion1(xi), ' gx(xi)=', iteraciones().funcion2(xi), 'error v= ', error)
        print"el valor de x, tal que f(x)=0 es: ", xi
        print"error ", error
        x=n.linspace(0,1.5,100)
        plt.title("metodo de punto fijo")
        plt.plot(x,iteraciones().funcion1(x),label="f(x)")
        plt.plot(x,iteraciones().funcion2(x),label="f(g)")
        plt.plot(x,x,label="f(x) = x")
        plt.axvline(xi,label="f(x) = 0, x={xi:.6f }",color='k')
        plt.axhline(0,color='k')
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
        #print fx,gx,tolerancia,xi
#i=iteraciones()
#i.itera()