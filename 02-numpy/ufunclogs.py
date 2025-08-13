import numpy as np
from math import log

""" Logs
NumPy provides functions to perform log at the base 2, e and 10.

We will also explore how we can take log for any base by creating a custom ufunc.

All of the log functions will place -inf or inf in the elements if the log can not be computed. """

# log 2
# create an array starting from 1-9 instead of writing it down
arr = np.arange(1, 10)
print(np.log2(arr))

""" Log at Base 10
Use the log10() function to perform log at the base 10 """

arr2 = np.arange(1, 20)
print(np.log10(arr2))


""" Natural Log, or Log at Base e
Use the log() function to perform log at the base e. """

arr3 = np.arange(1, 5)
print(np.log(arr3))

""" Log at Any Base
NumPy does not provide any function to take log at any base, so we can use the frompyfunc() 
function along with inbuilt function math.log() with two input parameters and one output param """

np_log = np.frompyfunc(log, 2, 1)
print(np_log(100, 15))