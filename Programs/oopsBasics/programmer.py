class Programmer:
    # The accessor and mutator methods can be defined and used like this:
    # Setters method
    def setName(self, name):
        self.name = name
    
    # The getters method
    def getName(self):
        return self.name
    
    def setSalary(self, salary):
        self.salary = salary
    
    def getSalary(self):
        return self.salary
    
    def setTechnologies(self, techs):
        self.technologies = techs
    
    def getTechnologies(self):
        self.technologies

p1 = Programmer()
p1.setName("John")
p1.setSalary(10000)
p1.setTechnologies(["Java", "Hibernate", "Spring", "Python"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())

# So this is how we use the getter and the setter methods to set and get the values.