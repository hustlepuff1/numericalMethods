import matplotlib.pyplot as plt
import time

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

# C:/Users/henry/Desktop/NumAn23/PyTest/af1

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

# 1번 airfoil 할당
fileName = input('Whats the first airfoil file name?: ')
data = open(fileName, 'r')
data.readlines(1)
for i in data:
    x1.append(float(i.split()[0]))
    y1.append(float(i.split()[1]))
data.close()

time.sleep(2)

# 2번 airfoil 할당
fileName = input('Whats the second airfoil file name?: ')
data = open(fileName, 'r')
data.readlines(1)
for i in data:
    x2.append(float(i.split()[0]))
    y2.append(float(i.split()[1]))
data.close()

time.sleep(2)

# 3번 airfoil 할당
fileName = input('Whats the last airfoil file name?: ')
data = open(fileName, 'r')
data.readlines(1)
for i in data:
    x3.append(float(i.split()[0]))
    y3.append(float(i.split()[1]))
data.close()

# 그래프 1번 그리기
plt.plot(x1, y1, 'b-', label='af1')
plt.axis('equal')


# 그래프 2번
plt.plot(x2, y2, 'g-', label='af2')
plt.axis('equal')


# 그래프 3번 그리기
plt.plot(x3, y3, 'r-', label='af3')
plt.axis('equal')

plt.title('HW01')
plt.legend()

time.sleep(1)
print('Drawing your graph...')
time.sleep(1)
print('End of Program!')
plt.show()
