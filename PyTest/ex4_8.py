## example4_8
import numpy as np
import math
from newtonRaphson2 import *
def f(x):
    f = np.zeros(len(x))
    f[0] = x[0]**2 + x[1]**2 - 3.0
    f[1] = x[0] * x[1] - 1.0
    return f
x = np.array([0.5, 1.5])
[sol,i_val]=newtonRaphson2(f,x)
#print(newtonRaphson2(f,x))
print("it=",i_val)
print("sol=",sol)
