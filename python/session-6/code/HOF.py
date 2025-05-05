def square(x):
    return x**2

# higher order function cause recieve function as input
def transform(f,l):
    output = []
    for i in l:
        output.append(f(i))
    print(output)

l = [1,2,3,4,5]
# transform(square,l)
transform(lambda x:x**2,l)