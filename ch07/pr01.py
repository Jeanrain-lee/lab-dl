import numpy as np
import sys, os
sys.path.append(os.pardir)
from dlf.common.util import im2col



x = np.random.rand(10, 1, 28, 28)
print(x.shape)
print(x[0].shape) #(1, 28, 28)
print(x[1].shape) #(1, 28, 28)

# 이런 (1, 28, 28) 이 10개가 있다
print(x[0, 0])

#DATANET

x1 = np.random.rand(1, 3, 7, 7) # (데이터 수, 채널 수, 높이, 너비)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape)  #(9, 75)

x2 = np.random.rand(10, 3, 7, 7) # 데이터 10개
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape) #(90, 75)


class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        pass

    def forward(self, x):
        pass
    
