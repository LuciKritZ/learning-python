def customGen(x,y):
    while x<y:
        yield x
        x+=1

result = customGen(10,30)
for i in result:
    print(i)

# Whenever we want to sort or customize the list according to our specific requirements, we can use the yield
# function or the custom generators. 