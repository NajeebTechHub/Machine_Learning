# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

p = int(input('Enter principle = '))
r = int(input('Enter rate of interest = '))
t = int(input('Enter time period = '))

si = (p * r * t) / 100

print(si)