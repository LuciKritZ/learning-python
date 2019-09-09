# Importing the whole functools
import functools
# Importing just the reduce function
from functools import reduce

lst = [5,10,15,20]
result = reduce(lambda x,y: x+y, lst)
print(result)