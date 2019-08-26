x = int(input("Enter an integer:"))
if(x%2 == 0):
    print(x, "is an even number.")
else:
    print(x,"is an odd number.")

# Places where we need to check for the multiple conditions, we can use the if else ladder.
# Only of the blocks gets executed.

# Handling the zero:
if(x == 0):
    print("Number is zero.")
elif(x%2 == 0):
    print(x, "is an even number.")
else:
    print(x,"is an odd number.")