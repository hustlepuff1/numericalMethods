## example5_4 (from ex3_12)
import numpy as np
from polyFit import *
import matplotlib.pyplot as plt

xData = np.array([1.9, 2.1, 2.4])
yData = np.array([1.3961, 1.5432, 1.7349])

while True:
    try:
        m = eval(input("\nDegree of polynomial (hit return to quit) ==> "))
        coeff = polyFit(xData,yData,m)
        print("Coefficients are:\n",coeff)
        print("Std. deviation =",stdDev(coeff,xData,yData))
    except SyntaxError: break

    x2=np.arange(1.5,3.1,0.01)
    y2=np.zeros(len(x2))

    p=np.zeros(len(coeff))
    for i in range(len(p)):
        p[i]=coeff[len(coeff)-1-i]
    
    
    for i in range(len(x2)):
        y2[i]=np.polyval(p,x2[i])
    plt.plot(xData,yData,'o',x2,y2,'-')
    plt.grid(True)
    plt.show()
