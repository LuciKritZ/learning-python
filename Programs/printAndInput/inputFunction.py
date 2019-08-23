# Basic usage of input function.
# s = input()
# print(s)

# To give it a label:
# s = input("Enter your name")
# print(s)

# By default, the input is considered of type string.
# To give it a particular type, we can use the type casting.
# i = int(input("Enter an integer number"))
# print(type(i))

# # Without type casting
# i = input("Enter an integer number")
# print(type(i))

# For handling multiple inputs:
# Using spaces:
# lst = [x for x in input("Enter three numbers separated by space:").split()]
# print(lst)

# Using comma:
# lst = [x for x in input("Enter three numbers separated by space:").split(',')]
# print(lst)

# To convert this into integers:
# lst = [int(x) for x in input("Enter three numbers separated by space:").split()]
# print(lst)

# To convert this into float:
lst = [float(x) for x in input("Enter three numbers separated by space:").split()]
print(lst)