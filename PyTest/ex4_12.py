## example4_12
from polyRoots import *
import numpy as np
c = np.array([-250.0,155.0,-9.0,-5.0,1.0])
#c=np.array([-13.,32.,-13.,2.])
#c=np.array([-6.*(1.-1j), 1., -6.*(1.+1.j),2.])
print('Roots are:\n',polyRoots(c,1.e-10))
