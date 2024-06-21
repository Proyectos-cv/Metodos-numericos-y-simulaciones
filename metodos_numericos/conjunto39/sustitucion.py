class susti:
    def proceso1(self):
        x = 0
        y = 0
        a=1
        b = 1
        c = 2
        d = 1
        e = 3
        f = 1
        #var = (e-b*y)/a
        #var2 = 2 * ((e-b*y)/a) - y

        var3=c*e
        var4=c*b+1
        #print var3,var4
        var1=(var3)/var4
        #print var1
        var= var1/c
        #print var
        #print var1
    def proceso(self,a,b,e,c,d,f):
        a=float(a)
        b=float(b)
        e=float(e)
        c=float(c)
        d=float(d)
        f=float(f)
        #a=float(-2.0)
        #aa=-2
        #print type(a)
        #print type(aa)
        #a = 1
        #b = 1
        #c = 2
        #d = 1
        #e = 3
        #f = 4
        #a=1
        #b=2
        #c=3
        #d=5
        #e=3
        #f=4
        pr = ((f) - ((e * c)/a)) / ((d) - (((b*c)/a)))
        o=float((e * c)/a)
        #print o
        #pr=(f-((d*e)/b))/(c-(a*d/b))
        # fx=(b*pr)/a
        gx = (f - d * pr) / c
        #gx=(f-d*pr)/d
        #print "y: ", pr
        #print "x: ", gx
        return pr,gx
#s=susti()
#s.procesos()