# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

sum = 0
avg = 0
n = 1
i = 0
while n != 0:
  n = int(input('Enter any number : '))
  i = i + 1
  sum = sum + n
  
print('sum :',sum)
print('average :',sum / (i-1))