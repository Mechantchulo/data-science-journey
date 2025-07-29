import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt


""" Chi Square distribution is used as a basis to verify the hypothesis.

It has two parameters:

df - (degree of freedom).

size - The shape of the returned array. """

arr = random.chisquare(df=2, size= (2,3))
print(arr)