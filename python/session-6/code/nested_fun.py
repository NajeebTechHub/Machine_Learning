def f(x):
    def g():
        x = 'abc'
    x = x + 1
    print('The x in f(x) is = ', x)
    g()
    return x

x = 3
z = f(x)