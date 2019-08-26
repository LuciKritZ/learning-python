print("Enter the marks in fashion: 1. Maths 2. Chemistry 3. Physics")
mathsMarks, chemistryMarks, physicsMarks = [float(x) for x in (input("Enter the marks of the student:")).split()]
averageMarks = 0

# For checking whether the student got passed in all the subjects.
if(mathsMarks < 35):
    print("Failed in Mathematics.")
elif(chemistryMarks < 35):
    print("Failed in Chemistry.")
elif(physicsMarks < 35):
    print("Failed in Physics.")
else:
    averageMarks = (mathsMarks + chemistryMarks + physicsMarks)/3
    # For calculating the grade.
    if(averageMarks <= 59):
        print("The student has received grade C.")
    elif(averageMarks <=69):
        print("The student has received grade B.")
    else:
        print("The student has received grade A.")