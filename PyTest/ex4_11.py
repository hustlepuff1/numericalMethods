## example4_11 라그랑주 반복 공식으로 해 찾기
from polyRoots import *
import numpy as np
from evalPoly import *

c = np.array([26.0,-4.48,-4.0,1.0]) # 뒤에서 함수 계수 쓰기

import matplotlib.pyplot as plt
xD=np.arange(-5.,5.001,0.01)
yD=np.zeros(len(xD))
for i in range(len(xD)):
    yD[i],dp,ddp=evalPoly(c,xD[i])
plt.plot(xD,yD.real,'-')
plt.grid(True)
plt.show()

#xexact=3.2-0.8j
#p,dp,ddp=evalPoly(c,xexact)
#print('xexact=',xexact,' f(x)=',p)
x=polyRoots(c)
print('Roots are:\n',x)
for i in range(len(x)):
    p,dp,ddp=evalPoly(c,x[i])
    print('x=',x[i],' f(x)=',p)
