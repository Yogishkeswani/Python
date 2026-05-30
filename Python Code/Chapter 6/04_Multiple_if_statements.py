a = int(input("Enter your age : "))

# If Statement no. 1

if(a%2 ==0):
    print("a is even")

# End of Statement no. 1 

# If Statement no. 2


if(a>=18):
    print("You are above the age of Consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is not a valid age ")

else:
    print("You are not above the age of Consent")

# End of Statement no. 2 

print("End of Program")