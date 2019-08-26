# import is used to include modules. A module is nothing but a python scripts that contains the
# reusable functions or reusable code.
import sys

# retreiving the array of args.
lst = sys.argv
for i in lst:
    print(i)

# Getting the length of the args array.
print(len(lst))

# Accessing the args using index.
print(lst[0])

# To provide the args in VSCode, open launch.json file and add a new object with a name "args" and provide
# the elements as you like.
# Example:
# {
#     // Use IntelliSense to learn about possible attributes.
#     // Hover to view descriptions of existing attributes.
#     // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Python: Current File",
#             "type": "python",
#             "request": "launch",
#             "program": "${file}",
#             "console": "integratedTerminal",
#             "args": ["arg1", "arg2"]
#         }
#     ]
# }