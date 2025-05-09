class parent:

    def fun(self):
        print('parent')

class child1(parent):
    pass

class child2(parent):
    pass

c1 = child1()
print(c1.fun())

c2 = child2()
print(c2.fun())