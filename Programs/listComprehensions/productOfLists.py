a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Without using the list comprehension
z = []
for i in range(len(a)):
    z.append(a[i]*b[i])

print(z)

# Using the list comprehension
y = []
y = [a[i]*b[i] for i in range(len(a))]
print(y)