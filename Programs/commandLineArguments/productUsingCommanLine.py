import sys

lst = sys.argv
print("Product is:", int(lst[1])*int(lst[2]))

# We have retrieved two command line arguments and performed the operations on them.
# We need to type cast the arguments to int as by default, the arguments are considered to be string.