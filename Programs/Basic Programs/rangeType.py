# Definfing an empty range
# rng = range() # It will throw an error as 1 argument is expected.
# The default index will be 0
rng1 = range(5)

for i in rng1:
    print(i)

# Giving two arguments: Starting index and ending index
rng2 = range(1,6)

for i in rng2:
    print(i)

# We can also pass the step value in the third argument. It will skip the 
# numbers by the defined 3rd argument.
rng3 = range(1, 20, 1)

for i in rng3:
    print(i)