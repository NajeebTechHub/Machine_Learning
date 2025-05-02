# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

import math

x1 = int(input('Enter value of first coordinates = '))
x2 = int(input('Enter value of second coordinates = '))
y1 = int(input('Enter value of third coordinates = '))
y2 = int(input('Enter value of fourth coordinates = '))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'The Euclidean distance between ({x1},{x2}) and ({y1},{y2}) = ',distance)