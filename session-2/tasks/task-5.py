# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two 
# numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 
# The next number in this series above is 13+21 = 34

series = []
for i in range(10):
  if i == 0 or i == 1:
    series.append(i)
  else:
    value = series[i - 1] + series[i - 2]
    series.append(value)
print(series)