import numpy as np

#In numpy we join arrays by axes
#we use concatenate() method

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([4,5,6,7,8])

joined_arr = np.concatenate((arr1, arr2))
print(joined_arr)

#joining 2-d arrays along axis 1
#axis 0 = row && axis 1 = column so it will join the columns


arr3 = np.array([[1,2,3,4], [5,6,7,8]])
arr4 = np.array([[1,2,3,4], [5,6,7,8]])
joined_array = np.concatenate((arr3, arr4), axis = 1)
print(joined_array)

#joining arrays using the stack function
#stacking is same as concatenation but is done along a new axis
#we use stack()

arr5 = np.array([1, 2, 3])

arr6 = np.array([4, 5, 6])

arr_stack = np.stack((arr1, arr2), axis=1)

print(arr_stack)

#stacking along the rows
#here we use hstack()

arr7 = np.array([1, 2, 3])

arr8 = np.array([4, 5, 6])

arr_hstack = np.stack((arr1, arr2), axis=1)

print(arr_hstack)
#vertical we use the vstack