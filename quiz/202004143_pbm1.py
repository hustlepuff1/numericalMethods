#202004143_pbm1.py
import numpy as np
import gaussPivot as gp

A=np.array([2,-1,0,0,0,0,-1,1,0,-1,2,-1,-1,2,-1,0],float)
A=A.reshape(4,4)
b=np.array([4,-7,12,-8],float)
x=gp.gaussPivot(A,b)
print(x)
