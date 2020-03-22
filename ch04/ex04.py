import numpy as np

a = np.array([1, 2, 3])
print('dim:', a.ndim) #1
print('shape:', a.shape) # 3,0
print('size:', a.size)  # size: 원소 전체의 개수
print('len:', len(a))

A = np.array([[1, 2, 3],
              [4, 5, 6]])
print('dim:', A.ndim) #2
print('shape:', A.shape) # 2,3
print('size:', A.size)  # size = shape[0] * shape[1]
print('len:', len(A))

print(A.shape[0])
print(A.shape[1])