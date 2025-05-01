# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cost = int(input('Enter cost price : '))
sell = int(input('Enter selling price : '))

if cost < sell:
  print('profit',sell - cost)
elif cost > sell:
  print('loss',cost - sell)
else:
  print('no loss no profit')