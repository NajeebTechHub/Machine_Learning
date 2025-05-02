# Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

num1 = int(input('Enter first number = '))
num2 = int(input('Enter second number = '))

dummy = num1
num1 = num2
num2 = dummy

print(num1)
print(num2)