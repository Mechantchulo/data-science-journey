'''
3-D arrays

An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.'''

import numpy as np

arr = np.array([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr.ndim)