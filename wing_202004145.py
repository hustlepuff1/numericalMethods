import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 개수 설정하기, 변수 설정 (20, 0.1, 'af1')
num_layers = int(input('Layers of Spars? : '))  # 예시: 20개
layer_height = float(input('Spar Height Difference? : '))  # 예시: 0.1
file_name = input('Airfoil file name? : ')

poleZ = num_layers / 10

data = np.loadtxt(file_name)

x1 = []
y1 = []
z1 = np.linspace(0, poleZ, num=30)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


data1 = open(file_name, 'r')
data1.readlines(1)
for ln in data1:
    x1.append(eval(ln.split()[0]))
    y1.append(eval(ln.split()[1]))
data1.close()


for i in range(num_layers):
    z = i * layer_height
    ax.plot(data[:, 0], data[:, 1], z, 'k')

X1, Z1 = np.meshgrid(x1, z1)
Y1, Z1 = np.meshgrid(y1, z1)

ax.plot_surface(X1, Y1, Z1, alpha=0.8)

ax.set_xlim(-0.5, 1)
ax.set_ylim(-0.5, 1)
ax.set_zlim(-0.5, 2.5)
ax.set_title('WING')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
