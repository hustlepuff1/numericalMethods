## example4_12 모든 근 찾기 허수용?
from polyRoots import *
import numpy as np
c = np.array([-250.0,155.0,-9.0,-5.0,1.0]) # 함수의 계수 거꾸로 입력하기!
#c=np.array([-13.,32.,-13.,2.])
#c=np.array([-6.*(1.-1j), 1., -6.*(1.+1.j),2.])
print('Roots are:\n',polyRoots(c,1.e-10))
