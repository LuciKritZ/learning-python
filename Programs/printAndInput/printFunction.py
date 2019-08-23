# Print nothing
print()

# print with repitition
print("Hello"*3)

# By default, the print will print the input in the single line.
# To print it in a new line, we use \n (new line character)
print("All the power \n is within you.")

a,b = 10,20
# Printing values together.
print(a,b)

# To separate the values while printing, we can sep.
print(a,b,sep=",")
# You can give any type of values in the separator:
print(a,b,sep="+++++")

name = "John"
marks = 94.5

# Normal printing
print(name, marks)

# To use strings and then use variables:
print("Name is",name,". Marks are ",marks)

# Another way to deal with it is using %s, %c, %f:
# To restrict the decimal point numbers, we can use %.2f or %.3f
print("Name is %s. Marks are %.2f."%(name, marks))

# Another way to format the data is by using the arguments and format():
print("Name is {}. Marks are {}.".format(name, marks))
# We can not restrict the number of decimal points. If we want to use the decimal points, we will use
# the 2nd way of representing a string.

# We can also use the index. The index defined here is the index of the parameters of the format function.
print("Name is {0}. Marks are {1}.".format(name, marks))