from math import sqrt, sin, pi
s = 0.0
for i in range(101):
    x = 0.01*pi*i
    s = s + sqrt(x)*sin(x)
print('by for-loop',s)

from numpy import sqrt, sin, arange, pi
x = arange(0.0, 1.001*pi, 0.01*pi)
s=sum(sqrt(x)*sin(x))
print('by arange:',s)

from numpy import linspace
x2 = linspace(0.0, 1.0*pi, 101)
s2=sum(sqrt(x2)*sin(x2))
print('by linspace:',s2)
