'''
keras Functional API
'''
import numpy as np
from tensorflow.keras import Sequential, Model
from tensorflow.keras import layers
from tensorflow.keras import Input

# X(N, 64) -> 8 x 8 | Dense(32) -> ReLU -> Dense(32) -> ReLU -> Dense(10) -> Softmax
seq_model = Sequential()

# 순서 |  model에서 정의, 컴파일, fit (그 과정에서 데이터 배치, epoch, loss를 줍니다)

# 모델 설계
seq_model.add(layers.Dense(32, activation='relu', input_shape=(64, )))  # (64, ) => 1차원 벡터다
seq_model.add(layers.Dense(32, activation='relu'))
seq_model.add(layers.Dense(10, activation='softmax'))
seq_model.summary()

# 모델 컴파일




