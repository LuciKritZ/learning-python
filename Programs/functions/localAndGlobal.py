x = 124
# A global variable.
def display():
    x=678
    # print(y)
    print(x)
    # A local variable.

    # To use the global variable with the same name, we can use the globals function in python.
    print(globals()['x'])

display()
# The display function will display the value of x given in the function as it will take the precedence.
print(x)
# The global variable will be printed.

# display() can be used as many times as we want by storing it in a variable.
z = display
z()