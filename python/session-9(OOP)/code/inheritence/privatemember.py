class parent:

    def __init__(self,pname,page):
        self.__parentname = pname
        self.parentage = page

    def __show(self):
        print('private method')


class child(parent):
    pass


c = child('najeeb',23)

# can't access private members of parent class
# print(c.__parentname)
# print(c.__show)

print(c.parentage)