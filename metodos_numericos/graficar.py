import numpy as np
import matplotlib.pyplot as m
class grafica:
    def f(self,x):
        return np.sin(10*x)+np.cos(3*x)
    def muestra(self):
        valor=g.f(5)
        print valor
        y=np.linspace(0,10,100)
        m.plot(y,g.f(y))
        m.grid()



g=grafica()
g.muestra()