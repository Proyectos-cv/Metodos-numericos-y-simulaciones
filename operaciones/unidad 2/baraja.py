import random as r
n=0
band=True
while band==True:
    a=r.randrange(1,14)
    b=r.randrange(1,5)
    n=n+1
    if a==13 and b==1:
        band = False
print "numero de veces para k de corazones: ", n
