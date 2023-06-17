import numpy as np
from newtonRaphson2 import *


def f(x):
    f = np.zeros(len(x))
    f[0] = x[0]**2 - 4*x[0] + x[1]**2.0
    f[1] = x[0]**2 + x[1]**2 - 6*x[1] + 5.0
    return f


x = np.array([1., 1.])
[sol, i_val] = newtonRaphson2(f, x)
# print(newtonRaphson2(f,x))
print("it=", i_val)
print("sol=", sol)
