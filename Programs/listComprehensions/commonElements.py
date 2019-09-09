a = [2,3,4,5,8]
b = [2,5,7,9,8]

# Without using the list comprehension
result = []
for i in a:
    if i in b:
        result.append(i)

print(result)

# Using the list comprehension
res = [i for i in a if i in b]
print(res)