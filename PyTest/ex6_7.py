## example6_7 Romberg 적분 이용하여 적분
import math
from romberg import *

def f(x): return 2.0*(x**2)*math.cos(x**2)

I,n = romberg(f,0,math.sqrt(math.pi)) #함수, 0부터 루트 파이 -> 적분 범위
print("Integral =",I)
print("numEvals =",n)
