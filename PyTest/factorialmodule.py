## module factorialmodule
'''factorial(n),
calc n!
'''

e=2.718
pi=3.14

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
