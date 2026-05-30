# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {} # Made an empty dictonary . Do not say that this is an empty set .. WHY? because the syntax for Empty Set is : 

# <variable name> = set() 

name = input("Enter friends name : ")
lang = input("Enter Language name :")
d.update({name : lang})  
 
name = input("Enter friends name : ")
lang = input("Enter Language name :")
d.update({name : lang})
 
name = input("Enter friends name : ")
lang = input("Enter Language name :")
d.update({name : lang})
 
name = input("Enter friends name : ")
lang = input("Enter Language name :")
d.update({name : lang})
 
print(d) # Printing the whole dictionary