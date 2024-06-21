
class red:
    def proceso1(self,a,b,e,c,d,f):
        x=0
        y=0
        a=1
        b=1
        c=2
        d=1
        e=3
        f=0
        var =  a*x + b*y + e
        var2 = c*x - d*y + f

        h=a+c
        var=(a*x + b*y + e)/h

        var2= c*var - d*y + f
        print var
        print var2


        #var3= var - y
        #var2=2*var3-y
        #print var3
        #print var2
    def proceso(self,a,b,e,c,d,f):
        a = float(a)
        b = float(b)
        e = float(e)
        c = float(c)
        d = float(d)
        f = float(f)
        #a = 1
        #b = 1
        #c = 2
        #d = 1
        #e = 3
        #f = 1

        #a = 1
        #b = 2
        #c = 3
        #d = 5
        #e = 3
        #f = 4
        pr = ((a * f) - (c * e)) / ((a * d) - (c * b))
        # fx=(b*pr)/a
        gx = (f - d * pr) / c
        print "y: ", pr
        print "x: ", gx
        return pr, gx

        #if (a>0 and c>0) or (a<0 and c<0):
         #   pr = ((a*f)-(c*e))/((a*d)-(c*b))
          #  # fx=(b*pr)/a
           # gx = (f - d * pr) / c
            #print "y: ", pr
           # print "x: ", gx
            #return pr,gx
        #elif (a<0 and c>0) or (a>0 and c<0) and abs(a)!=abs(c):
         #   pr = ((a*f)+(c*e))/((a*d)+(c*b))
          #  # fx=(b*pr)/a
           # gx = (f - d * pr) / c
           # print "y: ", pr
            #print "x: ", gx
            #return pr, gx
       # elif (a==c):
        #    pr = (e+f)/(d+b)
            # fx=(b*pr)/a
         #   gx = (f - d * pr) / c
          #  print "y: ", pr
           # print "x: ", gx
            #return pr, gx