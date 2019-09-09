def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decor
def integer():
    return 10

def num():
    return 5

resultFun = decor(num)
print(resultFun())

print(integer())

# If you always want a decorator function to apply to a function, we can do that by
# using the @operator or symbol.