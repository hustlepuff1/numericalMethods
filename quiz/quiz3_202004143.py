## quiz_3
from polyFit import *
from numpy import array

xData=array([1.0,2.5,3.5,4.0,1.1,1.8,2.2,3.7])
yData=array([6.0,15.7,27.1,33.8,5.3,9.5,11.1,28.8])
c1=polyFit(xData,yData,1)
print(c1)
sigma1=stdDev(c1,xData,yData)
c2=polyFit(xData,yData,2)
print(c2)
sigma2=stdDev(c2,xData,yData)
print(sigma1,sigma2)
