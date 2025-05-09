class parent:

    def __init__(self):
        self.name = 'najeeb'

    def login(self):
        print('login')

class child(parent):

    def enroll(self):
        print('enroll')


c = child()
print(c.name)
print(c.login())
print(c.enroll())