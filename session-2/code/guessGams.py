import random

number = random.randint(1,100)

guess = int(input("Enter your guess number = "))

counter = 1
while guess != number:
    if guess < number:
        print("your guess number is small")
    else:
        print("your guess number is large") 
        
    guess = int(input("Enter your guess number = "))
    
    counter += 1
else:
    print("win")