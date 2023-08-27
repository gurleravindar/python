
import numpy as np
import random

data = np.random.random(12).reshape(4,3)

print("before", data)

data[[0, 2]] = data[[2, 0]]

print('After', data)

