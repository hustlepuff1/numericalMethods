import numpy as np
import matplotlib.pyplot as plt


def gaussElimin(a, b):
    n = len(b)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k+1:n] = a[i, k+1:n] - lam * a[k, k+1:n]
                b[i] = b[i] - lam*b[k]

    for k in range(n-1, -1, -1):
        b[k] = (b[k]-np.dot(a[k, k+1:n], b[k+1:n]))/a[k, k]
    return b


def polyFit(xData, yData, m):
    a = np.zeros((m+1, m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i, j] = s[i+j]
    return gaussElimin(a, b)


def stdDev(c, xData, yData):
    def evalPoly(c, x):
        m = len(c) - 1
        p = c[m]
        for j in range(m):
            p = p*x + c[m-j-1]
        return p

    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n+1):
        p = evalPoly(c, xData[i])
        sigma = sigma + (yData[i] - p)**2
    sigma = np.sqrt(sigma/(n - m))
    return sigma


xData = np.array([])
yData = np.array([])

dataFile = input('File name? : ')

data = open(dataFile, 'r')
data.readlines(1)
for a in data:
    xData.append(eval(a.split()[0]))
    yData.append(eval(a.split()[1]))
data.close()


while True:
    try:
        m = 1
        if m == 0:
            break
        coeff = polyFit(xData, yData, m)
        print("Coefficients are:\n", coeff)
        print("Std. deviation =", stdDev(coeff, xData, yData))
    except SyntaxError:
        break

    x2 = np.arange(0., 3.001, 0.01)
    y2 = np.zeros(len(x2))

    p = np.zeros(len(coeff))
    for i in range(len(p)):
        p[i] = coeff[len(coeff)-1-i]

    for i in range(len(x2)):
        y2[i] = np.polyval(p, x2[i])
    plt.plot(xData, yData, 'o', x2, y2, '-')
    plt.grid(True)
    plt.show()
