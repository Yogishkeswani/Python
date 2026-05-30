# Write a program to find whether a number is prime or not

num = int(input("Enter the number: "))

k = 0
i = 1

while(i <= num):

    if(num % i == 0):
        k += 1

    i += 1


if(k == 2):
    print(num, "is a prime number")

else:
    print(num, "is not a prime number")