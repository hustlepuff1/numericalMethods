# 여기서부터는 계산하기위해 선언해주고 정의해주는 과정인것

import numpy as np  # 툴인데 숫자 행렬특화된놈
import matplotlib.pyplot as plt  # 그래프그릴수있게 해주는 툴

# 임의로 회전에 대해 정의한 함수


def ROT(theta, array):  # 어레이는 행렬쓸때 써먹는놈 넘파이에 속해있음
    result = np.array([(np.cos(theta), -np.sin(theta)), (np.sin(theta),
                      np.cos(theta))]) @ array  # 회전행렬 공식 적용 (@array = 행렬곱)
    return result  # 무조건 필요함

# np.array 라는것은 넘파이안에 있는 어레이를 꺼내오겠다 라는 의미
# 점 관점으로 접근해서 불러온 에어포일은 점들의 집합인데 이 전체 점들의 집합을 통채로 회전시키기 위한 define


airfoil_x = []  # 리스트
airfoil_y = []
airfoil_mat = []
# 위에있는놈들은 창고를 만들어준다는 의미로 받아들이면됨 아무거나 다 넣어도 ㄱㅊ

x = np.arange(0.0, 10, 0.001)

data = open('naca4415.txt', 'r')  # 데이터를 불러왔다
data.readlines(1)  # 불러온 데이터파일을 읽어내겠다
for a in data:  # a 는 a 인데 데이터 안에 있는 모든요소를 a 라는 곳 안에 다 하나씩 때려넣겠다
    airfoil_x.append(eval(a.split()[0]))  # 여기 두놈은... 걍 외워라...
    airfoil_y.append(eval(a.split()[1]))
data.close()  # 데이터를 다 끝냈으면 닫아서 리소스 안먹게 해주는 최적화작업, 안해도 돌아가긴함 좀 느려질뿐


for b in range(0, len(airfoil_x)):  # for루프 안에 b가 0부터 해당되는 길이 까지의 범위를 정해준다 이거안해주면 일일히 다써야함
    airfoil_mat.append(np.array([airfoil_x[b]-0.5, airfoil_y[b]]))
    # 이녀석안에 넘파이 어레이를 가지고 위에서 x, y로 찢은 데이터를 추가한다 (-0.5는 걍 평행이동한거임 중심에 맞출라고)

# -----------------------------------
# 여기서부터는 직접 계산을 돌리고 플로팅하는과정

# 똑같이 계산할놈들 창고를 만들어준다
rot_airfoil_x = []
rot_airfoil_y = []
result_x = []
result_y = []
testcase = np.arange(0, 10, 1)  # 레인지 함수이용해서 써도 괜찮음


for case in testcase:  # 테스트케이스안에 있는 놈들을 하나씩 불러오겠다!, 얘는 에어포일 전체의 관점에서 돌려줄때 사용한다는 의미
    angle = np.arctan(np.cos(case))  # 각도를 정의하고 구한것

    for i in range(0, len(airfoil_mat)):  # 여기에 들어가는 포문은 에어포일 형태자체에서 각각의 점들을 연산을하는것
        tmp = ROT(angle, airfoil_mat[i])
        tmp.tolist()
        rot_airfoil_x.append(tmp[0] + case)
        rot_airfoil_y.append(tmp[1] + np.sin(case))

    result_x.append(rot_airfoil_x)
    result_y.append(rot_airfoil_y)

for i in range(0, len(result_x)):
    plt.scatter(result_x[i], result_y[i], s=1)

plt.plot(x, np.sin(x), color='blue')
plt.grid(True)
plt.show()
