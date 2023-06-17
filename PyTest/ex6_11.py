# example 6_11 #적분점 갯수 판단과 적분값
import math
from gaussQuad import *


def f(x): return (math.sin(x)/x)**3
# def f(x): return x**7 -> can change square number #(math.sin(x)/x)**2


a = 0.0
b = math.pi #범위
Iexact = 1.41815
for m in range(2, 5):
    I = gaussQuad(f, a, b, m)
    print('I=', I)
    if abs(I - Iexact) < 0.00001:
        print("Number of nodes =", m)
        print("Integral =", gaussQuad(f, a, b, m))
        break
