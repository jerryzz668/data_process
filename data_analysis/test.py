import numpy as np

# arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
arr1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

batch = np.random.choice(3, 2)
arr1_batch1 = arr1[batch]
print(arr1_batch1)
