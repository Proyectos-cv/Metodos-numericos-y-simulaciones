import numpy as np
a=np.array([5,3,2])
print len(a)
#print a
#for i in range(2):
    #for j in range(2):
        #if a[j]>a[j+1]:
           # s = a[j]
            #a[j]=a[j+1]
            #a[j+1]=s
#print a

#a=float(10)/float(3)
#print a
#a=np.array([[2,4,6],[4,5,6],[3,1,-2]])
#b=np.array([18,24,4])
#x=np.linalg.solve(a,b)
#s=int(x[0])
#print x

#print float(x[0])
#print float(x[1])
#print float(x[2])
#print float(x[0]+x[1])



#import matplotlib.pyplot as plt
#import numpy as np
#x = np.linspace(-140, 140, 5)
#y = np.linspace(-130,130, 5)
#fx=lambda x: 3*x+ 2 * y
#aa=fx(x)
#plt.plot(x, aa, color="red")
#plt.subplot()
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

gana = 0
aux = 0
aux1 = 0
for o in range(4):
    w = z * p[o]
    w1 = z1 * p1[1]
    gan = w + w1
    if p[o] > 0 and p1 > 0 and ((p[o] <= q[0])) and ((p1[o] <= q1[0])) and (gan > gana):
        gana = gan
        aux = p[o]
        aux1 = p1[o]
print "optimo", gana
print"punto x", aux
print"punto y", aux1

for t in range(5):
    for y in range(5):
        if p[y] > p[y + 1] and p[y] > 0 and p[y + 1] > 0:
            s2 = p[y]
            p[y] = p[y + 1]
            p[y + 1] = s2
print p

for t1 in range(5):
    for y1 in range(5):
        if p1[y1] > p1[y1 + 1] and p1[y1] > 0 and p1[y1 + 1] > 0:
            s3 = p1[y1]
            p1[y1] = p1[y1 + 1]
            p1[y1 + 1] = s3
