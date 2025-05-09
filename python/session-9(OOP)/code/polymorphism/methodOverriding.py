class parent:

    def fun1(self):
        print('parent')

class child(parent):

    def fun1(self):
        print('child')

c = child()
print(c.fun1())