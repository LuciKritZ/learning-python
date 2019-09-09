# Importing the module that we have just created.
# import myMathModule

# Importing the module with an alias or a name.
# import myMathModule as mA

# print(myMathModule.sum(10, 20))
# print(myMathModule.diff(10, 20))

# print(mA.sum(10, 20))
# print(mA.diff(10, 20))

# ModuleName.FunctionName(arg1, arg2, ... , argN)

# And to totally avoid the name from the import, we can directly use the function:

from myMathModule import *
print(sum(10, 20))
print(diff(10, 20))