def g(x):
    def h(x):
        x = x + 1
        print('x in h(x) is = ',x)
    
    x = x + 1
    print('x in g(x) is = ',x)
    h(x)
    return x

x = 3
z = g(x)
print('x in main fun is = ',x)
print('z in main fun is = ',z)