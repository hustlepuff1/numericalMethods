## example5_4(2) (from ex3_9)
import numpy as np
from cubicSpline import *
#xData = np.array([1,2,3,4,5],float)
#yData = np.array([0,1,0,1,0],float)
xData = np.array([1.5, 1.9, 2.1, 2.4, 2.6, 3.1])
yData = np.array([1.0628, 1.3961, 1.5432, 1.7349, 1.8423, 2.0397])
k = curvatures(xData,yData)
print(k)
while True:
    try: x = eval(input("\nx (hit return to quit)==> "))
    except SyntaxError: break
    print("y =",evalSpline(xData,yData,k,x))
    

import matplotlib.pyplot as plt
x2=np.arange(1.,5.001,0.01)
y2=np.zeros(len(x2))
for i in range(len(x2)):
    y2[i]=evalSpline(xData,yData,k,x2[i])
plt.plot(xData,yData,'o',x2,y2,'-')
plt.grid(True)
plt.show()
