from abc import abstractmethod, ABC
# An interface class where all the methods in the class are abstract methods.
class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Methods:
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        # for passing the method without doing the implementation.
        pass

# Interface
class Audi(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Methods:
    def start(self):
        print("Starting the "+self.model)
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        # for passing the method without doing the implementation.
        pass
    
# To inherit the class, we include them in the brackets just as in a function in python.
class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        # BMW.__init__(self, make, model, year)
        # We can use the super keyword in Python, which will by default choose the super or the parent
        # class instead of writing the parent class name and then we will not include self.
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    
    # In addition to this, the child class can also define it's own functions:
    def display(self):
        print("The cruise control is "+str(self.cruiseControlEnabled))
    
    # Method Overriding
    def start(self):
        # If we want to invoke the overridden function of the parent class, it can be done using the
        # super keyword.
        super().start()
        print("Started!")
    
    def stop(self):
        super().stop()
        print("Stopped")
    
    # Defining the abstract class from the parent class
    def drive(self):
        print("Three series is being driven")

class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
    
    # Defining the abstract class from the parent class
    def drive(self):
        print("Five series is being driven.")

    def start(self):
        # If we want to invoke the overridden function of the parent class, it can be done using the
        # super keyword.
        super().start()
        print("Started!")
    
    def stop(self):
        super().stop()
        print("Stopped")
    

# Creating the object of the child class:
threeSeries = ThreeSeries(True, "BMW", "328i", 2018)

# Inheriting the methods as well as variables.
# After writing the same name of the method, we will see the method of the child class instead of the
# parent class. This is called method overriding.
threeSeries.start()
threeSeries.drive()
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.display()
threeSeries.stop()

# So this is how we implement the inheritance. Everything in parent class is available in the child
# class to use.

# Using five series:
fiveSeries = FiveSeries(True, "BMW", "545i", 2018)
fiveSeries.start()
fiveSeries.drive()
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.stop()