import numpy as np
from numpy import random

#Data distribution is the list of all possible values and how often each value occurs
#random distribution is a set of random numbers that follow a certain probability density function
#probability density function is a function that describes a continuous probability

#choice()method allows us to specify probability of values
""" Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

The probability for the value to be 3 is set to be 0.1

The probability for the value to be 5 is set to be 0.3

The probability for the value to be 7 is set to be 0.6

The probability for the value to be 9 is set to be 0 """

#sum of all probability should be equal to 1 or an error is thrown

random_val = random.choice([2,3,46,6], p = [0.1,0.5,0.0,0.4], size = (100))
print(random_val)

#you can also tweak the size 
arr = random.choice([4,67,5,3], p = [0.1,0.5,0.0,0.4], size = (2,3))
print(arr)