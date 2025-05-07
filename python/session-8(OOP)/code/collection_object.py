class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


p1 = Person('najeeb','male')
p2 = Person('haseeb','male')
p3 = Person('anees','male')

L = [p1,p2,p3]
for i in L:
    print(i.name,i.gender)

dic = {'p1':p1,'p2':p2,'p3':p3}
for i in dic:
    print(dic[i].name)

set = {p1,p2,p3}
for i in set:
    print(i.name)