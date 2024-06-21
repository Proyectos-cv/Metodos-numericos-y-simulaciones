import numpy as np
def vari1(a,rest,x1):
    aux = 10000
    pos = 0

    for k in range(1, 1 + rest):
        s = ((a[k][3 + rest])) / ((a[k][2]))
        if s < aux:
            pos = k
            aux = s
    print pos
    print aux

    for g in range(2):
        #a[pos][k1] = (a[pos][k1]) / aux
        a[pos][g] = (a[pos][g]) / a[pos][2]
    #for k1 in range(4 + rest):
    for k1 in range(3 + rest,-1,-1):
        #a[pos][k1] = (a[pos][k1]) / aux
        a[pos][k1] = (a[pos][k1]) / a[pos][2]



    for l in range(1 + rest):
        for l1 in range(2):
            if l != pos:
                a[l][l1] = a[l][l1] - ((a[pos][l1]) * (a[l][2]))


    for o in range(1 + rest):
        for o1 in range(3 + rest, 0, -1):
            if o != pos:
                a[o][o1] = a[o][o1] - ((a[pos][o1]) * (a[o][2]))
    print a
    print "x1= ", a[x1][3 + rest]
    print "x2= ", a[pos][3 + rest]
    print "z= ", a[0][3 + rest]



def vari2(a,rest,x2):
    aux = 10000
    pos = 0

    for k in range(1, 1 + rest):
        s = ((a[k][3 + rest])) / ((a[k][1]))
        if float(s) < aux:
            pos = k
            aux = float(s)
    print pos
    print aux



    for k1 in range(3 + rest, -1, -1):
        # a[pos][k1] = (a[pos][k1]) / aux
        a[pos][k1] = (a[pos][k1]) / a[pos][1]

    for o in range(1 + rest):
        for o1 in range(3 + rest, 0, -1):
            if o != pos:
                a[o][o1] = (a[o][o1] - ((a[pos][o1]) * (a[o][1])))
    print a
    print "x1= ",float(a[pos][3+rest])
    print "x2= ",float(a[x2][3+rest])
    print "z= ",float(a[0][3+rest])