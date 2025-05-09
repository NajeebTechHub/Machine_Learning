class parent1:

    def fun1(self):
        print('this is first parent')

class parent2:

    def fun2(self):
        print('this is second parent')

# method resolution order
# first parent first priority
class child(parent1, parent2):
    
    def fun3(self):
        print('this is child')

c = child()
print(c.fun1())
print(c.fun2())
print(c.fun3())