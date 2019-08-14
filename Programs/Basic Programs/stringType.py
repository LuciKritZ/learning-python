# Basic usage of string.
s = " You are awesome. "
print(s)

# This prints in three different lines.
s1 = """You are
the creator of
your destiny"""
print(s1)

# Indexing: Getting the value of the element in the string using the position of the particular 
# element.
print(s[2])

# Repetition: This will multiply the string and repeat it. This can be done by using the
# star operator (*)
print(s*2)

# For getting the length of the string, we can use the len() function.
""" NOTE:
    The index of the string always starts with 0 and goes upto len-1
"""
print(len(s1))

# For Slicing, we can use square brackets and then give the starting and the ending positions.
# Also, it doesn't include the element of the last index.
print(s[0:5])

# It takes the default starting index as 0 and the ending index as len-1 if not provided
# similar to the example provided below:
print(s[0:])
print(s[:8])

# Trying some negative integers.
# -1 always represents the last element.
print(s[-3: -1])

# Steps in slicing:
# Generally, the value of the first argument is one as it considers the next element.
# If we provide the third argument, it will start jumping accross the elements accordingly.
print(s[0:9:2])
print(s[15::-1])
print(s[::-1])

# Strip the spaces
print(s.strip())
# Strips the spaces from ending and beginning.
print(s.lstrip())
# Strips the spaces from the left side.
print(s.rstrip())
# Strips the spaces from the right side.

# Finding the substring
# The other two parameters are the starting index from which we want to start the search
# and the index where we want to end the search.
print(s.find('awe', 0, len(s)))
# If it doesn't finds the sub-string in the given index, it will return -1
print(s.find('awe', 0, 8))

# For getting the count of the element or the sub-string, we can use the count() function.
print(s.count('a'))

# For replacing the old substring to the new substring
print(s.replace('awesome', 'super awesome'))

# For displaying the string in upper case:
print(s.upper())

# For displaying the string in lower case:
print(s.lower())

# For displaying the Title case version of the string:
print(s.title())

integerVariable = 10
decimalVariable = 20.54
booleanVariable = True
stringVariable = "I am the best"

print(integerVariable, decimalVariable, booleanVariable, stringVariable)