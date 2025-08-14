import numpy as np

""" Trigonometric Functions
NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and 
produce the corresponding sin, cos and tan values. """

# Find sine value of PI/2:
result = np.sin(np.pi/2)
print(result)

""" Convert Degrees Into Radians
By default all of the trigonometric functions take radians as parameters but we 
can convert radians to degrees and vice versa as well in NumPy. """

# we use deg2rad()

arr1 = np.array([90, 360, 45])
result1 = np.deg2rad(arr1)
print(result1)

# Radians to Degrees we use rad2deg()

arr2 = np.array([0.234, 0.267])
result2 = np.rad2deg(arr2)
print(result2)



""" Finding Angles
Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for 
corresponding sin, cos and tan values given.
 """
 
arr3 = np.array([1, 0.5])
radr = print(np.arcsin(arr3))


""" Hypotenues
Finding hypotenues using pythagoras theorem in NumPy.

NumPy provides the hypot() function that takes the base and perpendicular values 
and produces hypotenues based on pythagoras theorem. """

height = 7
base = 8
hypot = np.hypot(height, base)
print(hypot)