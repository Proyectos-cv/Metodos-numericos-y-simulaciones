# -*- coding: utf-8 -*-
# #!/usr/bin/env python
from Tkinter import *
import cuadradoautomatico
import multiplicarautomatico
import cuadrados
class Menu_principal:
    def __init__(self):
        self.ventana_menu_principal=Tk()
        self.ventana_menu_principal.geometry("550x550")
        self.ventana_menu_principal.title("Menu principal")
        self.ventana_menu_principal.config(bg="light blue")
#        self.ventana_menu_principal.iconbitmap("icono_proyecto_simulacion.ico")
        self.ventana_menu_principal.config(cursor="hand2")
        self.ventana_menu_principal.config(relief="sunken")
        self.boton_metodo_generar_num_aleatorios= Button(self.ventana_menu_principal, text="Generar numeros seudoaleatorios", font=("Comic Sans MS", 20),relief=SOLID, padx=20,pady=20,bg='grey')
        self.boton_metodo_generar_num_aleatorios.place(x=50,y=100)
        self.boton_metodo_pruebas = Button(self.ventana_menu_principal,text="Prueba numeros aleatorios",font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20,bg='grey')
        self.boton_metodo_pruebas.place(x=50, y=250)
        self.boton_salir = Button(self.ventana_menu_principal, text="Salir",font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.ventana_menu_principal.destroy)
        self.boton_salir.place(x=50, y=390)
        self.ventana_menu_principal.mainloop()


#p=Menu_principal()

# -*- coding: utf-8 -*-
# #!/usr/bin/env python
#from tkinter import *

#class Metodo_cuadrados_medios:
   # def __init__(self):
    def cuadrados(self):
        self.ventana_metodo_cuadrados_medios=Tk()
        self.ventana_metodo_cuadrados_medios.geometry("750x750")
        self.ventana_metodo_cuadrados_medios.title('Metodo multiplicativo')
        self.ventana_metodo_cuadrados_medios.config(bg="light blue")
