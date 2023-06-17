# example7_2
import numpy as np
from run_kut4 import *
import matplotlib.pyplot as plt
from printSoln import *


def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -9*y[0]
    return F


x1 = 0.0  # Start of integration
xStop1 = 1.2  # End of integration
y1 = np.array([1.0, 0.0])  # Initial values of {y}
h1 = 0.4  # Step size

print('h = 0.4')
X1, Y1 = integrate(F, x1, y1, xStop1, h1)
printSoln(X1, Y1, 1)


x2 = 0.0  # Start of integration
xStop2 = 1.2  # End of integration
y2 = np.array([1.0, 0.0])  # Initial values of {y}
h2 = 0.2  # Step size

print('h = 0.2')
X2, Y2 = integrate(F, x2, y2, xStop2, h2)
printSoln(X2, Y2, 1)


x3 = 0.0  # Start of integration
xStop3 = 1.2  # End of integration
y3 = np.array([1.0, 0.0])  # Initial values of {y}
h3 = 0.1  # Step size

print('h = 0.1')
X3, Y3 = integrate(F, x3, y3, xStop3, h3)
printSoln(X3, Y3, 1)
