import numpy as np

""" Hyperbolic Functions
NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and 
produce the corresponding sinh, cosh and tanh values.. """

x = np.sinh(np.pi/2)
print(x)


arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

y = np.cosh(arr)

print(y)

""" 
Finding Angles
Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh 
inverse (arcsinh, arccosh, arctanh).

Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for 
corresponding sinh, cosh and tanh values given. """

z = np.arcsinh(1.0)

print(z)


arr1 = np.array([0.1, 0.2, 0.5])

x1 = np.arctanh(arr1)

print(x1)