import numpy as np
def f(x):
    f1=x[0]**2+x[1]**2-1
    f2=4*x[0]**2/9+4*x[1]**2-1
    return np.array([f1,f2])
def df(x):
    return np.array([[2*x[0],2*x[1]],
                     [8*x[0]/9,8*x[1]]])
n=100
x=np.array([1,1])
for k in range (n):
    xold=x
    jinv=np.linalg.inv(df(x))
    x=x-np.dot(jinv,f(x))
    #x=np.linalg.solve(df(x),df(x)* x - fx(x))
    e=np.linalg.norm(x-xold)
    print (k,x,e)
    if e<1e-10:
        break