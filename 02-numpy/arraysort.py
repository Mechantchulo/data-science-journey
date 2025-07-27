import numpy as np

#sorting means putting elements together in ordered manner
# we use sort()

arr = np.array([1,10,4,5])
print(np.sort(arr))

#strig sorting
str_arr = np.array(["apple", "apps", "mango", "zebra"])
print(np.sort(str_arr))

#boolean sort
bool_sort = np.array([True, False, True])
print(np.sort(bool_sort))

#sorting a 2-D array
arr2 = np.array([[10,7,5],[4,1,6]])
print(np.sort(arr2))