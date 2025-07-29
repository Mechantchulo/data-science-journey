#Use the random.normal() method to get a Normal Data Distribution.

""" It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.

 """
 
 #for better visualization use jupyter notebooks

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

arr = random.normal(size = (2,3))
print(arr)

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

#visualizarion of a normal graph

sns.displot(random.normal(size=1000), kind="kde")

plt.show()