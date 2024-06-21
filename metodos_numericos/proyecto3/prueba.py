from sympy import *
from tkinter import *
from tkinter import messagebox
class ne:
    def ventana1(self):
        self.v = Tk()
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="Unidad 1", bg='gray').place(x=10, y=0)
        self.v.geometry("600x800")
        self.v.config(bg="gray")
        self.v.config(relief="sunken")
        Label(self.v, font=("ROCKWELL", 18), fg='black', text="AX**2 + BY**2 - c", bg='gray').place(x=10,
                                                                                                   y=0)
        self.s = StringVar()
        self.c = Entry(self.v, textvariable=self.s).place(x=400, y=50)
        Button(self.v, font=("INK FREE", 18), fg='black', text="crear", bg='gray',
               command=self.proceso1, relief=FLAT).place(x=70, y=200)
        self.v = mainloop()
    def proceso1(self):
        x, y = symbols("x y")
        expr = self.s.get()
        print (diff(expr,x))
    def ventana2(self):
        x, a, b, c, d, e = symbols("x a b c d e")
        y=Function("y")
        init_printing()
        #ed=Eq(y(x).diff()+3*x**2*y(x),6*x**2)
        ed = Eq(y(x).diff(x,2)-4*y(x).diff()+4*y(x),6*exp(2*x)+x)
        print (dsolve(ed,y(x)))
        print (diff((a*x**2*exp(2*x)+b*x+c), x))
        print (diff(2*a*x**2*exp(2*x) + 2*a*x*exp(2*x) + b, x))

        f=4*a*x**2*exp(2*x) + 8*a*x*exp(2*x) + 2*a*exp(2*x)-4*2*a*x**2*exp(2*x) + 2*a*x*exp(2*x) + b+4*(a*x**2*exp(2*x)+b*x+c)
        print(f)
    def ventana(self):
        a=1
        messagebox.showinfo("aqui","resultados: "+str(a) +'\n'+"otro")

        #print (diff(a*x**2 + b*x + c - (d*x*exp(x)) - (e*exp(x)),x))
        #print (diff(2*a*x + b - d*x*exp(x) - d*exp(x) - e*exp(x),x))
        #f=2*a - d*x*exp(x) - 2*d*exp(x) - e*exp(x)-(8*(2*a*x + b - d*x*exp(x) - d*exp(x) - e*exp(x)))+(20*(a*x**2 + b*x + c - (d*x*exp(x)) - (e*exp(x))))
        #print(f)
        #print (diff(expr,x))
        #https://www.youtube.com/watch?v=TJ6h1WYplV8


n=ne()
n.ventana()
#x,y=symbols("x y")

#expre=x-y
#expre=sin(x)**2
#expre = (x**4+3*x**3+2*x+1)/((x+1)*(x+3)**2)
#expre=(x+y)**2
#expr=expand(expre)
#expr=apart(expre)
#expre=Eq(x**2,9)
#expr=solveset(expre)
#print (expre)
#print(expr)


#yacklyon base de datos

#matriz

#m1=Matrix([[1,2],[3,10]])
#m2=Matrix([[3,4],[5,6]])
#m1=Matrix([[x,x**y],[3,10]])
#m2=Matrix([[3,4],[5,6]])
#mul=m1*m2

#print(m1)
#print (m2)
#print (mul)

#evaluar

#expr=sin(x)
#expr=(input("cadena: "))
#expr=eval(expr)
#print(expr.evalf(subs={x:pi/2}))
#print(expr.evalf(subs={x:0}))


##derivadas
#expr=(input("cadena: "))
#evaluacion=int(input("evaluacion: "))
#print (diff(expr,x))
#derivada = (diff(expr,x))
#print (derivada.evalf(subs={x:evaluacion}))

##integrales
#expr=(input("cadena: "))
#evaluacion=int(input("evaluacion: "))
#print (integrate(expr,(x,0,oo)))
#integral = (integrate(expr,(x,0,oo)))
#print (integral.evalf(subs={x:evaluacion}))
