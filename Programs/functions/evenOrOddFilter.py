lst = [10, 33, 88, 90, 69]

# Using Filter for performing the operations on list.
result = list(filter(lambda x:x%2==0, lst))

# Printing result
print(result)

# Iterating over the result list.
for i in result:
    print(i)