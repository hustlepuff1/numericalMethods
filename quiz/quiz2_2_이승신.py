import numpy as np
from polyRoots import *

a = np.array([-6*(1.0-1.0j),1.0,-6*(1.0+1.0j),2.0])

print(polyRoots(a))