import numpy as np

# 마스킹 연산
# 특정 조건에 해당하는 행렬 값 바꾸기
# 원하는 픽셀 밝기 조절에 응용 가능

array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10
print(array2)

array1[array2] = 100
print(array1)

# 복수 객체 저장 및 불러오기

a1 = np.arange(0, 10)
a2 = np.arange(10, 20)

np.savez('saved.npz', array3=a1, array4=a2)
data = np.load('saved.npz')
result1 = data['array3']
result2 = data['array4']
print(result1)
print(result2)
