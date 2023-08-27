import numpy as np

arr = np.arange(11)

arr[3:9] = np.multiply(arr[3:9],-1)

print(arr)