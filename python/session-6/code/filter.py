# filter is higher order function cause revieve function as input

l = [1,2,3,4,5,6,7,8,8,9,5,55,77]
a = list(filter(lambda x:x > 5,l))
print(a)