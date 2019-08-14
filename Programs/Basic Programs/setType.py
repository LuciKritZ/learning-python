#Creating an empty set 
st = {}

# Basic
st1 = {10, 20, 30, 40}
print(st1)
print(type(st1))

# Trying to add the duplicate values:
st2 = {10, 20, 30, 40, 40, 20}
# It will automatically remove the duplicate elements.
print(st2)

# To perform an update operation i.e, to add an element to set, we can use update() method.
# We can provide any number of elements we want to add.
st1.update([88, 91, 68])
print(st1)

# NOTE:
# So, we can not perform indexing, slicing, and repitition
# print(st1[0])
# print(st1[0:5])
# print(st1*3)
# It will throw an exception: 'set' object does not support indexing
# 'set' object is not subscriptable - Trying to slice
# unsupported operand type(s) for *: 'set' and 'int' : Trying to repeat.

# To remove the element from the set:
st1.remove(10)
print(st1)


# Conversion of set to frozen set. Once it's converted to frozen set, the update and remove
# methods can not be performed.
f = frozenset(st2)
# f.update(20)
# f.remove(10)
# The frozen set doesn't even support these methods. All we can do is traverse using for loop.