## example4_9
import numpy as np
import math
from newtonRaphson2 import *
def f(x):
    f = np.zeros(len(x))
    f[0] = math.sin(x[0]) + x[1]**2 + math.log(x[2]) - 7.0
    f[1] = 3.0*x[0] + 2.0**x[1] - x[2]**3 + 1.0
    f[2] = x[0] + x[1] + x[2] - 5.0
    return f
x = np.array([1.0, 1.0, 1.])
sol,i_val=newtonRaphson2(f,x)
#print(newtonRaphson2(f,x))
print("it=",i_val)
print("sol=",sol)
