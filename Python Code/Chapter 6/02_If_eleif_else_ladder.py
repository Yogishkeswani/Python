a = int(input("Enter your age : "))

# If eleif else ladder

if(a>=18):
    print("You are above the age of Consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is not a valid age ")

else:
    print("You are not above the age of Consent")

print("End of Program")