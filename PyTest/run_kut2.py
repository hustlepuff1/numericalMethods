## module run_kut2
''' X,Y = integrate(F,x,y,xStop,h).
2nd-order Runge-Kutta method for solving the
initial value problem {y}’ = {F(x,{y})}, where
{y} = {y[0],y[1],...y[n-1]}.
x,y = initial conditions
xStop = terminal value of x
h = increment of x used in integration
F = user-supplied function that returns the
array F(x,y) = {y’[0],y’[1],...,y’[n-1]}.
''' 
import numpy as np
def integrate(F,x,y,xStop,h):

    def run_kut2(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        
        return K1

    X = [] # create empty list
    Y = []
    X.append(x) # append x to the list
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut2(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y) # return numpy array
