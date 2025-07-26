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
    