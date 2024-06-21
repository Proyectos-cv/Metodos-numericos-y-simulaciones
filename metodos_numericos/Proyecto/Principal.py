# -*- coding: utf-8 -*-
#!/usr/bin/env python

from tkinter import *
#import cv2
import sys
from U2 import MenuUnidad2
from U3 import MenuUnidad3
from U4 import MenuUnidad4
from U5 import MenuUnidad5
from U6 import MenuUnidad6

class MenuUnidad:
    def __init__(self):
        self.venUser = Tk()
        self.venUser.geometry("400x200")
        self.venUser.config(bg="#ffffff")
        self.venUser.config(cursor="cross")
        self.venUser.config(relief="sunken")
        self.venUser.title("Menu de Unidades")
        ancho_ventana = 1200
        alto_ventana = 800
        x_ventana = self.venUser.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.venUser.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.venUser.geometry(posicion)
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial"),width=1000,height=4)
        lblEti.place(x=0, y=(0))
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial", 15), width=1000,height=2)
        lblEti.place(x=0, y=(750))
        lblEti = Label(self.venUser, text="Menu de Unidades", fg="navy", bg="SkyBlue2", font=("Arial", 36))
        lblEti.place(x=400, y=(0))
        lblEti = Label(self.venUser, text="Escoge la unidad que quieras ver", fg="navy", bg="SkyBlue2", font=("Arial", 12))
        lblEti.place(x=67, y=(30))
        #IMU2=PhotoImage(file="C:\D2.png")
        #IMU3 = PhotoImage(file="C:\D3.png")
        #IMU4 = PhotoImage(file="C:\D4.png")
        btn1U= Button(self.venUser,text="Unidad 2", bg='cyan',width=19,height=20, command=self.U1)  # agregando botones con color
        btn1U.place(x=190, y=(200))
        btn2U = Button(self.venUser,text="Unidad 4",bg='ivory3',width=19,height=20, command=self.U2)  # agregando botones con color
        btn2U.place(x=600, y=(200))
        btn3U = Button(self.venUser,text="Unidad 3",bg='cyan',width=19,height=20, command=self.U3)  # agregando botones con color
        btn3U.place(x=400, y=(200))
        btn4U = Button(self.venUser, text="Unidad 5", bg='light sky blue',width=19,height=20, command=self.U5)  # agregando botones con color
        btn4U.place(x=800, y=(200))
        #btn5U = Button(self.venUser, text="Unidad 6", bg='azure',width=8,
        #               command=self.U5)  # agregando botones con color
        #btn5U.place(x=120, y=(120))
        btn6U = Button(self.venUser, text="Unidad 6", bg='light cyan', width=19,height=20,
                       command=self.U6)  # agregando botones con color
        btn6U.place(x=1000, y=(200))
        #btnSalir = Button(self.venUser, text="Salir", bg='grey', command=self.pafuera)
        #btnSalir.place(x=175, y=150)
        self.venUser.mainloop()


    def pafuera(self):
        sys.exit(1)
    def U1(self):
        #self.venUser.withdraw()
        dos = MenuUnidad2()
    def U2(self):
        Cuatro = MenuUnidad4()
    def U3(self):
        tres=MenuUnidad3()
    #def U4(self):
    #    cuatro=Menu4()
    def U5(self):
        cinco=MenuUnidad5()
    def U6(self):
        seis=MenuUnidad6()

pantalla=MenuUnidad()