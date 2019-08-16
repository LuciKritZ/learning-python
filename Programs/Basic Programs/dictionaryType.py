# Dictionary type is a JSON type of data type.
# It has key and value pairs.
dict1 = {
    1: "John",
    2: "Bob",
    3: "Bill"
}

# For printing the dictionary
print(dict1)

# For printing the items of the dictionary.
print(dict1.items())

# For just getting the keys, we can use the keys method.
print(dict1.keys())
# For looping through them:
k = dict1.keys()
for i in k:
    print(i)


# If we want the values, we can use the value method.
print(dict1.values())
# For looping through them:
v = dict1.values()
for i in v:
    print(i)

# For getting the particular value of the key:
print(dict1[3])

# For deleting the values, we can use the del function provided by the Python itself.
del dict1[2]
print(dict1)