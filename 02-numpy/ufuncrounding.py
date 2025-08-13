import numpy as np

""" Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix
rounding
floor
ceil """
""" 
Truncation
Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions. """

arr = np.array([3.78, 8.90])
result = np.trunc(arr)
result2 = np.fix(arr)
print(result)
print(result2)


""" Rounding
The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

E.g. round off to 1 decimal point, 3.16666 is 3.2 """

arr2 = np.array([3.156])
round = np.around(arr2, 2)
print(round)


""" Floor
The floor() function rounds off decimal to nearest lower integer.

E.g. floor of 3.166 is 3. """

arr3 = np.floor([-3.11, 4.567])
print(arr3)

""" 
Ceil
The ceil() function rounds off decimal to nearest upper integer.

E.g. ceil of 3.166 is 4. """

arr4 = np.ceil([4.56, -5.07])
print(arr4)
