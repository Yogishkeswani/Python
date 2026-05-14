friends = ["Apple","Orange",5,45.2,False,"Akash", "Rohan"]
print(friends)
friends.append("Harry") #append means that "Harry" will be attached at the end of the list
print(friends)

l1 = [1,34,5,4,55]
print(l1) # printing the list after
l1.sort()
l1.reverse()
l1.insert(3, 333) # replacing 3 with 333 
print(l1.pop(0)) # The number which will be in the INDEX position 0 will be deleted or popped 
l1.remove(55)
print(l1)

value = l1.pop(3)
print(value)