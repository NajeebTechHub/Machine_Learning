# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

h = int(input('Enter number of heads = '))
l = int(input('Enter number of legs = '))

# if l/h == 4:
#     print(f'There are {h} dogs and 0 chicken')
# else:
#     c = l/h
#     print(f'There are {c}')

c = (l - 4 * h) // 2 + h
d = h - c

print('Numbers of dogs = ',d)
print('Numbers of chickens = ',c)
