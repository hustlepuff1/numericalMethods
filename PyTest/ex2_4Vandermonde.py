# example2_4
import numpy as np
from gaussElimin import *


def vandermonde(v):
    n = len(v)
    a = np.zeros((n, n))
    for j in range(n):
        a[:, j] = v**(n-j-1)
        # a[:,j]=v**j
    return a


v = np.array([1., 1.2, 1.4, 1.6, 1.8, 2.])
b = np.array([0., 1., 0., 1., 0., 1.])
a = vandermonde(v)
print(a)
input()
aOrig = a.copy()
bOrig = b.copy()
x = gaussElimin(a, b)
det = np.prod(np.diagonal(a))
print('x=', x)
print('det=', det)
print('Check result: [a]x-b=', np.dot(aOrig, x)-bOrig)
input('Print return to exit')
