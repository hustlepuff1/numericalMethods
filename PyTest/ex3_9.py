# example3_9
import numpy as np
from cubicSpline import *
import matplotlib.pyplot as plt
xData = np.array([1, 2, 3, 4, 5], float)
yData = np.array([0, 1, 0, 1, 0], float)
k = curvatures(xData, yData)
# print(k)
while True:
    try:
        x = eval(input("\nx (hit return to quit)==> "))
    except SyntaxError:
        break
    print("y =", evalSpline(xData, yData, k, x))


x2 = np.arange(1., 5.001, 0.01)
y2 = np.zeros(len(x2))
for i in range(len(x2)):
    y2[i] = evalSpline(xData, yData, k, x2[i])
plt.plot(xData, yData, 'o', x2, y2, '-')
plt.grid(True)
plt.show()
