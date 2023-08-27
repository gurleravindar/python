import numpy as np
import random

data = np.random.random(16).reshape(2,2,2,2)

print(data)

total  = data.sum(axis=(0, 1)).shape

print(total)
