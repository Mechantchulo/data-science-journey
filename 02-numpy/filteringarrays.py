import numpy as np

#removing some elements out of an array is called filtering
#we use the boolean index list

arr = np.array([1,2,3,4,5,6])
filter_arr = [True, True, False ,True, False, True]

new_arr = arr[filter_arr]
print(new_arr)#only values with True will be output


#create a filtered array of numbers >42

arr2 = np.array([12,3,45,67,85])
filtered_arr = []

for x in arr2:
    if x>42:
        filtered_arr.append(True)
    else:
        filtered_arr.append(False)
        
new_filtered = arr2[filtered_arr]
print(new_filtered)

#create a filtered array that returns even numbers only
arr3 = np.array([2,4,56,78,47,7,38,54,455])
filtered_arr1 = []
for y in arr3:
    if y%2==0:
        filtered_arr1.append(True)
    else:
        filtered_arr1.append(False)
        
even_arr = arr3[filtered_arr1]
print(even_arr)

#we can still create directly from the original array

arr4 = np.array([2,34,5,6,78])
new_filter_arr = arr4 > 42
new_arr_new = arr4[new_filter_arr]
print(new_arr_new)
