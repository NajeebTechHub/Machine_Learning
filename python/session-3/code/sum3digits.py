num = int(input("Enter 3 digit number = "))

# 345 % 10 = 5
a = num % 10

# 345 // 10 = 34
num = num // 10

# 345 % 10 = 4
b = num % 10

# 345 // 10 = 3
num = num // 10

# 345 % 10 = 3
c = num % 10

result = a + b + c

print(result)