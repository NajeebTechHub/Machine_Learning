# Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

num = int(input('Enter any number for calculating factorial : '))

fac = 1
for i in range(1,num+1):
  fac = fac * i
print(f'The factorial of {num}! is = {fac}')