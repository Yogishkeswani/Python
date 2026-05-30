# Can you change the values inside a list which is contained in set s?

# s = {8, 7, 12, "Harry", [1,2]}

# Answer - You cannot change the values inside a list contained in a set because a list itself cannot exist inside a set in the first place.

s = {8, 7, 12, "Harry", [1,2]}

print(s) # This will give you an error because s is a set and [1,2] is a list so we can never enter a list in a set . 