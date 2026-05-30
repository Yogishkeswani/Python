# Write a program to find the sum of first n natural numbers using while loop

num = int(input("Enter the value of n"))

i = 1

k = 0

while(i<=num):
    k +=i
    i+=1
print("the sum is - ", k)