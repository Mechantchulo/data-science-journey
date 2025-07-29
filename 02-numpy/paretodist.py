import numpy as np
from numpy import random

""" A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

It has two parameter:

a - shape parameter.

size - The shape of the returned array """

arr = random.pareto(a=3, size = (2,3))
print(arr)