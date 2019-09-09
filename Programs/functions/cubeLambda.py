# First using the normal function using def keyword
def cube(n):
    return n**3

print(cube(2))

# Using the lambda function and storing it in a variable and then using the variable as the function.
f = lambda n: n**3
print(f(2))