import numpy as np

#slicing  an array means taking values from one index to a given index
#let's say from index 0 to index 2 of an array of array-length 10 -> [ start: end ]

#slice form index 1 to 5
arr1 = np.array([ 1,2,3,4,5,6,7,8,9])
print("[1:5]: ", arr1[1:5])
#result excludes the last index but includes the first index

#from index 4 to end of the array
arr = np.array([ 1,2,3,4,5,6,7,8,9])
print("[4:end]: ", arr1[4:])

#from beginning to index 4
arr2 = np.array([ 1,2,3,4,5,6,7,8,9])
print("[start:4]: ", arr1[:4])
#result excludes the last index but includes the first index

""" #Negative slicing -> we use minus sign 
[-3: -1] ->means from value index 3 to value index 1 from the end of the array """
#it is like reversing
arrn = np.array([ 1,2,3,4,5,6,7,8,9])
print("[-3:-1]: ", arrn[-3: -1])

#step value [1:3:2] -> 2 represents the steps
steparr = np.array([1,2,3,4,5,6,7,8,9])
print("[1:5:2]: ", steparr[1:5:2])

#slicing 2-D arrays

arr2 = np.array([[1,2,3], [4,5,6]])
print("array index 0 [0:2]: " ,arr2[0, 0:2])




# print the value at index 2 of the first and second row
# [0:2, 2] -> means from the first row to the second row, and in each row
# get the value at index 2

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
