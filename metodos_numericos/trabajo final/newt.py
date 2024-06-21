import numpy as np
from Tkinter import *
class ne:
    def ventana(self):
        self.v = Tk()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("600x800")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="AX**2 + BY**2 - c", bg='gray').place(x=10,
                                                                                                   y=0)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="(d/9)x**2 + eY**2 - f", bg='gray').place(x=10,
                                                                                                   y=50)

        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor A", bg='gray').place(x=400, y=25)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor B", bg='gray').place(x=400, y=75)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor C", bg='gray').place(x=400, y=125)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor D", bg='gray').place(x=400, y=175)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor E", bg='gray').place(x=400, y=225)
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="valor F", bg='gray').place(x=400, y=275)



        self.u = DoubleVar()
        self.c = Entry(self.v, textvariable=self.u).place(x=400, y=50)
        self.u1 = DoubleVar()
        self.c1 = Entry(self.v, textvariable=self.u1).place(x=400, y=100)
        self.u2 = DoubleVar()
        self.c2 = Entry(self.v, textvariable=self.u2).place(x=400, y=150)
        self.u3 = DoubleVar()
        self.c3 = Entry(self.v, textvariable=self.u3).place(x=400, y=200)
        self.u4 = DoubleVar()
        self.c4 = Entry(self.v, textvariable=self.u4).place(x=400, y=250)
        self.u5 = DoubleVar()
        self.c5 = Entry(self.v, textvariable=self.u5).place(x=400, y=300)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.proceso1, relief=FLAT).place(x=70, y=200)
        self.v = mainloop()
    def proceso(self):
        n=100
        a=self.u.get()
        b=self.u1.get()
        c=self.u2.get()
        d=self.u3.get()
        e=self.u4.get()
        f=self.u5.get()
        print a,b,c,d,e,f
        x=np.array([1,1])

        f1=lambda x: a*x[0]**2 + b*x[1]**2 - c
        f2=lambda x: (d/9)*(x[0]**2) + e*(x[1]**2) - f
        df=lambda x:([[2*x[0],2*x[1]],[8*x[0]/9,8*x[1]]])


        for k in range (n):

            xold=x
            jinv=np.linalg.inv(df(x))
            #x=x-np.dot(jinv,f(x))
            x = x - np.dot(jinv, np.array([f1(x),f2(x)]))
            #x=np.linalg.solve(df(x),df(x)* x - fx(x))
            e=np.linalg.norm(x-xold)
            print (k,x,e)
            #print x[0], x[1]
            if e<1e-10:
                break
    def proceso1(self):
        n=100
        x=np.array([1,1])

        f1=lambda x: x[0]**2 + x[1]**2 - 1
        f2=lambda x: 4*x[0]**2/9 + 4*x[1]**2 - 1
        df=lambda x:([[2*x[0],2*x[1]],[8*x[0]/9,8*x[1]]])

        self.vl = Tk()
        self.vl.geometry("600x800")
        listbox = Listbox(self.vl, width=100, height=50)
        for k in range (n):

            xold=x
            jinv=np.linalg.inv(df(x))
            #x=x-np.dot(jinv,f(x))
            x = x - np.dot(jinv, np.array([f1(x),f2(x)]))
            #x=np.linalg.solve(df(x),df(x)* x - fx(x))
            e=np.linalg.norm(x-xold)
            #print (k,x,e)
            ll= "x= ",x[0],"y= ", x[1]
            listbox.insert(0, ll)
            if e<1e-10:
                break
        listbox.place(x=250, y=0)
        self.vl = mainloop()


n=ne()
n.ventana()