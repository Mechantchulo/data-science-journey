import numpy as np

""" What is a Set
A set in mathematics is a collection of unique elements.

Sets are used for operations involving frequent intersection, union and difference operations. """

""" Create Sets in NumPy
We can use NumPy's unique() method to find unique 
elements from any array. E.g. create a set array, but remember that the set arrays should 
only be 1-D arrays. """

arr = np.array([1,2,3,3,3,3,3,5,57,484,48])
result = np.unique(arr)
print(result)


""" Finding Union
To find the unique values of two arrays, use the union1d() method. """

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)


""" Finding Intersection
To find only the values that are present in both arrays, use the intersect1d() method. """

arr3 = np.array([12,3,4,5,6])
arr4 = np.array([13,3,4,67])
newarr1 = np.intersect1d(arr1, arr2)
print(newarr1)


""" Finding Symmetric Difference
To find only the values that are NOT present in BOTH sets, use the setxor1d() method """

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr2 = np.setxor1d(set1, set2, assume_unique=True)

print(newarr2)