import numpy as np

#reshaping means changing the shape of an array
#The shape of an array is the number of elements in each dimension.

#chaging 1-D to 2-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(4,3)
print("1-D to 2-D: ", new_arr)


arr1 = np.array([1,2,3,4,5, 6,7,8,9,10,11,12])
new3d_array = arr1.reshape(2,3,2) 
print("1-d to 2-d: ", new3d_array)