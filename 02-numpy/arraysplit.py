import numpy as np

#splitting is the reverse operation of joining
#it breaks one array into multiple
#we use array_split() method for this

arr = np.array([1,2,3,4,5,6])
split_arr = np.array_split(arr, 3)
print(split_arr)
#this won't necessarily split equaly but it will split to number specified

#splitting 2-D arrays

arr1 = np.array([[1,2,3,4], [5,6,7,8]])
new_Split_arr = np.array_split(arr1, 2, axis = 1)
print(new_Split_arr)