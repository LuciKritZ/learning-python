# We use logical operators to form logic as the name suggests.\
# They operate against the boolean variables.
# They are: AND, OR and NOT
# AND: X and Y (If both are true)
# OR: X or Y (If anyone of them is true)
# NOT X: If X is not true.

x=20
y=30

# AND
print((x == 20 and y == 30)) # True
print((x == 25 and y == 30)) # False

# OR
print((x == 20 or y == 30)) # True
print((x == 25 or y == 30)) # True
print((x == 25 or y == 31)) # False

# NOT
print(not(x == 25 or y == 31)) # True