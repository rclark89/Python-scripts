import math
     
    #binomial discriminant formula  
    def disc():
        d = math.pow(x,2)-(4*a*c)
        return d
        # return command
     
    #these are the variables, the program now knows what values to assign to
    #x, a, and c.
    x = 1
    a = -1
    c = -1
     
    print "Binomial discriminant is:"
    print disc()
     
    if disc() > 0:
        print "Roots are real and distinct"
    elif disc() == 0:
        print "Root is real and distinct"
    elif disc() < 0:
        print "No real roots"
 
