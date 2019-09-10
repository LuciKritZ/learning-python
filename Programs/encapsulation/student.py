class Student:
    def __init__(self):
        self.id = 124
        self.name = "Krishal"
        # To mark the variables as private, include the two underscores __ at the beginning.
        self.__Id = 134
        self.__Name = "LOL"

    # To display the private variables:
    def display(self):
        print(self.__Id)
        print(self.__Name)

s = Student()
print(s.id)
print(s.name)
s.display()
# The below two won't work as the variables are private
# print(s.__Id)
# print(s.__Name)

# Using name mangling:
print(s._Student__Id)
# So in python when we make variables or fields, they are not completely hidden.
# To access the private field, the syntax would be:
# object._ClassName__PrivateVariable