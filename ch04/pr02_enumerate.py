import numpy as np

y_true = np.random.randint(10, size=10)
print(y_true)

y_true_2 = np.zeros((y_true.size, 10))
print(y_true_2)

for i in range(y_true.size):
    y_true_2[i][y_true[i]] = 1
print(y_true_2)

print()
print('enumerate 함수 연습')

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
