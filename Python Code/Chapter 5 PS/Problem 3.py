# Can we have a set with 18 (int) and '18' (str) as a value in it?
 
# Method 1 
s = {18 , '18'}

print(s , type(s))

# Method 2
s = set()

s.add(18)

s.add("18")

print(s , type(s))