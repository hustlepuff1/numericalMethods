import numpy as np


def gaussPivot(a, b, tol=1.0e-12):
    n = len(b)
    # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i, :]))
    for k in range(0, n-1):
        # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n, k])/s[k:n]) + k
        if abs(a[p, k]) < tol:
            raise ValueError("Matrix is singular")
        if p != k:
            b[[k, p]] = b[[p, k]]
            s[[k, p]] = s[[p, k]]
            a[[k, p]] = a[[p, k]]
        # Elimination
        for i in range(k+1, n):  # Elimination
            if a[i, k] != 0.0:
                lam = a[i, k]/a[k, k]
                a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
                b[i] = b[i] - lam*b[k]
    if abs(a[n-1, n-1]) < tol:
        raise ValueError("Matrix is singular")

    # Back Substitution
    b[n-1] = b[n-1]/a[n-1, n-1]  # Back substitution
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n]))/a[k, k]
    return b
