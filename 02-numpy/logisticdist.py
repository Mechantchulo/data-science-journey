import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

""" Logistic Distribution is used to describe growth.

Used extensively in machine learning in logistic regression, neural networks etc.

It has three parameters:

loc - mean, where the peak is. Default 0.

scale - standard deviation, the flatness of distribution. Default 1.

size - The shape of the returned array. """


arr = random.logistic(loc = 3, scale = 2, size=(2,3))
print(arr)

sns.displot(random.logistic(loc = 3, scale = 2, size = 1000))
plt.show()