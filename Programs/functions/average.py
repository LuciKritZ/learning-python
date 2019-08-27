# If we give default values to a and b, it will consider the same values when the arguments are not passed.
# However, if we pass the argument, the value of a and b will get replaced by the values provided while
# invoking the function.
def average(a=10, b=20):
    print(b)
    print(a)
    # print("The average of two functions is",(a+b)/2)
    # We can return the value as well.
    return (a+b)/2

result = average(10,20)
print(result)
# OR
print(average(10,30))
# Return is the keyword that we use the return output from the function.

# KEYWORD ARGUMENTS:
# The same function can be called by using the keyword arguments
print(average(a=10,b=20))
# So now, we can assign values directly to the variables.

# Default Arguments:
# If we invoke the average function without any parameters, we get an error that says,
# average function requires two parameters.(Missing arguments)

# print(average())

print(average(30))