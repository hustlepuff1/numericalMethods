import matplotlib.pyplot as plt
import time

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

T1 = [x1, x2, x3]
T2 = [y1, y2, y3]
print('Welcome to the airfoil ploting program!')

time.sleep(2)

a = eval(input('Proceed?: Yes = 1, No = 0 : '))

if a == 1:
    print('You have said yes!')
else:
    time.sleep(1)
    print('goodbye!')
    time.sleep(1)
    quit()

time.sleep(2)

# 에어포일 할당 함수


def airfoil(x, y):
    fileName = input('Whats is airfoil file name? : ')
    data = open(fileName, 'r')
    data.readlines(1)
    for i in data:
        x.append(float(i.split()[0]))
        y.append(float(i.split()[1]))
    data.close()


airfoil(x1, y1)
time.sleep(2)
airfoil(x2, y2)
time.sleep(2)
airfoil(x3, y3)

# 그래프 그리기
for i in range(1, 4):
    plt.subplot(3, 1, i)
    plt.plot(T1[i - 1], T2[i - 1], 'b-')
    plt.axis('equal')
    plt.title(i)

time.sleep(1)
print('Drawing your graph...')
time.sleep(1)
print('End of Program!')
plt.show()
