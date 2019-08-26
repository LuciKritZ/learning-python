userInput = int(input('Enter a desired number:'))
i = 0
while(i < userInput):
    i+=1
    if(i > 100):
        break
    elif(i%10 == 0):
        continue
    else:
        print(i)