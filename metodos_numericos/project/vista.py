from Tkinter import *
from puntofijo import iteraciones
import ttk
class inicio:
    def view(self):
        self.ventana = Tk()
        Label(self.ventana, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.ventana.geometry("370x250")
        self.ventana.config(bg="gray")
        self.ventana.config(relief="sunken")
        self.ventana.title("Unidad 1")
        Label(self.ventana, font=("ROCKWELL", 18), fg='black', text="metodos", bg='gray').place(x=10,y=0)
        self.dat = IntVar()
        #Entry(self.ventana, textvariable=self.dat).place(x=70, y=50)
        #Button(self.ventana, font=("INK FREE", 18), fg='black', text="crear", bg='gray',command=self.ir, relief=FLAT).place(x=70, y=100)
        Button(self.ventana, font=("INK FREE", 18), fg='black', text="punto fijo", bg='gray',command=self.puntofijo, relief=FLAT).place(x=70, y=150)
        self.ventana = mainloop()

    def puntofijo(self):
        self.pf = Tk()
        Label(self.pf, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.pf.geometry("370x250")
        self.pf.config(bg="gray")
        self.pf.config(relief="sunken")
        self.pf.title("metodo del punto fijo")
        Label(self.pf, font=("ROCKWELL", 12), fg='black', text="f(x)", bg='gray').place(x=70, y=25)
        self.dat = IntVar()
        Entry(self.pf, textvariable=self.dat).place(x=70, y=50)
        Label(self.pf, font=("ROCKWELL", 12), fg='black', text="g(x)", bg='gray').place(x=70, y=75)
        self.dat1 = IntVar()
        Entry(self.pf, textvariable=self.dat1).place(x=70, y=100)
        Label(self.pf, font=("ROCKWELL", 12), fg='black', text="tolerancia de error", bg='gray').place(x=70, y=125)
        self.dat2 = IntVar()
        Entry(self.pf, textvariable=self.dat2).place(x=70, y=150)
        Label(self.pf, font=("ROCKWELL", 12), fg='black', text="valor inicial de xi", bg='gray').place(x=70, y=175)
        self.dat3 = IntVar()
        Entry(self.pf, textvariable=self.dat3).place(x=70, y=200)
        Button(self.pf, font=("INK FREE", 18), fg='black', text="crear", bg='gray',command=self.extencionpf, relief=FLAT).place(x=220, y=100)
        #Button(self.pf, font=("INK FREE", 18), fg='black', text="punto fijo", bg='gray', command=self.puntofijo,
          #     relief=FLAT).place(x=70, y=150)

        #options=[
         #  "dgc",
          #"dfgdf"
         #]
        #self.cmb=ttk.Combobox(self.pf,width=21,values=options, state="readonly").place(x=90,y=120)
        self.combo=ttk.Combobox(self.pf)
        self.combo.place(x=200,y=50)
        self.combo['values']=("1","2","3")
        self.combo.current(2)
        self.pf = mainloop()
    def extencionpf(self):
        a=self.dat.get()
        b = self.dat1.get()
        c = self.dat2.get()
        d = self.dat3.get()
        x=0
        print a,b,c,d
        print (self.combo.get())
        iteraciones().itera(a,b,c,d)


i=inicio()
i.view()