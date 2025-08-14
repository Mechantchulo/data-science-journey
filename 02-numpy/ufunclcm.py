import numpy as np

""" Finding LCM (Lowest Common Multiple)
The Lowest Common Multiple is the smallest number that is a common multiple of two number """

num1 = 24
num2 = 6
result = np.lcm(num1, num2)
print(result)


""" Finding LCM in Arrays
To find the Lowest Common Multiple of all values in an array, you can use the reduce() method """

arr = np.array([2,4,6,98])
result1 = np.lcm.reduce(arr)
print(result1)


# Find the LCM of all values of an array where the array contains all integers from 1 to 10:

arr2 = np.arange(1, 23)
result2 = np.lcm.reduce(arr2)
print(result2)