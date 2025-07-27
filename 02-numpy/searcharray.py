import numpy as np
#you can search for a certain value in an array
#use where()

arr = np.array([1,2,3,4,5])
search_value = np.where(arr == 3)
if search_value in arr:
    print("Found ", search_value)# prints the index position of that value 
    
#find even value indexes

arr1 = np.array([1,2,3,4,5,6,7,8])
even_val = np.where(arr1%2 == 0)
print(even_val)

#find odd value indexes
arr2 = np.array([1,2,3,4,5,6,7,8])
odd_val = np.where(arr2%2 == 1)
print(odd_val)
    
#searchsorted() performs a binary search in array and returns index value where it would be inserted
#find indexes where value 7 should be inserted
#it assumes the arrays aresorted so it returns the index where a value must be
arr3 = np.array([6,8,7,9])
sort_arr = np.searchsorted(arr3, 7)
print(sort_arr)

#we can search from the right
arr4 = np.array([6,8,7,9])
sort_arr1 = np.searchsorted(arr3, 7, side='right')
print(sort_arr1)

#searching for more than 1 value
arr5 = np.array([1,3,5,7])
sort_arr2 = np.searchsorted(arr5, [10,0,4])
print(sort_arr2)