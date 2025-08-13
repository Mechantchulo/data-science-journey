import numpy as np

""" Addition
The add() function sums the content of two arrays, and return the results in a new array. """

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

result = np.add(x, y)
print(result)

""" Subtraction
The subtract() function subtracts the values from one array with the values from 
another array, and return the results in a new arr """

a = np.array([3,4,5,6,7])
b = np.array([2,1,1,4,6])
sub = np.subtract(a, b)
print(sub)

""" 
Multiplication
The multiply() function multiplies the values from one array with the values 
from another array, and return the results in a new array. """

c = np.array([1,2,3,4])
d = np.array([2,3,4,1])
mut = np.multiply(c,d)
print(mut)

""" Division
The divide() function divides the values from 
one array with the values from another array, and return the results in a new array. """

e = np.array([2,3,4,5,6])
d = np.array([1,2,3,4,1])
div = np.divide(e,d)
print(div)


""" Power
The power() function rises the values from the first array to the power of the values 
of the second array, and return the results in  a new array. """

f = np.array([1,2,3,4,5])
g = np.array([2,32,1,4,5])
pow = np.power(f,g)
print(pow)

""" Remainder
Both the mod() and the remainder() functions return the 
remainder of the values in the first array corresponding to 
the values in the second array, and return the results in a new array. """

h = np.array([10,20,30,40,50])
g = np.array([3,4,5,6,7])
rem = np.remainder(h,g)
print(rem)

""" Quotient and Mod
The divmod() function return both the quotient and the mod.
The return value is two arrays, the first array contains the quotient 
and second array contains the mod. """

i = np.array([10,20,30,40,50])
j = np.array([3,5,7,6,9])
quot = np.divmod(i,j)
print(quot)

""" 
Absolute Values
Both the absolute() and the abs() functions do the same absolute operation element-wise but we 
should use absolute() to avoid confusion with python's inbuilt math.abs() """

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)