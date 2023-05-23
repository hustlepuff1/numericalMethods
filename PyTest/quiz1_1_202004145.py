def f(x):
    return 2*x**3 - 13*x**2 + 32*x - 13


def df(x):
    return 6*x**2 - 26*x + 32


def newtonRaphson(x, tol=1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol:
            return x, i
    print('Too many iterations!')


root, numIter = newtonRaphson(2.0)
print('Root = ', root)
print('Num of iterations = ', numIter)
