from __future__ import division
# from PEP 0236:
# A future_statement is simply a from/import statement using the reserved
# module name __future__:
import math
 
def truedip(a,b):
    # a = apparent bed thickness or structure contour value
    # b = horizontal distance
    a = math.radians(a)
    b = math.radians(b)
    x = a/b
    print x
    y = math.atan(x)
    # trig functions in python are give in radians
    print "True dip is",math.degrees(y)
 
def appdip(a,b):
    # a = true dip
    # b = angle of horizontal deviation from true dip direction
    # tan a = tan true * sin b
    a = math.radians(a)
    b = math.radians(b)
    x = math.tan(a) * math.sin(b)
    print x
    # x = tan(apparent dip)
    y = math.atan(x)
    # y = apparent dip
    print math.degrees(y)
 
def convert():
    print("Input cooling rate in oC/Ma")
    cr = input()
    print ("Cooling rate in K/s")
    i = cr
    float(i)
    j = i/31536000000000
    print (j)
