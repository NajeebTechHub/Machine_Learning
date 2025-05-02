# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

n1 = int(input('Enter first nomerator = '))
d1 = int(input('Enter first denomerator = '))
n2 = int(input('Enter second nomerator = '))
d2 = int(input('Enter second denomerator = '))

f = ((n1 * d2) + (n2 * d1)) / (d1 * d2)

print(f)