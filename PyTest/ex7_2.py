## example7_2 오일러 방법으로 한것
import numpy as np
# from euler import *  # 위 아래 둘 중 하나 선택 가능
from run_kut2 import * # 에러가 오히려 없는 걸지도?
# from run_kut4 import *
import matplotlib.pyplot as plt

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1] - x # 두개 연립된 1차 상미방
    return F

x = 0.0 # Start of integration
xStop = 2.0 # End of integration
y = np.array([0.0, 1.0]) # Initial values of {y}
h = 0.05 # Step size 구간 나누기

X,Y = integrate(F,x,y,xStop,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
for i in range(len(X)):
    print('Y= ', Y[i], 'yExact =', yExact[i], 'Error =', Y[i]-yExact[i])
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()
