import numpy as np
#copy is used to create a new array
arr = np.array([1,2,3,4,5])
new_arr = arr.copy()
arr[0] = 34

print(arr.base)#returns none since copy owns the data
print(new_arr)

#view is just to view the array meaning any change affects the new one
#view does not own the data
view_array = np.array([6,7,8,9,0])
new_varray = view_array.view()
view_array[0] = 42

print(view_array)
print(new_varray)
