## example6_7
import math
from romberg import *

def f(x): return 2.0*(x**2)*math.cos(x**2)

I,n = romberg(f,0,math.sqrt(math.pi))
print("Integral =",I)
print("numEvals =",n)
