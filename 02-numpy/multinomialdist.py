import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt


"""
Multinomial distribution is a generalization of binomial distribution.

It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

It has three parameters:

n - number of times to run the experiment.

pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).

size - The shape of the returned array.
"""

arr = random.multinomial(n = 6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(arr)