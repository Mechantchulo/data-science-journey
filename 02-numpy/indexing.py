import numpy as np

#accessing the first index of a 0-D array

arr = np.array(2)

#accessing the first index of a 1-D array

arr1 = np.array([ 1, 24, 3 ])

#accessing the first index of a 2-D array

arr2 = np.array([[1,2,3], [2,4,6]])



print("First 0-D array index: ",arr)
print("First 1-D array index: ", arr1[0])
print("First 2-D array index: ",arr2[0,0])



