## Runge function
import numpy as np
from newtonPoly import *
import matplotlib.pyplot as plt

def runge_f(x):
    return 1./(1.+25.*x**2)

n=eval(input('Number of data?(from -1. to 1.)'))
xD=np.linspace(-1.,1.,n)
yD=runge_f(xD)

a=coeffts(xD,yD)
print('a=',a)

x=np.arange(-1.,1.001,0.01)
y=evalPoly(a,xD,x)
yexact=runge_f(x)

plt.plot(xD,yD,'x',x,y,'-',x,yexact,':')
plt.show()
