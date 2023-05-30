## test_202004143

from newtonRaphson import *
from math import sin,cos

def f(x): return sin(x)+3*cos(x)-2
def df(x): return cos(x)-3*sin(x)

root1= newtonRaphson(f,df,-2,0)
root2= newtonRaphson(f,df,0,2)

print(root1);
print(root2);
