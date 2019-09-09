def decorFun(fun):
    def inner(name):
        result = fun(name)
        result = result+", how are you?"
        return result
    return inner

@decorFun
def hello(name):
    return "Hello "+name

print(hello("John"))