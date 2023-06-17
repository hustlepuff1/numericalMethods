## example5_5 (from ex3_12)
import numpy as np
from polyFit import *
import matplotlib.pyplot as plt

xData = np.array([0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]) # x y 값 넣기
yData = np.array([1.9934, 2.1465, 2.2129, 2.1790, 2.0683, 1.9448, 1.7655, 1.5891])

while True:
    try:
        m = eval(input("\nDegree of polynomial (hit return to quit) ==> "))
        coeff = polyFit(xData,yData,m)
        print("Coefficients are:\n",coeff)
        print("Std. deviation =",stdDev(coeff,xData,yData))
    except SyntaxError: break

    x2=np.arange(0.,1.4,0.01)
    y2=np.zeros(len(x2))

    p=np.zeros(len(coeff))
    for i in range(len(p)):
        p[i]=coeff[len(coeff)-1-i]
    
    
    for i in range(len(x2)):
        y2[i]=np.polyval(p,x2[i])
    plt.plot(xData,yData,'o',x2,y2,'-')
    plt.grid(True)
    plt.show()
