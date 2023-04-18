import math as m
import matplotlib.pyplot as plt
from numpy import arange, sin, cos
x = arange(0.0, 6.2, 0.2)
plt.plot(x, sin(x), 'o-',)
plt.xlabel('x')
plt.legend(('sine', 'cosine'), loc=3)
plt.grid(True)
plt.savefig('testplot.png', format='png')
# plt.show()


def rotate(cpx, cpy, px, py, deg):
    global dx, dy
    dx = (px - cpx) * m.cos(deg) - (py - cpy) * m.sin(deg) + cpx
    dy = (px - cpx) * m.sin(deg) + (py - cpy) * m.cos(deg) + cpy
    return dx, dy


x = []
y = []
chx = []
chy = []
for i in range(0, 10, 1):
    deg = (m.pi/180)*i*36
    rad = ((m.pi)/4)*cos(deg)
    k = 0
    finput = "NACA0009.txt"
    data = open(finput, 'r')
    data.readlines(1)
    for ln in data:
        x.append(deg+eval(ln.split()[0])-1)
        y.append(sin(deg)+eval(ln.split()[1]))
        rotate(x[0], y[0], x[k], y[k], rad)
        chx.append(dx)
        chy.append(dy)
        k += 1
    plt.plot(chx, chy, '-.')
    x = []
    y = []
    chx = []
    chy = []
    data.close()
plt.show()
