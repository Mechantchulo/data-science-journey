import numpy as np

# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
""" 
Add the Elements of Two Lists
list 1: [1, 2, 3, 4]

list 2: [4, 5, 6, 7]

 """
 
arr1 = [1,2,4]
arr2 = [3,4,5]

result = np.add(arr1, arr2)
print(result)