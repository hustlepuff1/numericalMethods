# example3_10
import numpy as np
from polyFit import *
import matplotlib.pyplot as plt

xData = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
yData = np.array([2.9, 3.7, 4.1, 4.4, 5.0])

while True:
    try:
        m = eval(input("\nDegree of polynomial (0 to stop) ==> "))
        if m == 0:
            break
        coeff = polyFit(xData, yData, m)
        print("Coefficients are:\n", coeff)
        print("Std. deviation =", stdDev(coeff, xData, yData))
    except SyntaxError:
        break

    x2 = np.arange(0., 3.001, 0.01)
    y2 = np.zeros(len(x2))

    p = np.zeros(len(coeff))
    for i in range(len(p)):
        p[i] = coeff[len(coeff)-1-i]

    for i in range(len(x2)):
        y2[i] = np.polyval(p, x2[i])
    plt.plot(xData, yData, 'o', x2, y2, '-')
    plt.grid(True)
    plt.show()
