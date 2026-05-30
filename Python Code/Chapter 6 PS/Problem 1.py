# Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter a number : "))
gnum = num1

num2 = int(input("Enter a number : "))
if(gnum<num2):
    gnum = num2
  
num3 = int(input("Enter a number : "))
if(gnum<num3):
    gnum = num3

num4 = int(input("Enter a number : "))
if(gnum<num4):
    gnum = num4

print("The greatest number among 4 numbers is : ",gnum)