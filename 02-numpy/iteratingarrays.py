import numpy as np

#iterating is like looping through something
#we will use for loop

arr = np.array([1,2,3,4,5,6,7])

for n in arr:
    print(n)#prints all values in the array
    
#iterating 2-D arrays

arr2 = np.array([[1,2,3,4], [5,6,7,8]])

for x in arr2:
    print(x)
    
#to display the 2-D array as only numbers without the arrays we loop in a loop

arr3 = np.array([[1,2,3,4,5], [6,7,8,9,0]])

for x in arr3:
    for y in x:
        print(y)
        
#iterating a 3-D array
arr4 = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4], [5,6,7,8]]])
 
for z in arr4:
    print(z)
    
    
#iterating using the nditer()
arr5 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for a in np.nditer(arr5):
  print(a)
  
#iterating with different datatypes

