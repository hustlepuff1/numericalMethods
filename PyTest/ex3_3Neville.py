## example3_3
import numpy as np
from newtonPoly import *
from neville import *
import matplotlib.pyplot as plt

xD=np.array([4.,3.9,3.8,3.7])
yD=np.array([-0.06604, -0.02724, 0.01282, 0.05383])

y=neville(xD,yD, 3.95)
print('y(3.95)=',y)

x=neville(yD,xD, 0.)
print('x(y=0)=',x)

a=coeffts(xD,yD)
print('a=',a)

x=np.arange(3.7,4.0001,0.01)
y=evalPoly(a,xD,x)

plt.plot(xD,yD,'x',x,y,'-')
plt.show()
