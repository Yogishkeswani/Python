marks = {
    "Harry" : 100,
    "Yogish" : 80,
    "Shivam" : 50,
    70 : "Manish"  # -- this is also valid 
}

print(marks.items())

print(marks.keys())  # keys are basically the variables in the method marks .. Here, they are - "Harry" , "Yogish" , "Shivam" , 70

print(marks.values()) # values are basically the values in the method marks... Here, they are - 100 , 80 , 50 , "Manish"

marks.update({"Harry" : 99, "Yogish": 56, "Shivam" : 87, 0: "Kartik", 1:"Varun"})    # New dict updated by just a single function() and if any variable is not present then we will 

print(marks)

marks.get("Yogish") # if we give marks.get("Divya") and if Divya is not present in the Dict (here : named Marks)  

print(marks)

# IMPORTANT QUESTION - What is the diff btw the below two statements 
# They both will return the same value 

# Example 1

print(marks.get("Harry")) 

print(marks["Harry"])

# Example 2

print(marks.get("Harry2")) # Harry2 variable was'nt present in the dict marks . Thus, it returns or Prints None

print(marks["Harry2"]) # Returns an error 

marks.pop ("Harry") # Syntax list.pop(index) -- if index won't be given then No problem it will remove the last element / item 

print(marks.popitem())
# Used with dictionaries to remove and return the last inserted key-value pair.
# Syntax = dictionary.popitem()

print(marks)