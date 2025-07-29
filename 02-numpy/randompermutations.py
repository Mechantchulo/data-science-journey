import numpy as np
from numpy import random

#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
#random module has permutation() and shuffle() for this

#shuffling arrays means changing arrangement of elements in-place i.e in the array itself
#just shuffles randomly

arr = np.array([3,4,5,6])
random.shuffle(arr)
print(arr)


#generating permutations of arrays
arr1 = np.array([4,5,6,7])
print(random.permutation(arr1))