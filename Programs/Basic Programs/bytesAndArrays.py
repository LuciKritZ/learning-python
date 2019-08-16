lst = [20, 30, 40, 234]
print(type(lst))

# To convert list into bytes, we use a function called bytes().
by = bytes(lst)
print(type(by))

# You can't perform or add an element to the byte.
# If you will try it, it will throw an exception:
# 'bytes' object does not support item assignment.
# by[4]=[56] 

# For item assignment and modification, we have something called a bytearray.
b1 = bytearray(lst)
print(type(b1))
b1[2] = 33

"""
NOTE: A bytearray can perform the indexing operations.
However, no slicing and repition is allowed on either of these.
"""