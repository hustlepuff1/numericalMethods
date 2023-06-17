## example7_4 런지 쿠타 방법으로 한것
import numpy as np
from printSoln import *
from run_kut4 import *
import matplotlib.pyplot as plt

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -9*y[0]
    return F



x = 0.0 # Start of integration
xStop = 2.0 # End of integration
y = np.array([0.0, 1.0]) # Initial values of {y}
h = 0.2 # Step size
X,Y = integrate(F,x,y,xStop,h)
yExact = np.cos(3*x)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()

