# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

first = int(input('Enter first term = '))
second = int(input('Enter second term = '))
n = int(input('Enter n value = '))

difference = second - first
nth = first + (n - 1) * difference

print('The nth term of this series is = ',nth)
