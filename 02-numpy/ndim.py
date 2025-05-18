'''Check Number of Dimensions?

NumPy Arrays provides the ndim attribute that returns an integer that tells us

how many dimensions the array have.'''

import numpy as np
#creating a 0-D array
arr = np.array(42)
#creating a 1D array
a = np.array([1,2,3,4,5])
#creating a 2D array

b = np.array([[1,2,3], [4,5,6]])

#creating a 3D array

c = np.array([[[1,2,3], [4,5,6]],[[7,8,9], [10,11,12]]])

#printing the number of dimensions

print("Number of dimensions in 0-D array: ", arr.ndim)
print("1d array dimensions: ", a.ndim)
print("2d array dimensions: ", b.ndim)
print("3d array dimensions: ", c.ndim)