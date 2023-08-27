import numpy as np
import random

data = np.random.random(9).reshape(3,3)

np_new = np.sort(data, axis=0)
print(np_new)
