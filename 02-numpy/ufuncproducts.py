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


""" product Over an Axis
If you specify axis=1, NumPy will return the product of each array. """

arr4 = np.array([1,2,3,4,5])
arr5 = np.array([6,7,8,9,10])
prodresult = np.prod([arr4, arr5], axis =1)
print(prodresult)


""" Cummulative Product
Cummulative product means taking the product partially.

E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

Perfom partial sum with the cumprod() function """

arr6 = np.array([4,5,6,7])
cumprod = np.cumprod(arr6)
print(cumprod)