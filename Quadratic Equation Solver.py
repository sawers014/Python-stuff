
from cmath import sqrt
from hashlib import shake_128
import math
from fractions import Fraction as frac
def deltaPos(a, b, delta):
    d=2*a
    if delta == 0: #only one solution
        
        print("solution is: " + frac(-b, d) )
    else: # 2 solutions
        root=math.sqrt(delta)
        if int(root + 0.5) ** 2 == delta: #perfect square

            print("solution one is: " + str(  frac(int(-b+root), d) ) )
            print("solution two is: " + str(  frac(int(-b-root), d) ))
        else: #rational square

            print("solution one is: " + str(-b) + "+sqrt" + str(delta) + "/" + str(d))
            print("solution two is: " + str(-b) + "-sqrt"+str(delta) + "/" + str(d))
            
equation= str(input("enter the equation "))
eq = [] ## TODO optimize again this shit
eq = equation.split( "x^2")
final =  eq[1].split("x")
final.insert(0, eq[0])
a = final[0]
b=final[1]
c=int(final[2])
try: a=int(final[0]) # TODO optimize this shit
except:
    print()
if a == "" : 
    a=1
if a == "-":
    a=-1    
try: b=int(final[1]) # TODO optimize this shit
except:
    print()
if b == "+" : 
    b=1
if b == "-":
    b=-1    
delta=(b*b) -4*a*c        
if delta<0:
    print("No solution, parabola doesn't touch the X axis")
else: 
    deltaPos(a, b, delta)

