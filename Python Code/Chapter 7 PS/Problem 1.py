# # Program to print multiplication table of a given number





# # Method 1

# num = int(input("Enter a number : "))

# print("The table of", num)

# for i in range(11):
#     print(num, "x", i, "=", (num * i))






# # Method 2

# num = int(input("Enter a number : "))

# print("The table of", num)

# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")


# # f"" is called an f-string in Python
# # It allows us to directly insert variables inside a string using {}

# # {num} inserts the value of num
# # {i} inserts the value of i
# # {num*i} inserts the result of num multiplied by i

# # print(f"{num} X {i} = {num*i}")

# # Example:
# # If num = 5 and i = 2
# # Output will be:
# # 5 X 2 = 10








































# Program to print multiplication table of a given number



num = int(input("Enter a number : "))

i = 1

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
