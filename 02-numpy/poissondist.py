import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

""" It estimates how many times an event can happen in 
a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

 """
"""  
It has two parameters:

lam - rate or known number of occurrences e.g. 2 for above problem.

size - The shape of the returned array.
 """
 
arr = random.poisson(lam = 2, size=100)
print(arr)

#visualizing it now

sns.displot(random.poisson(lam = 2, size=100))
plt.show()