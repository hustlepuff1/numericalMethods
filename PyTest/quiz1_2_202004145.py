# example4_2
from bisection import *
import numpy as np


def f(x): return np.sin(x)+3*np.cos(x)-2


x = bisection(f, -2, 2, tol=1.0e-4)
print('x =', '{:6.4f}'.format(x))
