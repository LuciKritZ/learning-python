class objectCounter:
    numberOfObjects = 0
    def __init__(self):
        objectCounter.numberOfObjects += 1
    
    # To define a method a static method, we can use @staticmethod before declaring the method.
    @staticmethod
    def displayCount():
        print(objectCounter.numberOfObjects)

ob1 = objectCounter()
ob2 = objectCounter()

objectCounter.displayCount()