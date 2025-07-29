import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

""" Rayleigh distribution is used in signal processing.

It has two parameters:

scale - (standard deviation) decides how flat the distribution will be default 1.0).

size - The shape of the returned array.

 """

arr = random.rayleigh(scale = 2, size=(2,3))
print(arr)