# without using the list comprehension
lst = []
for x in range(1,11):
    lst.append(x**3)

print(lst)

# Using the list comprehension
lst1 = []
lst1 =  [x**3 for x in range(1,11)]
print(lst1)