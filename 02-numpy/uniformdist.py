import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

#unifrom distribution is used to describe probability where events have equal prob to occurence

"""
It has three parameters:

low - lower bound - default 0 .0.

high - upper bound - default 1.0.

size - The shape of the returned array.

"""
x = random.uniform(low=3, high= 5, size = 100)
print(x)

#visualization
data = sns.displot(random.uniform(low = 3, high=5, size=1000))
plt.show(data)