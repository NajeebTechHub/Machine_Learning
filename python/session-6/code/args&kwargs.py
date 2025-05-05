# using *args you can give any number of arguments 
# instead of args you can use anything

def multiply(*args):
    product = 1
    for i in args:
        product = product * i
    return product

print(multiply(5,7,4,7))

# **kwargs can pass any number of key,value pair argument to function
# instead of kwargs you can use anything

def capital(**kwargs):
    for i,j in kwargs.items():
        print(i,'->',j ) 

capital(pakistan='islamabad',ind='delhi')