import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

#binomial distribution is a discrete distribution
#It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

""" It has three parameters:

n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array. """

arr = random.binomial(n=5, p=0.5, size=10)
print(arr)

#visualization
sns.displot(random.binomial(n=10, p=0.7, size=100))
plt.show()