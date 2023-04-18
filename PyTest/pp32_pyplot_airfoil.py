import matplotlib.pyplot as plt

x = []
y = []
finput = input('airfoil file name?:')
data = open(finput, 'r')
data.readlines(1)
for ln in data:
    x.append(eval(ln.split()[0]))
    y.append(eval(ln.split()[1]))
    # print('x=',x,' y=',+y)
data.close()
plt.plot(x, y, '-')
plt.axis('equal')  # x, y 축 eq
plt.show()
input("\nPress return to continue")
