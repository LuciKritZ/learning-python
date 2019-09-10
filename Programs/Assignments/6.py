# Definfing a class:
class Patient:
    # Setters
    def setId(self, id):
        self.patientId = id
    
    def setName(self, name):
        self.patientName = name
    
    def setSSN(self, ssn):
        self.patientSSN = ssn
    
    # Getters
    def getId(self):
        return self.patientId
    
    def getName(self):
        return self.patientName
    
    def getSSN(self):
        return self.patientSSN


# Making an object
patient = Patient()

# Using the setters:
patient.setId(69)
patient.setName("PKMKB")
patient.setSSN(6969)

# Using the getters:
print("ID: "+str(patient.getId()))
print("Name: "+patient.getName())
print("SSN: "+str(patient.getSSN()))

"""
    NOTE:
    Always convert into string when the variable is a number when you concatenate or else
    it will throw an error: str is expected.
"""