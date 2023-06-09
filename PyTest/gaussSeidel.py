## module gaussSeidel
''' x,numIter,omega = gaussSeidel(iterEqs,x,tol = 1.0e-9)
Gauss-Seidel method for solving [A]{x} = {b}.
The matrix [A] should be sparse. User must supply the
function iterEqs(x,omega) that returns the improved {x},
given the current {x} (’omega’ is the relaxation factor).
'''
import numpy as np
import math
import matplotlib.pyplot as plt
def gaussSeidel(iterEqs,x,tol = 1.0e-9):
    dx_array=np.ones(501)
    i_array=np.arange(0.,501,1.0)
    omega = 1.0
    k = 10
    p = 1
    for i in range(1,501):
        xOld = x.copy()
        x = iterEqs(x,omega)
        dx = math.sqrt(np.dot(x-xOld,x-xOld))
        dx_array[i]=dx;
        if dx < tol:
            #plt.plot(i_array,dx_array,'-')
            plt.plot(i_array[0:i],dx_array[0:i],'o-')
            plt.yscale("log")
            plt.show()
            #input('Press return=>')
            return x,i,omega
        print('i=',i,' dx=',dx)
        # Compute relaxation factor after k+p iterations
        if i == k: dx1 = dx
        if i == k + p:
            dx2 = dx
            omega = 2.0/(1.0+math.sqrt(1.0-(dx2/dx1)**(1.0/p)))
            #omega = 1.0
    plt.plot(i_array,dx_array,'-')
    plt.yscale("log")
    plt.show()
    print('Gauss-Seidel failed to converge')
    
