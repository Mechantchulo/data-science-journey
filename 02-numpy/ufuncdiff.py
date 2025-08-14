import numpy as np

""" Differences
A discrete difference means subtracting two successive elements.

E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

To find the discrete difference, use the diff() function. """

arr = np.array([5,10,5,20])
result = np.diff(arr)
print(result)


""" We can perform this operation repeatedly by giving parameter n.

E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , 
then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
 """
 
arr1 = np.array([1,2,3,4,8,6])
result1 = np.diff(arr1, n=3)
print(result1)