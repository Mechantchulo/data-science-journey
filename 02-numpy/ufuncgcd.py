import numpy as np

""" Finding GCD (Greatest Common Devisor)
The GCD (Greatest Common Devisor), also known as HCF (Highest Common Factor) is 
the biggest number that is a common factor of both of the numbers.
 """
num1 = 54
num2 = 68
result = np.gcd(num1, num2)
print(result)


""" Finding GCD in Arrays
To find the Highest Common Factor of all values in an array, you can use the reduce() method.
 """

arr = np.array([45,68,90])
result1 = np.gcd.reduce(arr)
print(result1)


