# example6_4 재귀사다리꼴로 적분
import math
from trapezoid import *
def f(x): return math.sqrt(x)*math.cos(x)


Iold = 0.0
for k in range(1, 21):
    Inew = trapezoid(f, 0.0, math.pi, Iold, k) # 함수, 0 부터 파이까지 적분 범위
    if (k > 1) and (abs(Inew - Iold)) < 1.0e-6: #소숫점 자릿수
        break
    Iold = Inew
print("Integral =", Inew)
print("nPanels =", 2**(k-1))
