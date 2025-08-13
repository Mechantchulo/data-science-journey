import numpy as np

""" Products
To find the product of the elements in an array, use the prod() function """

arr = np.array([1,2,3,4,5,6,7])
product = np.prod(arr)
print(product)

# Find the product of the elements of two arrays:

arr2 = np.array([1,2,3,4,5,6])
arr3= np.array([4,5,6,7,8,9])
result = np.prod([arr2, arr3])
print(result)