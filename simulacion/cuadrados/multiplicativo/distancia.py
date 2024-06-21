import numpy as n
import random as r
class dis:
    def aleatorios(self,vez):
        datos=[]
        for i in range(vez):
            prob = r.random()
            datos.append(prob)
        return datos
    def saltos(self):
        a=float(input("alfa: "))
        b=float(input("beta: "))
        vez = int(input("datos aleatorios: "))
        datos=d.aleatorios(vez)
        auxarre=n.zeros(len(datos))
        for i in range(len(datos)):
            if a<=datos[i]<=b:
                auxarre[i]=1
        print datos
        print auxarre

        conta=0
        guarda=[]
        for j in range(len(auxarre)-1):
            conta=conta+1
            #auxarre=n.array([1,1,1,1,1])
            if auxarre[j]!=auxarre[j+1]:
                if j==len(auxarre)-2 and auxarre[j]!=auxarre[j+1]:
                    print"aqui"
                    guarda.append(conta)
                    conta=1
                    print"agregar"
                    guarda.append(conta)
                else:
                    guarda.append(conta)
                    conta=0
            elif j == len(auxarre) - 2 and auxarre[j] == auxarre[j + 1]:
                conta = conta + 1
                print"aqui"
                guarda.append(conta)
        #print guarda
        cuanto=[]
        dato=[]
        for k in range(len(guarda)):
            can = 1
            if guarda[k]!=-1:
                for k1 in range(k+1,len(guarda)):
                    if guarda[k]==guarda[k1]:
                        guarda[k1]=-1
                        can=can+1
                dato.append(guarda[k])
                cuanto.append(can)
        #print guarda
        print dato
        print cuanto
        d.tabla(a,b,cuanto)
    def tabla(self,a,b,cuanto):
        nu=len(cuanto)
        te=b-a
        tabla=n.zeros([nu,3])
        print tabla
        cua=0.0
        sum=0
        for r in range(len(cuanto)):
            sum=sum+cuanto[r]
        #cu=n.array([6,2,2])
        cu=cuanto
        for i in range(len(cuanto)):
            if i==len(cuanto)-1:
                val = (((1 - te) ** i))
                tabla[i][0] = val
            else:
                val = (te * ((1 - te) ** i))
                cua = cua + val
                tabla[i][0] = val
        for j in range(len(cuanto)):
            tabla[j][1] = cuanto[j]
        for k in range(len(cuanto)):
            if k==len(cuanto)-1:
                g=sum*((1 - te) ** k)
                tabla[k][2] = g
            else:
                g = sum* (te * (1 - te) ** k)
                tabla[k][2] = g
        estadistico=0.0
#        print tabla[2][2]
        for k in range(0,len(cuanto)):
            estadistico=estadistico+(((tabla[k][1] - tabla[k][2])**2)/tabla[k][2])
            print tabla[k][1]

        print tabla
        print cua
        print estadistico
    def aqui(self):
        a = int(input("rango menor: "))
        b = int(input("rango mayor: "))
        dato = 0
        for i in range(a, b):
            dato = p.prim(i, dato)
            if dato > mayor:
                mayor = dato
            if dato < mayor and dato > menor:
                menor = dato
        print"numero mayor de primos= ", mayor
        print"numero menor de primos= ", menor

d=dis()
#d.aleatorios()
d.saltos()
#d.tabla()


def tablas(self):
    nu = 3
    te = 0.57
    tabla = n.zeros([nu, nu])
    cua = 0.0
    cu = n.array([6, 2, 2])
    for i in range(nu):
        for j in range(nu):
            if j == 0 and i == 2:
                val = ((1 - te) ** i)
                cua = cua + val
                tabla[i][j] = val
            elif j == 0:
                val = (te * (1 - te) ** i)
                cua = cua + val
                tabla[i][j] = val
            elif j == 1:
                tabla[i][j] = cu[i]
            elif j == 2 and i == 2:
                g = 10 * ((1 - te) ** i)
                tabla[i][j] = g
            elif j == 2:
                g = 10 * (te * (1 - te) ** i)
                tabla[i][j] = g
    estadistico = 0.0
    print tabla[2][2]
    for k in range(0, 3):
        estadistico = estadistico + (((tabla[k][1] - tabla[k][2]) ** 2) / tabla[k][2])
        print tabla[k][1]

    print tabla
    print cua
    print estadistico

    for i in range(nu):
        for j in range(nu):
            if j == 0 and i == 2:
                val = ((1 - te) ** i)
                cua = cua + val
                tabla[i][j] = val
            elif j == 0:
                val = (te * (1 - te) ** i)
                cua = cua + val
                tabla[i][j] = val

            elif j == 1:
                tabla[i][j] = cu[i]
            elif j == 2 and i == 2:
                g = 10 * ((1 - te) ** i)
                tabla[i][j] = g
            elif j == 2:
                g = 10 * (te * (1 - te) ** i)
                tabla[i][j] = g