# Write a python program to calculate the square of a number entered by the user.

# a = int(input("Enter a number: "))

# b = (a*a)

# print("The square root of the entered number is : ", b)
import math
a = int(input("Enter a number: "))

b = math.pow(a,2)

# b = a*a # VALID

# b = a**2 # VALID

# b = a^2 # INVALID
print("The square root of the entered number is : ", b)