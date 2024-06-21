import numpy as np
from Tkinter import *
class Metodo_newton_rapson:
    def __init__(self):
        self.ventana_metodo_newton = Tk()
        self.ventana_metodo_newton.geometry("850x850")
        self.ventana_metodo_newton.title('Metodo multiplicativo')
        self.ventana_metodo_newton.config(bg="light blue")
     #   self.ventana_metodo_newton.iconbitmap("icono_proyecto_simulacion.ico")
        self.ventana_metodo_newton.config(cursor="hand2")
        self.ventana_metodo_newton.config(relief="sunken")
        label_titulo = Label(self.ventana_metodo_newton, text="Metodo Newton-Raphson ",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_titulo.place(x=130, y=10)
        label_valor_de_x=Label(self.ventana_metodo_newton, text="Valor de x",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_valor_de_x.place(x=10,y=60)
        self.caja_texto_valor_x=Entry(self.ventana_metodo_newton, font="Arial")
        self.caja_texto_valor_x.place(x=154,y=60,width=150, height=35)
        label_elevacion_de_x=Label(self.ventana_metodo_newton, text="Numero elevado de x",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_elevacion_de_x.place(x=330,y=60)
        self.caja_texto_elevacion_de_x=Entry(self.ventana_metodo_newton, font="Arial")
        self.caja_texto_elevacion_de_x.place(x=605,y=60,width=150, height=35)
        label_valor_de_c_1=Label(self.ventana_metodo_newton, text="Valor de C1",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_valor_de_c_1.place(x=10,y=110)
        self.valor_de_c1=Entry(self.ventana_metodo_newton, font="Arial")
        self.valor_de_c1.place(x=160,y=110,width=150, height=35)
        label_valor_de_y=Label(self.ventana_metodo_newton, text="Valor de Y",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_valor_de_y.place(x=10,y=160)
        self.valor_de_Y=Entry(self.ventana_metodo_newton,font="Arial")
        self.valor_de_Y.place(x=169,y=160,width=150, height=35)
        label_valor_de_elevacion_de_y=Label(self.ventana_metodo_newton, text="Numero elevado de Y",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_valor_de_elevacion_de_y.place(x=330,y=160)
        self.caja_texto_elevacion_de_y = Entry(self.ventana_metodo_newton, font="Arial")
        self.caja_texto_elevacion_de_y.place(x=620, y=160, width=150, height=35)
        label_valode_de_x2=Label(self.ventana_metodo_newton, text="Numero de X2",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_valode_de_x2.place(x=10,y=240)
        self.valor_de_x2=Entry(self.ventana_metodo_newton,font="Arial")
        self.valor_de_x2.place(x=200,y=240,width=150, height=35)
        label_elevacion_de_x2=Label(self.ventana_metodo_newton, text="Numero elevado de X2",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_elevacion_de_x2.place(x=355,y=240)
        self.caja_elevacion_de_x2=Entry(self.ventana_metodo_newton,font="Arial")
        self.caja_elevacion_de_x2.place(x=650, y=240, width=150, height=35)
        label_valor_de_Y2=Label(self.ventana_metodo_newton, text="Numero de Y2",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_valor_de_Y2.place(x=10,y=300)
        self.caja_de_valor_de_y2=Entry(self.ventana_metodo_newton,font="Arial")
        self.caja_de_valor_de_y2.place(x=200,y=300,width=150, height=35)
        label_elevado_de_y2=Label(self.ventana_metodo_newton, text="Numero de elevado  Y2",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_elevado_de_y2.place(x=360,y=300)
        self.caja_de_elevacion_de_y2=Entry(self.ventana_metodo_newton,font="Arial")
        self.caja_de_elevacion_de_y2.place(x=655, y=300, width=150, height=35)
        label_valor_de_c_2=Label(self.ventana_metodo_newton, text="Valor de C2",fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_valor_de_c_2.place(x=10,y=358)
        self.caja_de_valor_c_2=Entry(self.ventana_metodo_newton,font="Arial")
        self.caja_de_valor_c_2.place(x=165,y=358,width=150, height=35)
        #Aqui van los botones
        boton_calcular=Button(self.ventana_metodo_newton, text="Generar ", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.muestra_resultado)
        boton_calcular.place(x=10,y=450)
        self.ventana_metodo_newton.mainloop()

    def F(self,x):
        elevacio_x1=int(self.caja_texto_elevacion_de_x.get())
        elevacio_de_y1=int(self.caja_texto_elevacion_de_y.get())
        c_1=int(self.valor_de_c1.get())
        elevacio_de_x2=int(self.caja_elevacion_de_x2.get())
        elevacion_de_y2=int(self.caja_de_elevacion_de_y2.get())
        c_2=int(self.caja_de_valor_c_2.get())
        f1 = x[0] ** elevacio_x1 + x[1] ** elevacio_de_y1 - c_1
        f2 = 4 * x[0] ** elevacio_de_x2 / 9 + 4 * x[1] ** elevacion_de_y2 - c_2
        return np.array([f1, f2])

    def dF(self,x):
        return np.array([[2 * x[0], 2 * x[1]],
                         [8 * x[0] / 9, 8 * x[1]]])

    def muestra_resultado(self):
        N= 100
        x = np.array([1, 1])

        for k in range(N):
            xold = x
            Jinv = np.linalg.inv(self.dF(x))
            x = x - np.dot(Jinv, self.F(x))
            e = np.linalg.norm(x - xold)
            print(k, x, e)
            if e < 1e-10:
                break


if __name__ == "__main__":
    obj=Metodo_newton_rapson()


