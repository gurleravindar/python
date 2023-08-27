import numpy as np

data = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])

unique, counts = np.unique(data, return_counts=True)


for i in range(len(unique)):
    print(unique[i] , 'comes' , counts[i] , 'times')