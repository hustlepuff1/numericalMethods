# pbm2
import numpy as np
from newtonPoly import *

xData = np.array([0, 0.5, 1], float)
yData = np.array([-1, 4, 3], float)
a = coeffts(xData, yData)
y = evalPoly(a, xData, 1.5)
print(a)
print(y)
