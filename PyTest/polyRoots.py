## module polyRoots
''' roots = polyRoots(a).
Uses Laguerre’s method to compute all the roots of
a[0] + a[1]*x + a[2]*xˆ2 +...+ a[n]*xˆn = 0.
The roots are returned in the array ’roots’,
''' 
from evalPoly import *
import numpy as np
import cmath
from random import random

def polyRoots(a,tol=1.0e-12):
    def laguerre(a,tol):
        #x = random() # Starting value (random number)
        x=1.0+2.0j
        n = len(a) - 1
        for i in range(300):
            p,dp,ddp = evalPoly(a,x)
            if abs(p) < tol: return x
            g = dp/p
            h = g*g - ddp/p
            f = cmath.sqrt((n - 1)*(n*h - g*g))
            if abs(g + f) > abs(g - f): dx = n/(g + f)
            else: dx = n/(g - f)
            x = x - dx
            if abs(dx) < tol: return x
        print('Too many iterations')
    def deflPoly(a,root): # Deflates a polynomial
        n = len(a)-1
        b = [(0.0 + 0.0j)]*n
        b[n-1] = a[n]
        for i in range(n-2,-1,-1):
            b[i] = a[i+1] + root*b[i+1]
        return b
    # solve roots of polynomial
    n = len(a) - 1
    roots = np.zeros((n),dtype=complex)
    for i in range(n):
        x = laguerre(a,tol)
        if abs(x.imag) < tol: x = x.real
        roots[i] = x
        a = deflPoly(a,x)
    return roots
