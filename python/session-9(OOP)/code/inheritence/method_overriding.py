class parent:

    def method(self):
        print('this is parent class method')


class child(parent):

    def method(self):
        print('this is child class method')


c = child()
print(c.method())