class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    
    class Engine:
        def __init__(self, number):
            self.number = number
        
        def start(self):
            print("Engine has started.")
    
c = Car("BMW", 2017)

# You need an object of the outer class to access the inner class.
e = c.Engine(998877)
e.start()