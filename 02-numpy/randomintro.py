import numpy as np
#random number is a number that cannot be predicted
#Random numbers are generated through a generation algorithm called pseudo random
# we work with a random module to generate random numbers

from numpy import random

random_number = random.randint(100)
print(random_number)

#Generating random floats we use rand()
x = random.rand()
print(x)

#generating random arrays
#it takes a size parameter to specify shape of a array
arr = random.randint(100, size = (3))
print(arr)

#create a random 2-D array with 2 rows and 5 columns using the size parameter
arr1 = random.randint(50, size = (2,5))
print(arr1)

#rand() also specifies the shape of an array too
arr2 = random.rand(5)
print(arr2)

#use rand() to create a random array of size 3,4
arr3 = random.rand(3,4)
print(arr3)

#Generating a random number from an array
#choice() allows you to choose numbers from an array

arr4 = random.choice([3,5,4,6])
print(arr4)

#you can also add the size parameter to get the shape of the output
arr5 = random.choice([1,2,3,4,5,6], size = (2,2))
print(arr5)