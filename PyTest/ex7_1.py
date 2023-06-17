# example7_2
import numpy as np
from euler import *
import matplotlib.pyplot as plt

# 0부터 0.03까지 적분 계산
def F(x, y):
    F = np.zeros(1)
    F[0] = x**2-4*y[0]
    return F


x = 0.0  # 적분 시작 범위
xStop = 0.03  # 적분 종료 범위
y = np.array([1.0])  # 초기값
h = 0.01  # 간격

X, Y = integrate(F, x, y, xStop, h)
yExact = (31./32.)*np.exp(-4.*X)+(1.0/4.0)*X**2-(1.0/8.0)*X+(1.0/32.0) # 해석해를 계산하여 절단오차 구하기
for i in range(len(X)):
    print('Y= ', Y[i], 'yExact =', yExact[i], 'Error =', Y[i]-yExact[i])
plt.plot(X, Y[:, 0], 'o', X, yExact, '-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('Numerical', 'Exact'), loc=0)
plt.show()
