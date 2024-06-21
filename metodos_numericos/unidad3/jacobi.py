import numpy as n

class jacob:
    def jacobi(self):
            n=4
            a=n.random.rand(n,n)
        b=n.random.rand(n,)
        alpha=3*n
        add=n.dot(a,a.t)+alpha.identy(n)
        a=add
        print a
j=jacob()
j.jacobi()