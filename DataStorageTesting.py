import re
import numpy as np


arr = np.array([1, 2, 3, 4], np.int8)
arr2 = np.array([4, 3, 2, 1], np.int8)

arr3 = np.array([arr, arr2])

print(np.add(arr3[0], arr3[1]))