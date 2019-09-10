# It can be done by setters and getters in similar to the other programming languages.
class Student:
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
s = Student()
s.setId(23)
s.setName("Krishal the great!")
print(s.getId())
print(s.getName())