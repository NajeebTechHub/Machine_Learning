# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

angle1 = int(input('Enter first angle : '))
angle2 = int(input('Enter second angle : '))
angle3 = int(input('Enter third angle : '))

total = angle1 + angle2 + angle3

if(total == 180):
  print('It can form triangle')
else:
  print("It can't form triangle")