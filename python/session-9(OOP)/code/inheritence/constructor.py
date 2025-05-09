class parent:

    def __init__(self,pname,page):
        print('parent constructor')
        self.parentname = pname
        self.parentage = page


class child(parent):

    def __init__(self,cname,cage):
        print('child constructor')
        self.childname = cname
        self.childage = cage


c = child('najeeb',23)
