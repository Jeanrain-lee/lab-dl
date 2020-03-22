import numpy as np


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(b)
print(np.dot(a.T, b))

A = np.array([[1, 2],
              [3, 4]
])
B = np.array([[5, 6],
              [7, 8]
])
print(np.matmul(A, B))

