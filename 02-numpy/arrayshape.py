import numpy as np

#shape of an array is the number of elements in each dimension
#we use the shape attribute of an array and returns a tuple with index having corresponding elements

arr = np.array([[1,2,3,4,5], [5,6,7,8,9]])
print(arr.shape)# outputs 2 rows and 5 columns

#use ndmin to create a 5-D array

arr1 = np.array([1,2,3,4], ndmin=5)
print("shape of array is: ", arr1.shape)