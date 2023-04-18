## example2_4
import numpy as np
from LUdecomp import *

a=np.array([[1.,4.,1.],[1.,6.,-1.],[2.,-1.,2.]])
b=np.array([7.,13.,5.])
aOrig=a.copy()
bOrig=b.copy()

LUdecomp(a)
det=np.prod(np.diagonal(a))
x=LUsolve(a,b)
print('x=',x)
print('det=',det)
print('Check result: [a]x-b=',np.dot(aOrig,x)-bOrig)
input('Print return to exit')