#        self.ventana_metodo_cuadrados_medios.iconbitmap("icono_proyecto_simulacion.ico")
        self.ventana_metodo_cuadrados_medios.config(cursor="hand2")
        self.ventana_metodo_cuadrados_medios.config(relief="sunken")
        label_titulo = Label(self.ventana_metodo_cuadrados_medios, text="Metodo cuadrados medios ", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_titulo.place(x=250, y=10)

        self.sem=IntVar()
        label_semilla=Label(self.ventana_metodo_cuadrados_medios, text="Semilla", fg="black",font=("Comic Sans MS", 20), bg='white', justify="center")
        label_semilla.place(x=10,y=100)
        self.caja_semilla=Entry(self.ventana_metodo_cuadrados_medios,textvariable=self.sem,font="Arial")
        self.caja_semilla.place(x=110,y=100,width=150, height=35)

        self.cuanto=IntVar()
        label_cantidad = Label(self.ventana_metodo_cuadrados_medios, text="cantidad", fg="black",
                              font=("Comic Sans MS", 20), bg='white', justify="center")
        label_cantidad.place(x=300, y=100)
        self.caja_cantidad = Entry(self.ventana_metodo_cuadrados_medios,textvariable=self.cuanto, font="Arial")
        self.caja_cantidad.place(x=450, y=100, width=150, height=35)

        boton_generar=Button(self.ventana_metodo_cuadrados_medios, text="Generar", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.cuadrado)
        boton_generar.place(x=10,y=400)
        boton_salir = Button(self.ventana_metodo_cuadrados_medios, text="Salir", font=("Comic Sans MS", 20),relief=SOLID, padx=20, pady=20, bg='grey',command=self.ventana_metodo_cuadrados_medios.destroy)
        boton_salir.place(x=200, y=400)
        boton_generar_alea = Button(self.ventana_metodo_cuadrados_medios, text="Generar aleatorio", font=("Comic Sans MS", 20),relief=SOLID, padx=20, pady=20, bg='grey',command=self.automaticocuadrados)
        boton_generar_alea.place(x=350, y=400)
        self.ventana_metodo_cuadrados_medios.mainloop()
    def cuadrado(self):
        lista_retorno = cuadrados.cuadrado().entrada(self.sem.get(),self.cuanto.get())
        print lista_retorno
        print "estoy en la interfaz"

        label_lista_de_numeros_generados = Label(self.ventana_metodo_cuadrados_medios,
                                                 text="Lista de numeros generados", fg="black",
                                                 font=("Comic Sans MS", 20), bg='white', justify="center")
        label_lista_de_numeros_generados.place(x=200, y=150)
        lista_numeros_generados = Listbox(self.ventana_metodo_cuadrados_medios, width=60, height=10)
        for i in range(0, len(lista_retorno)):
            lista_numeros_generados.insert(0, str(lista_retorno[i]))
        lista_numeros_generados.place(x=10, y=210)
    def automaticocuadrados(self):

        lista_retorno=cuadradoautomatico.cuadrado().entrada(self.cuanto.get())
        print lista_retorno
        print "estoy en la interfaz"

        label_lista_de_numeros_generados = Label(self.ventana_metodo_cuadrados_medios,
                                             text="Lista de numeros generados", fg="black",
                                             font=("Comic Sans MS", 20), bg='white', justify="center")
        label_lista_de_numeros_generados.place(x=200, y=150)
        lista_numeros_generados = Listbox(self.ventana_metodo_cuadrados_medios, width=60, height=10)
        for i in range(0,len(lista_retorno)):
            lista_numeros_generados.insert(0,str(lista_retorno[i]))
        lista_numeros_generados.place(x=10, y=210)





#if __name__ == "__main__":
 #   obj=Metodo_cuadrados_medios()

# -*- coding: utf-8 -*-
# #!/usr/bin/env python
#from tkinter import *

#class Metodo_multiplicativo:
    #def __init__(self):
    def multiplicativo(self):
        self.ventana_metodo_multiplicativo=Tk()
        self.ventana_metodo_multiplicativo.geometry("750x750")
        self.ventana_metodo_multiplicativo.title('Metodo multiplicativo')
        self.ventana_metodo_multiplicativo.config(bg="light blue")
      #  self.ventana_metodo_multiplicativo.iconbitmap("icono_proyecto_simulacion.ico")
        self.ventana_metodo_multiplicativo.config(cursor="hand2")
        self.ventana_metodo_multiplicativo.config(relief="sunken")
        label_titulo=Label(self.ventana_metodo_multiplicativo,text="Metodo multiplicativo", fg="black", font=("Comic Sans MS", 20),bg='white', justify="center")
        label_titulo.place(x=250,y=50)
        label_numero=Label(self.ventana_metodo_multiplicativo,text="Semilla", fg="black", font=("Comic Sans MS", 20),bg='white', justify="center")
        label_numero.place(x=10,y=130)
        self.caja_texto_semilla=Entry(self.ventana_metodo_multiplicativo,font="Arial")
        self.caja_texto_semilla.place(x=110,y=135,width=150, height=35)

        #label_conjunto_t=Label(self.ventana_metodo_multiplicativo,text="Conjunto T", fg="black", font=("Comic Sans MS", 20),bg='white', justify="center")
        #label_conjunto_t.place(x=10,y=190)
        ##self.caja_texto_conjunto_t=Entry(self.ventana_metodo_multiplicativo,font="Arial")
        #self.caja_texto_conjunto_t.place(x=155,y=190,width=150, height=35)

        #label_conjunto_v=Label(self.ventana_metodo_multiplicativo,text="Conjunto V", fg="black", font=("Comic Sans MS", 20),bg='white', justify="center")
        #label_conjunto_v.place(x=10,y=250)
        #self.caja_texto_conjunto_v=Entry(self.ventana_metodo_multiplicativo,font="Arial")
        #self.caja_texto_conjunto_v.place(x=155,y=250,width=150, height=35)

        label_cantidad = Label(self.ventana_metodo_multiplicativo, text="cantidad", fg="black",
                               font=("Comic Sans MS", 20), bg='white', justify="center")
        label_cantidad.place(x=300, y=130)
        self.caja_cantidad = Entry(self.ventana_metodo_multiplicativo, font="Arial")
        self.caja_cantidad.place(x=450, y=130, width=150, height=35)

        boton_generar_numeros=Button(self.ventana_metodo_multiplicativo, text="Generar", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey')
        boton_generar_numeros.place(x=10,y=520)
        boton_salir=Button(self.ventana_metodo_multiplicativo, text="Salir", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.ventana_metodo_multiplicativo.destroy)
        boton_salir.place(x=200,y=520)
        boton_num_aleatorio=Button(self.ventana_metodo_multiplicativo, text="Generar numero aleatorio", font=("Comic Sans MS", 20), relief=SOLID, padx=20, pady=20, bg='grey',command=self.automaticomulti)
        boton_num_aleatorio.place(x=350,y=520)
        self.ventana_metodo_multiplicativo.mainloop()
    def automaticomulti(self):
        datos=multiplicarautomatico.multi().mul(int(self.caja_cantidad.get()))
        print datos
        print "estoy en la interfaz"
        label_lista_de_numeros_generados = Label(self.ventana_metodo_multiplicativo, text="Lista de numeros generados",
                                                 fg="black", font=("Comic Sans MS", 20), bg='white', justify="center")
        label_lista_de_numeros_generados.place(x=200, y=300)
        lista_numeros_generados = Listbox(self.ventana_metodo_multiplicativo, width=60, height=10)
        for i in range(0,len(datos)):
            lista_numeros_generados.insert(0, str(datos[i]))
        lista_numeros_generados.place(x=10, y=350)
p = Menu_principal()
#p.cuadrados()
p.multiplicativo()
#if __name__ == "__main__":
 #   obj=Metodo_multiplicativo()