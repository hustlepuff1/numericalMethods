## example7_2
import numpy as np
from run_kut4 import *
import matplotlib.pyplot as plt
from printSoln import *

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -9*y[0]
    return F

x = 0.0 # Start of integration
xStop = 1 # End of integration
y = np.array([1.0, 0.0]) # Initial values of {y}
h = 0.1 # Step size

X,Y = integrate(F,x,y,xStop,h)
printSoln(X,Y,1)
