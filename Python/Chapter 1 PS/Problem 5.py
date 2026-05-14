# Label the program written in problem 4 with comments.
import os

# Specify the directory path
path = "."

# Get and print the contents of the directory
contents = os.listdir(path)

for item in contents:
    print(item)