# module newtonPoly
''' p = evalPoly(a,xData,x).
    Evaluates Newton’s polynomial p at x. The coefficient
    vector {a} can be computed by the function ’coeffts’.
    a = coeffts(xData,yData).
    Computes the coefficients of Newton’s polynomial.
'''


def lagrangePoly(xData, yData, x):
    n = len(xData) - 1  # Degree of polynomial
    L = [0]*(n+1)
    for k in range(0, n+1):
        # Lagrange cardinal functio Li(x)
        Li = 1
        for j in range(n+1):
            if k != j:
                Li *= (x-xData[j])/(xData[k]-xData[j])
        L[k] = yData[k]*Li
    P = sum(L)
    return P


a = [0, 2, 3]
b = [7, 11, 28]
print(lagrangePoly(a, b, 1))
