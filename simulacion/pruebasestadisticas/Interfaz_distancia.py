from Tkinter import *
import numpy as n
import random as r
#from tkinter import messagebox
class Metodo_Distancia:
    def __init__(self):
        self.ventana_metodo_distancia = Tk()
        self.ventana_metodo_distancia.geometry("900x900")
        self.ventana_metodo_distancia.title('Metodo multiplicativo')
        self.ventana_metodo_distancia.config(bg="light blue")
#        self.ventana_metodo_distancia.iconbitmap("icono_proyecto_simulacion.ico")
        self.ventana_metodo_distancia.config(cursor="hand2")
        self.ventana_metodo_distancia.config(relief="sunken")
        label_titulo = Label(self.ventana_metodo_distancia, text="Metodo Distancia ",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_titulo.place(x=250, y=10)
        label_numero_alea = Label(self.ventana_metodo_distancia, text=" ALPHA  ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_numero_alea.place(x=10, y=90)
        self.cantida_de_alpha = Entry(self.ventana_metodo_distancia, font="Arial")
        self.cantida_de_alpha.place(x=150, y=90, width=150, height=35)
        label_numero_alea = Label(self.ventana_metodo_distancia, text=" BETA  ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_numero_alea.place(x=10, y=150)
        self.cantida_de_beta = Entry(self.ventana_metodo_distancia, font="Arial")
        self.cantida_de_beta.place(x=150, y=150, width=150, height=35)
        label_altearios=Label(self.ventana_metodo_distancia, text=" CANTIDAD ALEATORIOS  ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_altearios.place(x=10,y=240)
        self.caja_aletarios=Entry(self.ventana_metodo_distancia,font="Arial")
        self.caja_aletarios.place(x=400,y=240, width=150, height=35)
        label_altearios = Label(self.ventana_metodo_distancia, text=" Resultado Tabla  ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_altearios.place(x=10, y=290)
        self.caja_tabla = Entry(self.ventana_metodo_distancia, font="Arial")
        self.caja_tabla.place(x=400, y=290, width=150, height=35)
        label_altearios = Label(self.ventana_metodo_distancia, text=" ESTADISTICO ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_altearios.place(x=10, y=350)
        self.caja_estadistico = Entry(self.ventana_metodo_distancia, font="Arial")
        self.caja_estadistico.place(x=400, y=350, width=150, height=35)
        boton_generar=Button(self.ventana_metodo_distancia, text="Generar ", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.princial_distancia)
        boton_generar.place(x=10,y=510)
        boton_salir=Button(self.ventana_metodo_distancia, text="Salir", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.ventana_metodo_distancia.destroy)
        boton_salir.place(x=210,y=510)
        self.ventana_metodo_distancia.mainloop()

    def princial_distancia(self):
        a=float(self.cantida_de_alpha.get())
        b=float(self.cantida_de_beta.get())
        vez=int(self.caja_aletarios.get())
        cuanto=[]
        self.aleatorios(vez)
        self.saltos(a,b,vez)
        #self.tabla(a,b,cuanto)

    def aleatorios(self, vez):
        print("Estoy en la funcion aleatorios")
        datos = []
        for i in range(vez):
            prob = r.random()
            datos.append(prob)
        return datos

    def saltos(self,a,b,vez):
        print("Estoy en la funcion Saltos")
        #a = float(input("alfa: "))
        #b = float(input("beta: "))
        #vez = int(input("datos aleatorios: "))
        datos = self.aleatorios(vez)
        auxarre = n.zeros(len(datos))
        for i in range(len(datos)):
            if a <= datos[i] <= b:
                auxarre[i] = 1
        print(datos)
        print(auxarre)

        conta = 0
        guarda = []
        for j in range(len(auxarre) - 1):
            conta = conta + 1
            # auxarre=n.array([1,1,1,1,1])
            if auxarre[j] != auxarre[j + 1]:
                if j == len(auxarre) - 2 and auxarre[j] != auxarre[j + 1]:
                    print("aqui")
                    guarda.append(conta)
                    conta = 1
                    print("agregar")
                    guarda.append(conta)
                else:
                    guarda.append(conta)
                    conta = 0
            elif j == len(auxarre) - 2 and auxarre[j] == auxarre[j + 1]:
                conta = conta + 1
                print("aqui")
                guarda.append(conta)
        # print guarda
        cuanto = []
        dato = []
        for k in range(len(guarda)):
            can = 1
            if guarda[k] != -1:
                for k1 in range(k + 1, len(guarda)):
                    if guarda[k] == guarda[k1]:
                        guarda[k1] = -1
                        can = can + 1
                dato.append(guarda[k])
                cuanto.append(can)
        # print guarda
        print(dato)
        print(cuanto)
        self.tabla(a, b, cuanto)

    def tabla(self, a, b, cuanto):
        print("Estoy en la funcion Tabla")
        nu = len(cuanto)
        te = b - a
        tabla = n.zeros([nu, 3])
        print(tabla)
        cua = 0.0
        sum = 0
        for r in range(len(cuanto)):
            sum = sum + cuanto[r]
        # cu=n.array([6,2,2])
        cu = cuanto
        for i in range(len(cuanto)):
            if i == len(cuanto) - 1:
                val = (((1 - te) ** i))
                tabla[i][0] = val
            else:
                val = (te * ((1 - te) ** i))
                cua = cua + val
                tabla[i][0] = val
        for j in range(len(cuanto)):
            tabla[j][1] = cuanto[j]
        for k in range(len(cuanto)):
            if k == len(cuanto) - 1:
                g = sum * ((1 - te) ** k)
                tabla[k][2] = g
            else:
                g = sum * (te * (1 - te) ** k)
                tabla[k][2] = g
        estadistico = 0.0
        #        print tabla[2][2]
        for k in range(0, len(cuanto)):
            estadistico = estadistico + (((tabla[k][1] - tabla[k][2]) ** 2) / tabla[k][2])
            print(tabla[k][1])

        print(tabla)
        print(cua)
        self.caja_tabla.insert(0,cua)
        print(estadistico)
        self.caja_estadistico.insert(0,estadistico)

    def aqui(self):
        print("Estoy en la funcion aqui")
        a = int(input("rango menor: "))
        b = int(input("rango mayor: "))
        dato = 0
        for i in range(a, b):
            dato = self.prim(i, dato)
            if dato > mayor:
                mayor = dato
            if dato < mayor and dato > menor:
                menor = dato
        print("numero mayor de primos= ", mayor)
        print("numero menor de primos= ", menor)


c=Metodo_Distancia()