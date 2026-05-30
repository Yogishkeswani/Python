# Write a program to input eight numbers from the user and display all the unique numbers (once).

# Method 1

n1 = int(input("Enter a number :"))

n2 = int(input("Enter a number :"))

n3 = int(input("Enter a number :"))

n4 = int(input("Enter a number :"))

n5 = int(input("Enter a number :"))

n6 = int(input("Enter a number :"))

n7 = int(input("Enter a number :"))

n8 = int(input("Enter a number :"))

number = {n1 ,n2 ,n3 ,n4 ,n5 ,n6, n7 , n8} # Number set made sucessfully 

print(number)




# Method 2

s = set() # Empty set

n = input ("Enter number : ")
s.add(int(n)) 

n = input ("Enter number : ")
s.add(int(n)) 

n = input ("Enter number : ")
s.add(int(n)) 

n = input ("Enter number : ")
s.add(int(n)) 

n = input ("Enter number : ")
s.add(int(n)) 

n = input ("Enter number : ")
s.add(int(n)) 

n = input ("Enter number : ")
s.add(int(n)) 

print(s)