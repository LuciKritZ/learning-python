def display(name):
    def message():
        return "Hello "

    result = message()+name+"!"
    return result

print(display("Krishal"))
# print(message())
# The above method will only be accessible in the function display()