## example2_15 방정식 가우스 사이덜 반복법
import numpy as np
from gaussSeidel import *

def iterEqs(x,omega):
    n = len(x)
    x[0]=1./4.*(12.+x[1]-x[2])
    x[1]=1./4.*(-1.+x[0]+2.*x[2])
    x[2]=1./4.*(5.-x[0]+2.*x[1])
    print(x)
    return x

n = eval(input("Number of equations ==>(3) "))
x = np.zeros(n)
#x = np.ones(n)
x,numIter,omega = gaussSeidel(iterEqs,x)

print("\nNumber of iterations =",numIter)
print("\nRelaxation factor =",omega)
print("\nThe solution is:\n",x)
