a = 13
b = 100
c = -66
# print(a,b,c)
x = 33.5
y = 25.8
z = 25
# print(x,y,z)
# To determine what type of data type, a variable is, we use the type() function.
# print(type(a))
# In Python, everything is an object. And so, it will display <class 'int'> which means,
    # a is an object of class int.

#Complex Types
d = 3+5j
print(d)
print(type(d))

# Binary Types
e = 0B1010
print(e)

# Hexadecimal Types
f = 0Xff
print(f)

# Assignment - 1
# Octadecimal Type:
o = 0O20
print(o)

# Booleans or bool can carry two values: true or false.
g = True
print(g)
print(type(g))
print(9 > 8)
# This will return true as 9 > 8

# For conversion of type, we can use the int() function, which converts the float to int
h = int(x)
print(h)
print(type(h))

# Similarly for float, we use float()
i = float(22.5)
print(i)
print(type(i))

# We have bin for binary
print(bin(19))

# We have hex for hexadecimal
print(hex(10))

# And, we have oct for octadecimal
print(oct(10))