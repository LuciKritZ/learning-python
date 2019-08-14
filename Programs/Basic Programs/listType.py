# Defining an empty list:
lst = []
# You can add all types of data types in the list.
lst1 = [10, 20, "LuciKritZ", -10, 30.5]
print(lst1)

# Printing the element with the index provided inside the square brackets.
print(lst1[3])

# Slicing the list
print(lst1[3:5])

# Repitition
print(lst1*4)

# Length function
print(len(lst1))

# For adding an element in the list, we use the append() function.
lst1.append(40)
lst1.append(690)
print(lst1)

# For removing an element in the list, we use the remove() function.
lst1.remove("LuciKritZ") # Deleting by value
del(lst1[1]) # Deleting by index. It is an inbuilt function by python.
# If the parameter provided is not in the list, it throws an exception:
    # ValueError: list.remove(x): x is not in the list.
print(lst1)


# To remove all the elements from the list:
lst2 = lst1
lst2.clear()
print(lst2)

# To get the maximum element from the list:
lst3 = [20, 30 ,40, 50, 60]
print(max(lst3))

# To get the minimum element from the list:
print(min(lst3))

# To insert at a particular index:
lst3.insert(3, 99) # First arg: index, Second arg: Value of element.
print(lst3)

# For sorting the list, we can use sort() method
# Ascending Order:
lst3.sort()
print(lst3)
# Descending Order:
lst3.sort(reverse = True)
print(lst3)