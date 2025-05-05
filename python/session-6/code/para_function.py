# default argument
def power(a = 1, b = 1):
    return a ** b

print(power(5))

# positional argument
print(power(5,2))

# keyword arguments
print(power(b = 4, a = 2))