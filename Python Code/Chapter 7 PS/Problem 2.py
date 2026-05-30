# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.


# l = ["Harry", "Soham", "Sachin", "Rahul"]

# Method 1

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Good morning {name}")

# Method 2

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Good morning ",name)



# Just a different list

l = ["Soham", "Sachin" , "Sonu" , "Sahil" , "Raj", "Ram", "Sid"]

for name in l:
    if(name.startswith("S")):
        print(f"Good morning {name}")

