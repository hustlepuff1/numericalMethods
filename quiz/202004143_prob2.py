## prob2

from newtonRaphson2 import*
from numpy import *

def f(x):
    f=zeros(len(x))
    f[0]=(x[0]-2)**2+x[1]**2-4
    f[1]=x[0]**2 + (x[1]-3)**2-4
    return f

x=array([1.0, 1.0])
roots=newtonRaphson2(f,x)
print(roots)
