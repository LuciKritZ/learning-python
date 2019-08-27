"""
ALGORITHM FOR RECURSION
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    NOTE:
    Never ever forget to give the end condition or it can result in an infinite loop and the application
    will run out of memory.
"""

def factorial(n):
    if n==0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

print(factorial(53))