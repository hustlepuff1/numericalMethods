## module gaussElimin
import numpy as np
'''
    x = gaussElimin(a,b)
    solves [a] b = x by Gauss Elimination
'''
def gaussElimin(a,b): # textbook code
    n = len(b) # length of vector
    #print('A=',a)
    # Elimination phase
    for k in range(0, n-1): # single comment
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k] # Calculate constant for elimination
                a[i, k+1:n] = a[i, k+1:n] - lam * a[k, k+1:n]
                b[i] = b[i] - lam*b[k]
    #print('A=',a)
    # Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k]-np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
