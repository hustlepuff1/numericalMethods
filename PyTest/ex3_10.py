# example3_10 데이터 x, y의 선형 회귀 와 표준편차
import numpy as np
from polyFit import *
import matplotlib.pyplot as plt

xData = np.array([1.0, 2.5, 3.5, 1.1, 1.8, 3.7])
yData = np.array([6.0, 15.7, 27.1, 5.3, 9.5, 28.8])
xData = np.array([0, 0.5, 1], float)
yData = np.array([-1, 4, 3], float)

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
