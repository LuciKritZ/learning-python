# Creating an empty tuple
tpl = ()
tpl2 = (1, 2, 4, 4, 'XYZ')
# Whenever we are using a tuple with a single element, we will always use comma after the
# first element, otherwise, it will consider the element as an integer.
tpl3 = (40)
tpl4 = (40,)
print(type(tpl3))
print(type(tpl4))
# The result will be only 40 as there is no comma at the end.

# Fetching the value of the element by the index:
print(tpl2[2])

# Repition of the tuple:
print(tpl2*2)

"""
NOTE: We can not slice the tuple, as we can't modify the tuple.
"""

# For counting the presence of a particular element in a tuple, we can use the count() method.
print(tpl2.count(4))

# For finding the index of the certain value, we can use the index() method.
print(tpl2.index('XYZ'))
print(tpl2.index(4))

# For converting a list to the tuple, we can use the tuple() method.
lst = [1,2,3,4,5]
tplx1 = tuple(lst) # Converted to tuple and keep in mind, now we can't modify the tplx1
print(type(tplx1))
print(type(lst))

"""
NOTE: Only convert list to tuple when you're sure you won't need any modifications in the list
afterwards. Keeping it for the comparison is a good idea.
"""