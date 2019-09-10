# Usage of the class
class Product:
    # The constructor method which will be initialized only once per class will contain all the
    # variables.
    def __init__(self):
        # Self points out to the current object that is being pointed out.
        self.name = 'iPhone'
        self.description = 'Awesome'
        self.price = 700
    
    # Definfing instance functions or variables that can be access these variables or fields.
    def display(self):
        # Always Remember:
        # Self always points to the object that is invoking that method, constructor or another method.
        print(self.name)
        print(self.price)
        print(self.description)
    
# An object of the class Product.
# p1 will be allocated to different and separate memory location. Similarly, for all other objects.
p1 = Product()
print(p1.name)
print(p1.description)
print(p1.price)

# Another object of the class Product.
p2 = Product()
print(p2.name)
print(p2.description)
print(p2.price)
p2.display()