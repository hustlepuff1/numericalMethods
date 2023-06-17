## example3_12 차수 m 에 대한 다항식을 데이터 이용해 몇 차 인지 맞추는것
import numpy as np
from polyFit import *
import matplotlib.pyplot as plt

xData = np.array([-0.04,0.93,1.95,2.90,3.83,5.0, \
                                5.98,7.05,8.21,9.08,10.09])
yData = np.array([-8.66,-6.44,-4.36,-3.27,-0.88,0.87, \
                                3.31,4.63,6.19,7.4,8.85])

while True:
    try:
        m = eval(input("\nDegree of polynomial (hit return to quit) ==> "))
        coeff = polyFit(xData,yData,m)
        print("Coefficients are:\n",coeff)
        print("Std. deviation =",stdDev(coeff,xData,yData))
    except SyntaxError: break

    x2=np.arange(-0.04,10.091,0.01)
    y2=np.zeros(len(x2))

    p=np.zeros(len(coeff))
    for i in range(len(p)):
        p[i]=coeff[len(coeff)-1-i]
    
    
    for i in range(len(x2)):
        y2[i]=np.polyval(p,x2[i])
    plt.plot(xData,yData,'o',x2,y2,'-')
    plt.grid(True)
    plt.show()
