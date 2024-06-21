import matplotlib.pyplot as plt
import numpy as np
class trabajo:
    def puntos(self,a,b,c,d,e,f,a1,b1,c1,d1,e1,f1,z,z1):
        #print a,b,c,d
        x1=(float(e)/float(a))
        x2 = (float(f) / float(b))
        y1 = (float(e) / float(c))
        y2 = (float(f) / float(d))
        if e1 !=0 and a1!=0:
            x3 = (float(e1) / float(a1))
        else:
            pass
        if f1 != 0 and b1 != 0:
            x4 = (float(f1) / float(b1))
        else:
            pass
        if e1 != 0 and c1 != 0:
            y3 = (float(e1) / float(c1))
        else:
            pass
        if f1 != 0 and d1 != 0:
            y4 = (float(f1) / float(d1))
        else:
            pass

        #print x1,x2,y1,y2,y3,y4,x3,x4
        if  a1!=0 and c1!=0 and b1!=0 and d1!=0:
            q = np.array([x1, x2, x3, x4])
            q1 = np.array([y1, y2, y3, y4])

            for i in range(3):
                for j in range(3):
                    if q[j] > q[j + 1]:
                        s = q[j]
                        q[j] = q[j + 1]
                        q[j + 1] = s
            print q

            for i in range(3):
                for j in range(3):
                    if q1[j] > q1[j + 1]:
                        s1 = q1[j]
                        q1[j] = q1[j + 1]
                        q1[j + 1] = s1
            print q1

            l=np.array([a,c])
            l1 = np.array ([b,d])
            l2 = np.array([a1,c1])
            l3 = np.array([b1,d1])

            print l
            print l1
            unoa = np.array([l,l1])
            unob = np.array([e, f])
            x = np.linalg.solve(unoa, unob)
            print x
            dosa = np.array([l,l2])
            dosb = np.array([e, e1])
            dosx = np.linalg.solve(dosa, dosb)
            print dosx
            tresa = np.array([l,l3])
            tresb = np.array([e, f1])
            tresx = np.linalg.solve(tresa, tresb)
            print tresx
            cuatroa = np.array([l1,l2])
            cuatrob = np.array([f, e1])
            cuatrox = np.linalg.solve(cuatroa, cuatrob)
            print cuatrox
            cincoa = np.array([l1,l3])
            cincob = np.array([f, f1])
            cincox = np.linalg.solve(cincoa, cincob)
            print cincox
            seisa = np.array([l2,l3])
            seisb = np.array([e1, f1])
            seisx = np.linalg.solve(seisa, seisb)
            print seisx

            p=np.array([x[0],dosx[0],tresx[0],cuatrox[0],cincox[0],seisx[0]])
            p1=np.array([x[1],dosx[1],tresx[1],cuatrox[1],cincox[1],seisx[1]])
            aux=10000000
            aux1=0
            print p
            print p1
            for o in range (len(p)):
                if (p[o]<q[0]) and (p[o]>0) and p[o]<aux:
                    aux=p[o]
                    aux1=p1[o]
            j=(aux*z)+(aux1*z1)
            print aux
            print aux1
            aux3 = 10000000
            aux4=0
            for o in range(len(p1)):
                if p1[o] < q1[0] and p1[o] > 0 and p1[o] < aux3:
                    aux4 = p1[o]
                    aux3 = p[o]

            j1=(aux3*z)+(aux4*z1)
            print aux3
            print aux4
            if j>j1:
                print"optimo: ",j
                print"punto en x: ",aux
                print"punto en y: ",aux1
            elif j<j1:
                print"optimo: ",j1
                print"punto en x: ",aux3
                print"punto en y: ",aux4
            elif j==j1:
                print"optimo: ",j
                print"punto en x: ",aux
                print"punto en y: ",aux1
        elif  a1!=0 and c1!=0 and b1==0 and d1==0:
            q = np.array([x1, x2, x3])
            q1 = np.array([y1, y2, y3])

            for i in range(2):
                for j in range(2):
                    if q[j] > q[j + 1]:
                        s = q[j]
                        q[j] = q[j + 1]
                        q[j + 1] = s
            print q

            for i in range(2):
                for j in range(2):
                    if q1[j] > q1[j + 1]:
                        s1 = q1[j]
                        q1[j] = q1[j + 1]
                        q1[j + 1] = s1
            print q1

            l=np.array([a,c])
            l1 = np.array ([b,d])
            l2 = np.array([a1,c1])


            print l
            print l1
            unoa = np.array([l,l1])
            unob = np.array([e, f])
            x = np.linalg.solve(unoa, unob)
            print x
            dosa = np.array([l,l2])
            dosb = np.array([e, e1])
            dosx = np.linalg.solve(dosa, dosb)
            print dosx

            tresa = np.array([l1,l2])
            tresb = np.array([f, e1])
            tresx = np.linalg.solve(tresa, tresb)
            print tresx



            p=np.array([x[0],dosx[0],tresx[0]])
            p1=np.array([x[1],dosx[1],tresx[1]])
            aux=10000000
            aux1=0
            for o in range (len(p)):
                if p[o]<q[0] and p[o]>0 and p[o]<aux:
                    aux=p[o]
                    aux1=p1[o]
            j=(aux*z)+(aux1*z1)
            print aux
            print aux1
            aux3 = 10000000
            aux4=0
            for o in range(len(p1)):
                if p1[o]<q1[0] and p1[o]>0 and p1[o]<aux3:
                    aux3 = p[o]
                    aux4 = p1[o]
            j1=(aux3*z)+(aux4*z1)
            print aux3
            print aux4
            if j>j1:
                print"optimo: ",j
                print"punto en x: ",aux
                print"punto en y: ",aux1
            elif j<j1:
                print"optimo: ",j1
                print"punto en x: ",aux3
                print"punto en y: ",aux4
            elif j==j1:
                print"optimo: ",j
                print"punto en x: ",aux
                print"punto en y: ",aux1
        elif  a1==0 and c1==0 and b1==0 and d1==0:
            q = np.array([x1, x2])
            q1 = np.array([y1, y2])

            for i in range(1):
                for j in range(1):
                    if q[j] > q[j + 1]:
                        s = q[j]
                        q[j] = q[j + 1]
                        q[j + 1] = s
            print q

            for i in range(1):
                for j in range(1):
                    if q1[j] > q1[j + 1]:
                        s1 = q1[j]
                        q1[j] = q1[j + 1]
                        q1[j + 1] = s1
            print q1

            l=np.array([a,c])
            l1 = np.array ([b,d])


            print l
            print l1
            unoa = np.array([l,l1])
            unob = np.array([e, f])
            x = np.linalg.solve(unoa, unob)
            print x


            p=np.array([x[0]])
            p1=np.array([x[1]])
            aux=10000000
            aux1=0
            for o in range (len(p)):
                if p[o]<q[0] and p[o]>0 and p[o]<aux:
                    aux=p[o]
                    aux1=p1[o]
            j=(aux*z)+(aux1*z1)
            print aux
            print aux1
            aux3 = 10000000
            aux4=0
            for o in range(len(p1)):
                if p1[o] < q1[0] and p1[o] > 0 and p1[o] < aux3:
                    aux3 = p[o]
                    aux4 = p1[o]
            j1=(aux3*z)+(aux4*z1)
            print aux3
            print aux4
            if j>j1:
                print"optimo: ",j
                print"punto en x: ",aux
                print"punto en y: ",aux1
            elif j<j1:
                print"optimo: ",j1
                print"punto en x: ",aux3
                print"punto en y: ",aux4
            elif j==j1:
                print"optimo: ",j
                print"punto en x: ",aux
                print"punto en y: ",aux1
    def grafica(self, a,a1,b1,b,c,c1,d1,d,e1,f1,e,f):
        #fx = lambda x: 3 * x - 5
        #gx = lambda x: -2 * x + 1
        x = np.linspace(-200, 200, 5)
        y = np.linspace(-200,200, 5)
        if a1!=0 and c1!=0:
            u= (-a1 * x + e1) / c1
            hx = lambda x: u
            cc = hx(x)
            plt.plot(x, cc, color="blue")
        if b1!=0 and d1!=0:
            v = (-b1 * x + f1) / d1
            rx = lambda x: v
            dd = rx(x)
            plt.plot(x, dd, color="yellow")
        e = (-a*x +e)/c
        f = (-b*x + f)/d
        fx = lambda x: e
        gx = lambda x: f
        #hx= lambda x: u
        #rx= lambda x: v
        #x = np.linspace(-5, 5, 5)

        aa = fx(x)
        bb = gx(x)
        #cc= hx(x)
        #dd= rx(x)

        l=[-200,200,-200,200]

        plt.plot(x, aa, color="red")
        plt.plot(x, bb, color="green")
        #plt.plot(x, cc, color="blue")
        #plt.plot(x, dd, color="gray")
        #plt.axvline(30,0,50, label='pyplot vertical line')
        #plt.axhline(30, 0, 50, label='pyplot vertical line')
        plt.grid()
        plt.title('optimizacion')
        plt.xlabel('insumo 1')
        plt.ylabel('insumo 2')
        #plt.text(3,10,'c')
        plt.axis(l)
        plt.show()

t=trabajo()
#t.puntos()
a = int(input("x1: "))
b = int(input("x2: "))
a1 = int(input("x3: "))
b1 = int(input("x4: "))
c = int(input("y1: "))
d = int(input("y2: "))
c1 = int(input("y3: "))
d1 = int(input("y4: "))
e = int(input("constante ecuacion 1: "))
f = int(input("constante ecuacion 2: "))
e1 = int(input("constante ecuacion 3: "))
f1 = int(input("constante ecuacion 4: "))
z = int(input("ganancia x: "))
z1 = int(input("ganancia y: "))
#t.grafica(a,a1,b1,b,c,c1,d1,d,e,f,e1,f1)
t.puntos(a,b,c,d,e,f,a1,b1,c1,d1,e1,f1,z,z1)
t.grafica(a,a1,b1,b,c,c1,d1,d,e1,f1,e,f)