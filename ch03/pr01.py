import numpy as np


def init_network():
    network = dict()
    network['W1'] = np.random.random(size=(2, 3)).round(2)