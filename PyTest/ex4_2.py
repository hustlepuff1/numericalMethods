## 이분법으로 근 찾기
from bisection import *

def f(x): return x**3 - 10.0*x**2 + 5.0 # 함수
x = bisection(f, 0.0, 1.0, tol = 1.0e-4) # 0부터 1 구간
print('x =','{:6.4f}'.format(x)) # 소숫점 4자리까지 표기
