userInteger = int(input("Enter the number of your choice:"))
isPrimeNumber = True
for i in range(2, userInteger - 1):
    if( userInteger%i == 0):
        isPrimeNumber = False
        break

if(isPrimeNumber):
    print("It's a prime number.")
else:
    print("It's a composite number.")