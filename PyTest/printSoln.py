## module printSoln
''' printSoln(X,Y,freq).
Prints X and Y returned from the differential
equation solvers using printout frequency ’freq’.
freq = n prints every nth step.
freq = 0 prints initial and final values only.
''' 
def printSoln(X,Y,freq):
    def printHead(n):
        print("\n x ",end=" ")
        for i in range (n):
            print(" y[",i,"] ",end=" ")
        print()
    def printLine(x,y,n):
        print("{:13.4e}".format(x),end=" ")
        for i in range (n):
            print("{:13.4e}".format(y[i]),end=" ")
        print()
        
    m = len(Y)
    try: n = len(Y[0])
    except TypeError: n = 1
    if freq == 0: freq = m
    printHead(n)
    for i in range(0,m,freq):
        printLine(X[i],Y[i],n)
    if i != m - 1: printLine(X[m - 1],Y[m - 1],n)

