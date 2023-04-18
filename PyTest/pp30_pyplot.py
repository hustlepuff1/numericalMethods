import matplotlib.pyplot as plt
from numpy import arange, sin, cos
x = arange(0.0, 6.2, 0.2)
plt.plot(x, sin(x), 'o-', x, cos(x), '^-')
# plt.plot(x,sin(x),'o-')
# plt.plot(x,cos(x),'s-')
plt.xlabel('x')
plt.ylabel('function')
plt.legend(('sin', 'cos'), loc=0)
plt.grid(True)
plt.savefig('testplot.jpg', format='jpg')

plt.show()

input("\nPress return to exit")
