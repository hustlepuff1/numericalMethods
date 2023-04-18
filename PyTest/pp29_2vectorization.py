import time
from math import sqrt, sin, pi
n = eval(input('number of steps:'))
start = time.time()
s = 0.0
for i in range(n+1):
    x = 1./n*pi*i
    s = s + sqrt(x)*sin(x)
print('by for-loop', s, '\ttime:', time.time()-start)

from numpy import sqrt, sin, arange, pi
start1 = time.time()
x = arange(0.0, (1+1./(10*n))*pi, pi/n)
s = sum(sqrt(x)*sin(x))
print('by arange:', s, '\ttime:', time.time()-start1)


from numpy import linspace
start2 = time.time()
x2 = linspace(0.0, 1.0*pi, n+1)
s2 = sum(sqrt(x2)*sin(x2))
print('by linspace:', s2, '\ttime:', time.time()-start2)
