class igualacion:
    def iguala1(self):

        fx=lambda x: 3-x
        gx=lambda x: x
        h=fx - gx
    def iguala4(self):
        x=0
        y=0
        a=1
        b=1
        c=2
        d=1
        e=3
        f=1
        fx=a*x+b*y
        gx=c*x+d*y
        i=-(b/a)+(e/a)
        p=(d*i)/c
#        print i
 #       print p
    def iguala(self,a,b,e,c,d,f):
        a = float(a)
        b = float(b)
        e = float(e)
        c = float(c)
        d = float(d)
        f = float(f)
        #x=1
        #y=1
        #a=1
        #b=2
        #c=3
        #d=5
        #e=3
        #f=4

        #a=1
        #b=1
        #c=2
        #d=1
        #e=3
        #f=1

        pr=((a*f)-(e*c))/((a*d)-(c*b))
        #fx=(b*pr)/a
        gx=(f-d*pr)/c
       #print "y: ",pr
        #print "x: ",gx
        return pr,gx
