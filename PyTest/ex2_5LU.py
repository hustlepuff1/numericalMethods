## example2_4 
import numpy as np
from LUdecomp import *

a=np.array([[2.,-1.,0.,0.],[0.,0.,-1.,1.],[0.,-1.,2.,-1],[-1.,2.,-1.,0.]]) # A 행렬
b=np.array([4.,-7.,12.,-8.]) # B 벡터
aOrig=a.copy()
bOrig=b.copy()

LUdecomp(a)
det=np.prod(np.diagonal(a))
x=LUsolve(a,b)
print('x=',x)
print('det=',det)
print('Check result: [a]x-b=',np.dot(aOrig,x)-bOrig)
input('Print return to exit')
