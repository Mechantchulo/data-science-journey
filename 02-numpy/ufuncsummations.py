import numpy as np

""" Summations
What is the difference between summation and addition?

Addition is done between two arguments whereas summation happens over n elements.
Summation is more of like getting the sum of everything in there. """

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([4,5,6,7,8])
result = np.sum([arr1, arr2])
print(result)


""" Summation Over an Axis
If you specify axis=1, NumPy will sum the numbers in each array """

arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])
results = np.sum([arr3, arr4], axis = 1)
print(results)


""" Cummulative Sum
Cummulative sum means partially adding the elements in array.

E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

Perfom partial sum with the cumsum() function. """

arr5 = np.arange(1,10)
cumsum = np.cumsum(arr5)
print(cumsum)