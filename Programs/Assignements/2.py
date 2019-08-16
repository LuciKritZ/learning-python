"""
LIST TYPE
"""
# For getting a random number for index.
import random

# Countries List
countries = ["India", "USA", "Australia"]

# Adding an element to the end.
countries.append("PKMKB")

# Deleting a random element.
totalElements = len(countries)
randomIndex = random.randint(0,totalElements)
del countries[randomIndex - 1]

# Inseting an element in the middle
middleElement = int(len(countries)/2)
countries.insert(middleElement+1, "China")
print(countries)


"""
SET TYPE
NOTE: We can not perform any indexing operations, so adding an element to the end,
removing by index and adding a country in the middle is not possible.
All we can do is define a set.
"""
# Defining a Set
countriesOfSetType = {"India", "USA", "Australia"}