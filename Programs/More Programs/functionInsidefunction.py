# Using functions inside a function.
def display(fun):
    return "Hello" +fun

def name():
    return "Krishal"

print(display(name()))