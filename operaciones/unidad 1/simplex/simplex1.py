import numpy as np
import simplex2
def variable1(a, rest):

    aux=10000
    pos=0

    for k in range(1,1 + rest):
        s=((a[k][3+rest]))/((a[k][1]))
        if s<aux:
            pos=k
            aux=s
    print pos
    print aux
    x1=pos
    for k1 in range(3+rest,-1,-1):

        a[pos][k1] = (a[pos][k1]) / a[pos][1]
    for o in range(1 + rest):
        for o1 in range(3 + rest,0,-1):
            if o != pos:
                a[o][o1] = a[o][o1]-((a[pos][o1])*(a[o][1]))
    print a
    simplex2.vari1(a,rest,x1)





def variable2(a, rest):

    aux = 10000
    pos = 0

    for k in range(1, 1 + rest):
        s = ((a[k][3 + rest])) / ((a[k][2]))
        if s < aux:
            pos = k
            aux = s
    print pos
    print aux
    x2=pos

    for g in range(2):

        a[pos][g] = (a[pos][g]) / a[pos][2]
    for k1 in range(3 + rest, -1, -1):

        a[pos][k1] = (a[pos][k1]) / a[pos][2]


    for l in range(1 + rest):
        for l1 in range(2):
            if l != pos:
                a[l][l1] = (a[l][l1] - ((a[pos][l1]) * (a[l][2])))
    for o in range(1 + rest):
        for o1 in range(3 + rest, -1, -1):
            if o != pos:
                a[o][o1] = (a[o][o1] - ((a[pos][o1]) * (a[o][2])))
    print a
    simplex2.vari2(a, rest,x2)