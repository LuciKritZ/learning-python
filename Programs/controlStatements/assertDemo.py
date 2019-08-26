x = int(input("Please enter an integer 10."))
assert x>10, "Wrong number entered."
print("You entered", x)

# Assertions is used for obtaining specific behaviour along with the message exception.
# If there is no assertion error, the program will run normally, but if the assertion fails,
# it will display the message along with a link where you can find, exactly where the assertion was used. 