## example3_2
import numpy as np
from newtonPoly import *
import matplotlib.pyplot as plt

xD=np.array([-2,1,4,-1,3,-4],float)
yD=np.array([-1,2,59,4,24,-53],float)

a=coeffts(xD,yD)
print('a=',a)

x=np.arange(-4.,4.01,0.1)
y=evalPoly(a,xD,x)

plt.plot(xD,yD,'x',x,y,'-')
plt.show()
