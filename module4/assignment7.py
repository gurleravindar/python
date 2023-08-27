import numpy as np

np_array = np.array([np.NaN,   1.,   2.,  np.NaN,   3.,   4.,   5.])
print(np_array)

arr_without_nan = np_array[~np.isnan(np_array)]  # use ~ for negation
print(arr_without_nan)