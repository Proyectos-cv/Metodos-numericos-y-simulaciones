import numpy as n
import matplotlib.pyplot as plt
import numpy as n
class grafic:
    def intervalo(self,a,b):
        #x=n.linspace(0,1.5,100)
        x = n.linspace(a, b, 100)
        fx = 2 * (n.exp(x ** 2)) - 5 * x
        gx = (2 * (n.exp(x ** 2))) / 5

        plt.title("metodo de punto fijo")
        plt.plot(x,fx,label="f(x)")
        plt.plot(x,gx,label="f(g)")
        plt.plot(x,x,label="f(x) = x")
        plt.axhline(0,color='k')
        plt.legend(loc='upper right')
        plt.grid()
        plt.show()
#g=grafic()
#g.intervalo()