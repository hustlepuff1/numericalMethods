# example4_7 뉴턴 랩슨 근 찾기
import numpy as np
def f(x): return np.sin(x)+3*np.cos(x)-2
def df(x): return np.cos(x)-3*np.sin(x)

def newtonRaphson(x, tol=1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx

    if abs(dx) < tol:
        return x, i
    print(f'Too many iterations\n')


root, numIter = newtonRaphson(2.0)
print(f'Root = {root}')
print(f'Number of iterations = {numIter}')
